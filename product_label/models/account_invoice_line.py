# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    product_label_description = fields.Char(
        string="Product Labels Description",
        compute="_compute_product_label_description")

    @api.depends("product_id.label_ids.display_on_invoice")
    def _compute_product_label_description(self):
        for line in self.filtered(lambda x: x.product_id):
            line.product_label_description = ", ".join(
                line.product_id.mapped('label_ids').filtered(
                    lambda x: x.display_on_invoice).mapped('code'))
