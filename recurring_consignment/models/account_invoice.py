# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    # Column Section
    is_consignment_invoice = fields.Boolean(
        string="Is Consignment Invoice", readonly=True
    )

    consignment_line_ids = fields.One2many(
        comodel_name="account.move.line",
        inverse_name="consignment_invoice_id",
        string="Commissionned Lines",
        readonly=True,
    )

    @api.constrains("partner_id")
    def _check_partner_id_recurring_consignment(self):
        self.mapped("invoice_line_ids")._check_invoice_line_recurring_consignment()

    # Report Function
    @api.model
    def get_commission_information_summary(self, invoice):
        AccountMoveLine = self.env["account.move.line"]
        groups = {}
        res = []
        sorted_lines = AccountMoveLine.search(
            [("id", "in", invoice.consignment_line_ids.ids)],
            order="tax_line_id desc, name",
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

    @api.model
    def get_commission_information_accounting_detail(self, invoice):
        AccountMoveLine = self.env["account.move.line"]
        res = []
        sorted_lines = AccountMoveLine.search(
            [("id", "in", invoice.consignment_line_ids.ids)],
            order="date, move_id, tax_line_id desc, name",
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

    @api.model
    def get_commission_information_product_detail(self, invoice):
        ProductProduct = self.env["product.product"]

        res = []

        # Get Product ids
        consignor_products = ProductProduct.with_context(active_test=False).search(
            [("consignor_partner_id", "=", invoice.partner_id.id)]
        )

        # Get Account Move
        moves = invoice.mapped("consignment_line_ids.move_id")

        groups = self.get_commission_information_product_detail_grouped(
            consignor_products, moves
        )

        # Compute sum of each product
        for key, value in groups.items():
            (product_id, price_unit, discount) = key
            product = ProductProduct.browse(product_id)
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
    @api.model
    def get_commission_information_product_detail_grouped(
        self, consignor_products, moves
    ):
        AccountInvoice = self.env["account.invoice"]
        AccountInvoiceLine = self.env["account.invoice.line"]

        groups = {}

        # Get related invoice
        com_invoices = AccountInvoice.search([("move_id", "in", moves.ids)])

        com_invoice_lines = AccountInvoiceLine.search(
            [
                ("invoice_id", "in", com_invoices.ids),
                ("product_id", "in", consignor_products.ids),
            ]
        )

        for com_invoice_line in com_invoice_lines:
            key = (
                com_invoice_line.product_id.id,
                com_invoice_line.price_unit,
                com_invoice_line.discount,
            )
            groups.setdefault(
                key,
                {
                    "quantity": 0,
                    "total_vat_excl": 0,
                },
            )
            if com_invoice_line.invoice_id.type == "out_invoice":
                quantity = com_invoice_line.quantity
            else:
                quantity = -com_invoice_line.quantity

            groups[key] = {
                "quantity": groups[key]["quantity"] + quantity,
                "total_vat_excl": groups[key]["total_vat_excl"]
                + com_invoice_line.price_subtotal_signed,
            }
        return groups

    @api.model
    def _get_commission_key(self, move_line):
        if move_line.tax_line_id.consignment_product_id:
            tax = move_line.tax_line_id
            # That is Tax line
            return ("tax", _("Tax Collected %s") % (tax.amount))
        else:
            return (
                "revenue",
                _("Income Collected. Taxes: %s")
                % (", ".join([str(x.amount) for x in move_line.tax_ids])),
            )
