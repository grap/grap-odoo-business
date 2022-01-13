# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, models
from odoo.exceptions import Warning as UserError


class AccountInvoiceLine(models.Model):
    _inherit = ["account.invoice.line", "recurring.consignment.line.mixin"]
    _name = "account.invoice.line"

    @api.constrains("product_id")
    def _check_invoice_line_recurring_consignment(self):
        for line in self:
            if (
                line.invoice_id.partner_id.is_consignor
                and not line.product_id.is_consignment_commission
            ):
                raise UserError(
                    _(
                        "You can only sale consignment Commission to consignor."
                        " If you want to sale regular products, please create"
                        " another customer"
                    )
                )
            if (
                not line.invoice_id.partner_id.is_consignor
                and line.product_id.is_consignment_commission
            ):
                raise UserError(
                    _(
                        "You can not sale consignment commission to a customer"
                        " that are not flagged as consignor"
                    )
                )
