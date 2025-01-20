# Copyright (C) 2025 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    display_organic_column = fields.Boolean(compute="_compute_display_organic_column")

    def _compute_display_organic_column(self):
        for move in self:
            move.display_organic_column = "01_organic" in move.mapped(
                "order_line.product_id.organic_type"
            )
