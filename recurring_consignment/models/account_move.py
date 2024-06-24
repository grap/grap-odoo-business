# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import Command, _, api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    is_consignment_invoice = fields.Boolean(readonly=True)

    def action_post(self):
        consignment_invoice_first_posted = self.filtered(
            lambda x: not x.posted_before and x.is_consignment_invoice
        )
        res = super().action_post()
        consignment_invoice_first_posted._recurring_consigment_mark_as_paid()
        return res

    def _recurring_consigment_mark_as_paid(self):
        # The first time a commission invoice is posted, create
        # a Miscellanious Operation to transfer amount from 'Receivable' account
        # to 'Receivable / Payable' account
        # and mark the invoice as paid

        for move in self:
            receivable_line = move.line_ids.filtered(
                lambda x: x.display_type == "payment_term"
            )
            credit_vals = {
                "account_id": receivable_line.account_id.id,
                "partner_id": move.partner_id.id,
                "debit": receivable_line.credit,
                "credit": receivable_line.debit,
            }
            debit_vals = {
                "account_id": move.partner_id.consignment_account_id.id,
                "partner_id": move.partner_id.id,
                "debit": receivable_line.debit,
                "credit": receivable_line.credit,
            }
            misc_move_vals = {
                "journal_id": move.company_id.commission_deduction_journal_id.id,
                "date": move.date,
                "ref": _(
                    "deduction of %(move_name)s on the amount to be repaid",
                    move_name=move.name,
                ),
                "move_type": "entry",
                "line_ids": [Command.create(credit_vals), Command.create(debit_vals)],
            }

            misc_move = self.create(misc_move_vals)
            misc_move.action_post()
            move.js_assign_outstanding_line(
                misc_move.line_ids.filtered(
                    lambda x, line=receivable_line: x.account_id == line.account_id
                ).id
            )

    # View Section
    def button_commission_view_invoice_lines(self):
        invoice_lines = self.mapped("invoice_line_ids.consignment_invoice_line_ids")
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "account.action_move_line_select"
        )
        action["domain"] = [("id", "in", invoice_lines.ids)]
        action["context"] = {}
        return action

    # Report Function
    def get_commission_information_summary(self):
        """Return a detailled dictionnary that will be used in report for the consignor,
        after the invoice pages in the section named 'Commission Summary'
        """
        groups = {}
        res = []
        sorted_lines = self.invoice_line_ids.consignment_invoice_line_ids.sorted(
            key=lambda x: (x.tax_line_id, x.name)
        )
        for move_line in sorted_lines:
            key = self._get_commission_key(move_line)
            groups.setdefault(key, [])
            groups[key].append(move_line)
        for key, value in groups.items():
            (kind, name) = key
            amount = 0
            for move_line in value:
                amount += move_line.credit - move_line.debit
            res.append(
                {
                    "type": kind,
                    "name": name,
                    "amount": amount,
                    "is_commission": (kind == "revenue"),
                }
            )
        return res

    def get_commission_information_accounting_detail(self):
        """Return a detailled dictionnary that will be used in report for the consignor,
        after the invoice pages in the section named 'Account Moves Details'
        """
        res = []
        sorted_lines = self.invoice_line_ids.consignment_invoice_line_ids.sorted(
            key=lambda x: (x.date, x.move_id.name, not x.tax_line_id, x.name)
        )
        for move_line in sorted_lines:
            tmp = self._get_commission_key(move_line)
            res.append(
                {
                    "date": move_line.date,
                    "name": move_line.move_id.name,
                    "description": tmp[1],
                    "debit": move_line.debit,
                    "credit": move_line.credit,
                    "is_commission": tmp[0] == "revenue",
                }
            )
        return res

    def get_commission_information_product_detail(self):
        """Return a detailled dictionnary that will be used in report for the consignor,
        after the invoice pages in the section named 'Product Details'
        """
        res = []
        groups = self._get_commission_information_product_detail_grouped()

        # Compute sum of each product
        for key, value in groups.items():
            (product, price_unit, discount) = key
            res.append(
                {
                    "product_code": product.default_code,
                    "product_name": product.name,
                    "price_unit": price_unit,
                    "discount": discount,
                    "quantity": value["quantity"],
                    "total_vat_excl": value["total_vat_excl"],
                }
            )
        return sorted(
            res, key=lambda k: (k["product_name"], -k["price_unit"], k["discount"])
        )

    # Private Function
    def _get_commission_information_product_detail_grouped(self):
        """Overload this function in extra consignment module
        to return the detailled list of product that have been commissionned
        by this invoice. (for exemple in recurring_consignment_pos)
        """
        groups = {}

        # Get related invoice lines
        com_invoice_lines = self.mapped(
            "invoice_line_ids.consignment_invoice_line_ids"
        ).filtered(lambda x: x.display_type == "product" and x.product_id)

        for com_invoice_line in com_invoice_lines:
            key = (
                com_invoice_line.product_id,
                com_invoice_line.price_unit,
                com_invoice_line.discount,
            )
            groups.setdefault(key, {"quantity": 0, "total_vat_excl": 0})
            if com_invoice_line.move_id.move_type == "out_invoice":
                groups[key]["quantity"] += com_invoice_line.quantity
                groups[key]["total_vat_excl"] += com_invoice_line.price_subtotal
            else:
                groups[key]["quantity"] -= com_invoice_line.quantity
                groups[key]["total_vat_excl"] -= com_invoice_line.price_subtotal

        return groups

    @api.model
    def _get_commission_key(self, move_line):
        if move_line.tax_line_id:
            # That is a Tax line
            return ("tax", _("Tax Collected %s") % (move_line.tax_line_id.amount))

        # That is a Revenue line
        return (
            "revenue",
            _("Income Collected. Taxes: %s")
            % (", ".join([str(x.amount) for x in move_line.tax_ids])),
        )
