# Copyright (C) 2025 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    def _get_aggregated_properties(self, move_line=False, move=False):
        res = super()._get_aggregated_properties(move_line=move_line, move=move)
        line = move_line and move_line or move
        if not line:
            return res
        res.update(
            {
                "organic_type": line.product_id.organic_type,
                "display_organic_column": line.picking_id.display_organic_column,
            }
        )
        return res
