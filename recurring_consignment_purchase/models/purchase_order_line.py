# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, models
from odoo.exceptions import UserError


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order"

    @api.constrains("product_id")
    def _check_order_line_recurring_consignment(self):
        for line in self:
            if line.order_id.consignment_trade and not line.product_id.is_consignment:
                raise UserError(
                    _("You can only purchase consigned products to consignor.")
                )
            if not line.order_id.consignment_trade and line.product_id.is_consignment:
                raise UserError(
                    _(
                        "You can not purchase consigned products to a supplier"
                        " that is not flagged as consignor."
                    )
                )
