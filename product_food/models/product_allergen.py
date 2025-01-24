# Copyright (C) 2020 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductAllergen(models.Model):
    _name = "product.allergen"
    _description = "Allergens"

    code = fields.Char()

    name = fields.Char(required=True)

    active = fields.Boolean(default=True)

    website = fields.Char()

    note = fields.Text()

    product_ids = fields.Many2many(
        comodel_name="product.product",
        relation="product_allergen_product_rel",
        column1="allergen_id",
        column2="product_id",
    )

    product_qty = fields.Integer(
        string="Products Quantity", compute="_compute_product_qty"
    )

    @api.depends("product_ids")
    def _compute_product_qty(self):
        for allergen in self:
            allergen.product_qty = len(allergen.product_ids)
