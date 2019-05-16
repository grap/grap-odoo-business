# coding: utf-8
# Copyright (C) 2019-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models

import openerp.addons.decimal_precision as dp


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_standard_price_updatable = fields.Boolean(
        string="Standard Price Updatable",
        compute="_compute_theoritical_standard_price")

    theoritical_standard_price = fields.Float(
        string="Theoritical Standard Price",
        compute="_compute_theoritical_standard_price",
        digits_compute=dp.get_precision("Product Price"))

    @api.multi
    @api.depends(
        'seller_ids.theoritical_standard_price')
    def _compute_theoritical_standard_price(self):
        for template in self:
            if not template.seller_ids:
                continue
            result = template.seller_ids[0].theoritical_standard_price
            template.theoritical_standard_price = result
            template.is_standard_price_updatable =\
                result and template.standard_price != result

    @api.multi
    def apply_theoritical_standard_price(self):
        for template in self:
            template.standard_price = template.theoritical_standard_price
