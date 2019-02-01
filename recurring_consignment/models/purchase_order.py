# coding: utf-8
# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author: Quentin DUPONT (https://twitter.com/pondupont)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    consignment_trade = fields.Boolean(
        string='Consignment Trade', related='partner_id.is_consignor')

    # Override Section
    # Make purchase order not to be invoiced
    @api.model
    def _prepare_order_line_move(
            self, order, order_line, picking_id, group_id):
        res = super(PurchaseOrder, self)._prepare_order_line_move(
            order, order_line, picking_id, group_id)
        if order.consignment_trade:
            for item in res:
                item['invoice_state'] = 'none'
        return res
