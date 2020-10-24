# Copyright (C) 2017 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import timedelta

from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError


class InvoiceCommissionWizard(models.TransientModel):
    _name = 'invoice.commission.wizard'
    _description = "Invoice Commission Wizard"

    # Columns Section
    max_date = fields.Date(
        string="Max Date",
        required=True,
        default=lambda x: x._default_max_date(),
        help="The commission will be computed for the sale"
        " until this date included.")

    wizard_line_ids = fields.One2many(
        comodel_name="invoice.commission.wizard.line",
        inverse_name="wizard_id",
        default=lambda x: x._default_wizard_line_ids())

    # Default values Section
    def _default_wizard_line_ids(self):
        ResPartner = self.env['res.partner']
        WizardLine = self.env["invoice.commission.wizard.line"]
        consignors = ResPartner.browse(self.env.context.get('active_ids', []))
        line_vals = []
        for consignor in consignors.filtered(lambda x: x.is_consignor):
            line_vals.append(
                (0, 0, {
                    'partner_id': consignor.id,
                    'consignment_account_id': consignor.consignment_account_id,
                    'consignment_commission': consignor.consignment_commission,
                    'move_line_qty': len(
                        WizardLine._get_move_lines_with_values(
                            consignor, self._default_max_date()))
                })
            )
        return line_vals

    def _default_max_date(self):
        today = fields.date.today()
        return fields.date(today.year, today.month, 1) - timedelta(days=1)

    @api.onchange("max_date")
    def _onchange_max_date(self):
        for wizard_line in self.wizard_line_ids:
            wizard_line.move_line_qty = len(wizard_line._get_move_lines())

    # Action Section
    @api.multi
    def invoice_commission(self):
        self.ensure_one()
        move_AccountMoveLine = self.env['account.move.line']
        AccountInvoice = self.env['account.invoice']
        invoice_ids = []
        grouped_data = {}

        for wizard_line in self.wizard_line_ids:

            if not wizard_line.move_line_qty:
                continue

            # Create Commission Invoice
            invoice_vals = wizard_line._prepare_invoice()
            invoice = AccountInvoice.create(invoice_vals)
            invoice_ids.append(invoice.id)

            # Get lines to commission
            all_lines = wizard_line._get_move_lines()

            for product_line in all_lines.filtered(
                    lambda x: not x.tax_line_id):
                # We select only product lines (=non tax lines)
                key = wizard_line._get_line_key(product_line)
                grouped_data.setdefault(key, [])
                grouped_data[key].append(product_line)

            # Create lines
            for key, product_lines in grouped_data.items():
                current_line_ids = [x.id for x in product_lines]
                wizard_line._create_invoice_line(key, product_lines, invoice)

                # Mark Move lines as commisssioned
                current_lines = move_AccountMoveLine.browse(current_line_ids)
                current_lines.write({
                    'consignment_invoice_id': invoice.id,
                    'consignment_commission':
                    wizard_line.consignment_commission,
                })

            # Mark taxes Move lines as no commisssioned
            all_lines.filtered(lambda x: x.tax_line_id).write({
                'consignment_invoice_id': invoice.id,
                'consignment_commission': 0,
            })

        if not invoice_ids:
            raise UserError(_(
                "There is no move lines to commission for there consignors"
                " and this date."))

        # Recompute Taxes
        invoices = AccountInvoice.browse(invoice_ids)
        invoices.compute_taxes()

        # Return action that displays new invoices
        action = self.env.ref('account.action_invoice_tree1').read()[0]

        if len(invoices) > 1:
            action['domain'] =\
                "[('id', 'in', [" + ','.join(map(str, invoices.ids)) + "])]"
        else:
            form_view = [(self.env.ref('account.invoice_form').id, 'form')]
            action['views'] = form_view + [
                (state, view) for state, view in action.get('views', [])
                if view != 'form'
            ]
            action['res_id'] = invoices.ids[0]

        return action
