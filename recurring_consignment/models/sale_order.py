# coding: utf-8
# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.constrains('partner_id')
    def _check_partner_id_recurring_consignment(self):
        self.mapped('order_line')._check_order_line_recurring_consignment()
