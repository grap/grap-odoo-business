# Copyright (C) 2020 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductAllergen(models.Model):
    _name = "product.allergen"
    _description = "Allergens"

    code = fields.Char(string="Code")

    name = fields.Char(string="Name", required=True)

    active = fields.Boolean(string="Active", default=True)

    company_id = fields.Many2one(comodel_name="res.company", string="Company")

    website = fields.Char(string="Website")

    note = fields.Text(string="Note")

    product_ids = fields.Many2many(
        comodel_name="product.product",
        relation="product_allergen_product_rel",
        column1="allergen_id",
        column2="product_id",
        string="Products",
    )

    product_qty = fields.Integer(
        string="Product Quantity", compute="_compute_product_qty")

    @api.multi
    @api.depends("product_ids")
    def _compute_product_qty(self):
        for allergen in self:
            allergen.product_qty = len(allergen.product_ids)
