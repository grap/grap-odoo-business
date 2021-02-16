# Copyright (C) 2020 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    label_ids = fields.Many2many(
        comodel_name="product.label", string="Labels", compute="_compute_label_ids"
    )

    @api.depends("order_line.product_id.label_ids.display_on_report")
    def _compute_label_ids(self):
        for invoice in self:
            invoice.label_ids = invoice.mapped(
                "order_line.product_id.label_ids"
            ).filtered(lambda x: x.display_on_report)
