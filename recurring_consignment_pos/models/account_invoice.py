# Copyright (C) 2020 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.model
    def get_commission_information_product_detail_grouped(
            self, consignor_products, moves):

        groups = super().get_commission_information_product_detail_grouped(
            consignor_products, moves)

        PosOrder = self.env['pos.order']
        PosOrderLine = self.env['pos.order.line']

        # Get related pos order
        com_orders = PosOrder.search([('account_move', 'in', moves.ids)])

        com_order_lines = PosOrderLine.search([
            ('order_id', 'in', com_orders.ids),
            ('product_id', 'in', consignor_products.ids),
        ])

        for com_order_line in com_order_lines:
            key = (
                com_order_line.product_id.id,
                com_order_line.price_unit,
                com_order_line.discount,
            )
            groups.setdefault(key, {
                'quantity': 0,
                'total_vat_excl': 0,
            })
            groups[key] = {
                'quantity': groups[key]['quantity']
                + com_order_line.qty,
                'total_vat_excl': groups[key]['total_vat_excl']
                + com_order_line.price_subtotal,
            }
        return groups
