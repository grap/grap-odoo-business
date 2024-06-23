# Copyright (C) 2017 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import timedelta

from odoo import Command, _, api, fields, models
from odoo.exceptions import ValidationError


class InvoiceCommissionWizard(models.TransientModel):
    _name = "invoice.commission.wizard"
    _description = "Invoice Commission Wizard"

    # Columns Section
    max_date = fields.Date(
        required=True,
        default=lambda x: x._default_max_date(),
        help="The commission will be computed for the sale"
        " until this date included.",
    )

    wizard_line_ids = fields.One2many(
        comodel_name="invoice.commission.wizard.line",
        inverse_name="wizard_id",
        default=lambda x: x._default_wizard_line_ids(),
    )

    # Default values Section
    def _default_wizard_line_ids(self):
        ResPartner = self.env["res.partner"]
        WizardLine = self.env["invoice.commission.wizard.line"]
        consignors = ResPartner.browse(self.env.context.get("active_ids", []))
        res = []
        for consignor in consignors.filtered(lambda x: x.is_consignor):
            line_vals = {
                "partner_id": consignor.id,
                "move_line_qty": len(
                    WizardLine._get_move_lines_with_values(
                        consignor, self._default_max_date()
                    )
                ),
            }
            res.append(Command.create(line_vals))
        return res

    def _default_max_date(self):
        today = fields.date.today()
        return fields.date(today.year, today.month, 1) - timedelta(days=1)

    # Onchange Section
    @api.onchange("max_date")
    def _onchange_max_date(self):
        for wizard_line in self.wizard_line_ids:
            wizard_line.move_line_qty = len(wizard_line._get_move_lines())

    # Action Section
    def invoice_commission(self):
        self.ensure_one()
        AccountMove = self.env["account.move"]

        commission_invoices = AccountMove

        for wizard_line in self.wizard_line_ids:
            if not wizard_line._get_move_lines():
                continue

            # Create Commission Invoice
            invoice_vals = wizard_line._prepare_invoice_vals()
            commission_invoices |= AccountMove.create(invoice_vals)

        if not commission_invoices:
            raise ValidationError(
                _(
                    "There is no move lines to commission for there consignors"
                    " and this date."
                )
            )

        # Return action that displays new invoices
        action = self.env["ir.actions.actions"]._for_xml_id(
            "account.action_move_out_invoice_type"
        )

        if len(commission_invoices) > 1:
            action["domain"] = (
                "[('id', 'in', [" + ",".join(map(str, commission_invoices.ids)) + "])]"
            )
        else:
            action["views"] = [(self.env.ref("account.view_move_form").id, "form")]
            action["res_id"] = commission_invoices.ids[0]

        return action
