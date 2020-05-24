# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author: Quentin DUPONT (https://twitter.com/pondupont)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    consignment_trade = fields.Boolean(
        string='Consignment Trade', related='partner_id.is_consignor')

    @api.multi
    def action_view_invoice(self):
        orders = self.filtered(lambda x: x.consignment_trade)
        if orders:
            raise UserError(_(
                "You can not make invoices for purchase order(s) %s"
                " because there are associated to consignor(s).") % (
                ', '.join([x.name for x in orders])))
        res = super().action_view_invoice()
        return res
