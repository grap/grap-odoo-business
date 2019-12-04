# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    # Onchange Section
    @api.onchange('consignor_partner_id')
    def onchange_consignor_partner_id_variant(self):
        ProductTemplate = self.env['product.template']
        ProductTemplate._onchange_consignor_partner_id(self)
