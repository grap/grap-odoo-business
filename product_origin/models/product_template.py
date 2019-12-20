# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import api, fields, models
from .product_product import ProductProduct


class ProductTemplate(models.Model):
    _inherit = "product.template"

    country_id = fields.Many2one(
        comodel_name="res.country",
        related="product_variant_ids.country_id",
        string="Country",
        help="Country of production of the product",
        readonly=False,
    )

    state_id = fields.Many2one(
        comodel_name="res.country.state",
        related="product_variant_ids.state_id",
        string="State",
        help="State of production of the product",
        readonly=False,
    )

    origin_description = fields.Char(
        related="product_variant_ids.origin_description",
        string="Production Origin Complement",
        readonly=False,
    )

    maker_description = fields.Char(
        related="product_variant_ids.maker_description",
        string="Maker",
        readonly=False,
    )

    # Onchange section
    @api.onchange("state_id")
    def onchange_state_id(self):
        ProductProduct.onchange_state_id(self)

    @api.onchange("country_id")
    def onchange_country_id(self):
        ProductProduct.onchange_country_id(self)
