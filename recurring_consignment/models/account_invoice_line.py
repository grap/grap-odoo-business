# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, models
from odoo.exceptions import Warning as UserError


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    @api.constrains("product_id", "company_id")
    def _check_invoice_line_recurring_consignment(self):

        for line in self:
            commission_product_id = line.company_id.commission_product_id
            if not commission_product_id:
                continue
            if (
                line.invoice_id.partner_id.is_consignor
                and line.product_id != commission_product_id
            ):
                raise UserError(
                    _(
                        "You can only sale consignment Commission to consignor."
                        " If you want to sale regular products, please create"
                        " another customer"
                    )
                )
