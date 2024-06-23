# Copyright (C) 2017 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import Command, _, api, fields, models
from odoo.exceptions import ValidationError


class InvoiceCommissionWizardLine(models.TransientModel):
    _name = "invoice.commission.wizard.line"
    _description = "Invoice Line Commission Wizard"

    # Columns Section
    wizard_id = fields.Many2one(
        comodel_name="invoice.commission.wizard", required=True, ondelete="cascade"
    )

    partner_id = fields.Many2one(
        string="Consignor",
        comodel_name="res.partner",
        required=True,
        domain="[('is_consignor', '=', True)]",
    )

    consignment_account_id = fields.Many2one(
        string="Account",
        comodel_name="account.account",
        readonly=True,
        required=True,
        related="partner_id.consignment_account_id",
    )

    consignment_commission = fields.Float(
        string="Commission Rate", related="partner_id.consignment_commission"
    )

    max_date = fields.Date(
        string="Max Date", related="wizard_id.max_date", required=True, readonly=True
    )

    move_line_qty = fields.Integer(string="Move Lines Quantity")

    # On change section
    @api.onchange("partner_id")
    def _onchange_partner_id(self):
        for wizard_line in self:
            wizard_line.move_line_qty = len(wizard_line._get_move_lines())

    # Prepare Section
    def _prepare_invoice_vals(self):
        self.ensure_one()
        AccountMoveLine = self.env["account.move.line"]

        invoice_vals = {
            "partner_id": self.partner_id.id,
            "invoice_date": self.max_date,
            "is_consignment_invoice": True,
            "move_type": "out_invoice",
            "invoice_line_ids": [],
        }

        # Categorize Move Lines to be commissioned
        all_lines = self._get_move_lines()
        grouped_lines = {}
        for line in all_lines:
            key = self._get_line_key(line)
            grouped_lines.setdefault(key, AccountMoveLine)
            grouped_lines[key] |= line

        # Add Commission lines vals
        for key, lines in grouped_lines.items():
            line_vals = self._prepare_invoice_line_vals(key, lines)
            invoice_vals["invoice_line_ids"].append(Command.create(line_vals))

        return invoice_vals

    def _prepare_invoice_line_vals(self, key, lines):
        commission_product = self.partner_id.company_id.commission_product_id
        if not commission_product:
            raise ValidationError(
                _(
                    "you can not create a consignment invoice because you"
                    " didn't defined a Consignment product at the company"
                    " level. (%s)"
                )
                % self.partner_id.company_id.name
            )

        # compute Unit price, based on product line to commission
        total_credit = 0
        for line in lines.filtered(lambda x: not x.tax_line_id):
            total_credit += line.credit - line.debit

        price_unit = total_credit * self.consignment_commission / 100

        # Handle correct computaton of Price Unit, depending on
        # if the product is vat excl or vat Incl.
        taxes = commission_product.taxes_id
        if taxes:
            if len(taxes) != 1:
                raise ValidationError(
                    _(
                        "Incorrect fiscal settings block the possibility"
                        " to generate commission invoices:"
                        " Too many taxes %(tax_names)s",
                        tax_names=", ".join(taxes.mapped("name")),
                    )
                )
            if taxes[0].amount_type != "percent":
                raise ValidationError(
                    _(
                        "Incorrect fiscal settings block the possibility"
                        " to generate commission invoices : Incorrect tax type"
                        " on the tax %(tax_name)s",
                        tax_name=taxes[0].name,
                    )
                )
            if taxes[0].price_include:
                price_unit = price_unit * (100 + taxes[0].amount) / 100

        return {
            "product_id": commission_product.id,
            "quantity": 1,
            "price_unit": price_unit,
            "name": _(
                "Commission on Sale or Refunds\n"
                "(Rate : %(rate).2f %%; Base : %(total_credit).2f € ;"
                " Period %(month)s-%(year)s)",
                rate=self.partner_id.consignment_commission,
                total_credit=total_credit,
                month=key[0],
                year=key[1],
            ),
            "consignment_invoice_line_ids": [Command.link(line.id) for line in lines],
        }

    # Private Section
    @api.model
    def _get_line_key(self, move_line):
        return (
            move_line.move_id.date.year,
            move_line.move_id.date.month,
        )

    @api.model
    def _get_move_lines_with_values(self, partner, max_date):
        if not (partner and max_date):
            return []

        AccountJournal = self.env["account.journal"]
        AccountMoveLine = self.env["account.move.line"]
        journals = AccountJournal.search([("type", "in", ["sale", "sale_refund"])])

        # Get lines to commission
        domain = [
            ("date", "<=", max_date),
            ("account_id", "=", partner.consignment_account_id.id),
            ("journal_id", "in", journals.ids),
            ("consignment_invoice_line_id", "=", False),
            ("parent_state", "=", "posted"),
        ]
        res = AccountMoveLine.search(domain, order="date, move_id, tax_line_id")
        return res

    def _get_move_lines(self):
        self.ensure_one()
        return self._get_move_lines_with_values(self.partner_id, self.max_date)
