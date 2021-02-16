# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class ProductPricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    @api.model
    def _prepare_consignment_exception(self, pricelist, template):
        return {
            "pricelist_id": pricelist.id,
            "product_tmpl_id": template.id,
            "applied_on": "1_product",
            "base": "pricelist",
            "compute_price": "formula",
            "base_pricelist_id": pricelist.consignment_pricelist_id.id,
        }
