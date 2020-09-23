# Copyright (C) 2017 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from datetime import timedelta

from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError


class InvoiceCommissionWizardLine(models.TransientModel):
    _name = 'invoice.commission.wizard.line'
    _description = "Invoice Line Commission Wizard"

    # Columns Section
    wizard_id = fields.Many2one(
        comodel_name="invoice.commission.wizard", required=True,
        ondelete="cascade")

    partner_id = fields.Many2one(
        string='Consignor', comodel_name='res.partner', required=True,
        domain="[('is_consignor', '=', True)]")

    consignment_account_id = fields.Many2one(
        string="Account", comodel_name="account.account", readonly=True,
        required=True, related="partner_id.consignment_account_id")

    consignment_commission = fields.Float(
        string='Commission Rate',
        related="partner_id.consignment_commission")

    max_date = fields.Date(
        string="Max Date", related="wizard_id.max_date", required=True,
        readonly=True)

    move_line_qty = fields.Integer(string='Move Lines Quantity')

    # On change section
    @api.onchange("partner_id")
    def _onchange_partner_id(self):
        for wizard_line in self:
            wizard_line.move_line_qty = len(wizard_line._get_move_lines())

    # Prepare Section
    @api.multi
    def _prepare_invoice(self):
        self.ensure_one()
        partner = self.partner_id
        date_invoice = self.max_date - timedelta(days=1)
        return {
            'partner_id': partner.id,
            'date_invoice': date_invoice,
            'is_consignment_invoice': True,
            'type': 'out_invoice',
            'account_id': self.consignment_account_id.id,
            'fiscal_position_id': partner.property_account_position_id.id,
        }

    @api.multi
    def _create_invoice_line(self, key, lines, invoice):
        # [MIGRATION] Odoo >13
        # remove call of _onchange_product_id() and refactor this function
        self.ensure_one()
        AccountInvoiceLine = self.env['account.invoice.line']

        rate = self.partner_id.consignment_commission
        product = lines[0].tax_ids[0].consignment_product_id
        total_credit = 0
        for line in lines:
            total_credit += line.credit - line.debit

        price_unit = total_credit * rate / 100

        vals = {
            'invoice_id': invoice.id,
            'product_id': product.id,
            'account_id': product.property_account_income_id.id,
            'quantity': 1,
            'price_unit': price_unit,
            'name': _(
                "Commission on Sale or Refunds\n"
                "(Rate : %.2f %%; Base : %.2f € ; Period %s-%s)") % (
                rate, total_credit,
                key[0], key[1]),
        }

        move_line = AccountInvoiceLine.create(vals)
        move_line._onchange_product_id()

        # Compute price, depending on the tax settings
        taxes = move_line.invoice_line_tax_ids
        if len(taxes) != 1:
            raise UserError(_(
                "Incorrect fiscal settings block the possibility"
                " to generate commission invoices : Too many taxes %s") % (
                ', '.join(taxes.mapped('name'))))

        tax = taxes[0]
        if tax.amount_type != 'percent':
            raise UserError(_(
                "Incorrect fiscal settings block the possibility"
                " to generate commission invoices : Incorrect tax type"
                " on the tax %s") % (tax.name))

        # Rewrite name and price_unit, because on change erased correct values
        if tax.price_include:
            move_line.price_unit = price_unit * (100 + tax.amount) / 100
        else:
            move_line.price_unit = price_unit

        move_line.name = vals['name']
        return move_line

    # Private Section
    @api.model
    def _get_line_key(self, move_line):
        date = move_line.move_id.date
        return (date.year, date.month, str(set(move_line.tax_ids.ids)))

    @api.model
    def _get_move_lines_with_values(self, partner, max_date):
        if not (partner and max_date):
            return []

        AccountInvoice = self.env['account.invoice']
        AccountJournal = self.env['account.journal']
        AccountMoveLine = self.env['account.move.line']

        # Get Lines to ignore
        ignore_move_line_ids = AccountInvoice.search([
            ('is_consignment_invoice', '=', True),
            ('partner_id', '=', partner.id),
        ]).mapped('move_id.line_ids').ids

        journals = AccountJournal.search([
            ('type', 'in', ['sale', 'sale_refund'])])

        # Get lines to commission
        domain = [
            ('date', '<', max_date),
            ('account_id', '=', partner.consignment_account_id.id),
            ('journal_id', 'in', journals.ids),
            ('consignment_invoice_id', '=', False),
            ('id', 'not in', ignore_move_line_ids),
        ]
        res = AccountMoveLine.search(
            domain, order='date, move_id, tax_ids, tax_line_id')
        return res

    @api.multi
    def _get_move_lines(self):
        self.ensure_one()
        return self._get_move_lines_with_values(self.partner_id, self.max_date)
