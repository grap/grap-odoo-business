# Copyright (C) 2020 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    # View Section
    @api.multi
    def button_commission_view_pos_order_lines(self):
        pos_order_lines = self._get_commission_related_pos_order_lines()
        action = self.env.ref("point_of_sale.action_pos_all_sales_lines")
        action_data = action.read()[0]
        action_data["domain"] = [("id", "in", pos_order_lines.ids)]
        return action_data

    # Private Section
    @api.multi
    def _get_commission_related_pos_order_lines(self):
        PosOrder = self.env["pos.order"]
        PosOrderLine = self.env["pos.order.line"]
        ProductProduct = self.env["product.product"]

        # Get Account Move
        moves = self.mapped("consignment_line_ids.move_id")

        # Get Product ids
        consignor_products = ProductProduct.with_context(active_test=False).search(
            [("consignor_partner_id", "in", self.mapped("partner_id").ids)]
        )

        # Get related pos orders
        com_orders = PosOrder.search([("account_move", "in", moves.ids)])

        # We add pos.order.line sales, that are not invoiced
        # because the lines are still include in the module
        # recurring_consignement, in the original function
        # get_commission_information_product_detail_grouped.
        return PosOrderLine.search(
            [
                ("order_id", "in", com_orders.ids),
                ("order_id.state", "!=", "invoiced"),
                ("product_id", "in", consignor_products.ids),
            ]
        )

    @api.multi
    def _get_commission_information_product_detail_grouped(self):
        groups = super().get_commission_information_product_detail_grouped()

        # Get related pos order lines
        com_order_lines = self._get_commission_related_pos_order_lines()

        for com_order_line in com_order_lines:
            key = (
                com_order_line.product_id.id,
                com_order_line.price_unit,
                com_order_line.discount,
            )
            groups.setdefault(
                key,
                {
                    "quantity": 0,
                    "total_vat_excl": 0,
                },
            )
            groups[key] = {
                "quantity": groups[key]["quantity"] + com_order_line.qty,
                "total_vat_excl": groups[key]["total_vat_excl"]
                + com_order_line.price_subtotal,
            }
        return groups
