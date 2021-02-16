# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductPricetagType(models.Model):
    _name = "product.pricetag.type"
    _description = "Product Pricetag Types"

    # Column Section
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        default=lambda s: s._default_company_id(),
    )

    name = fields.Char(string="Name", required=True)

    color = fields.Char(
        string="Color",
        required=True,
        default="#FFFFFF",
        size=7,
        help="Color of the Pricetag by default. Format #RRGGBB",
    )

    product_ids = fields.One2many(
        string="Products",
        comodel_name="product.product",
        inverse_name="pricetag_type_id",
    )

    product_qty = fields.Integer(
        string="Products Quantity", compute="_compute_product_qty", store=True
    )

    @api.depends("product_ids")
    def _compute_product_qty(self):
        for pricetag_type in self:
            pricetag_type.product_qty = len(pricetag_type.product_ids)

    # Default Section
    @api.model
    def _default_company_id(self):
        return self.env.user.company_id.id
