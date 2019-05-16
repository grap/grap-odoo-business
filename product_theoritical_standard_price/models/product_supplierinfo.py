# coding: utf-8
# Copyright (C) 2019-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models

import openerp.addons.decimal_precision as dp


class ProductSupplierinfo(models.Model):
    _inherit = 'product.supplierinfo'

    theoritical_standard_price = fields.Float(
        string="Theoritical Standard Price",
        compute="_compute_theoritical_standard_price",
        digits_compute=dp.get_precision("Product Price"))

    @api.multi
    @api.depends(
        'pricelist_ids.price', 'pricelist_ids.discount',
        'pricelist_ids.discount2', 'pricelist_ids.discount3')
    def _compute_theoritical_standard_price(self):
        for supplierinfo in self:
            if not supplierinfo.pricelist_ids:
                continue
            partnerinfo = supplierinfo.pricelist_ids[0]
            template = supplierinfo.product_tmpl_id
            uom_id = template.uom_id
            purchase_uom_id = supplierinfo.product_uom
            if uom_id == purchase_uom_id:
                factor = 1
            else:
                factor = purchase_uom_id.factor_inv / uom_id.factor_inv

            supplierinfo.theoritical_standard_price = (
                partnerinfo.price *
                (1 - partnerinfo.discount / 100) *
                (1 - partnerinfo.discount2 / 100) *
                (1 - partnerinfo.discount3 / 100)) / factor

    @api.multi
    def apply_theoritical_standard_price(self):
        for supplierinfo in self:
            supplierinfo.product_tmpl_id.standard_price =\
                self.theoritical_standard_price
