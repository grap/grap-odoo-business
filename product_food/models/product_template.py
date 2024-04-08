# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models

from .product_product import ProductProduct


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # Column Section
    is_alimentary = fields.Boolean(
        string="Is Alimentary",
        related="product_variant_ids.is_alimentary",
        readonly=False,
    )

    alcohol_by_volume = fields.Float(
        string="Alcohol by Volume",
        related="product_variant_ids.alcohol_by_volume",
        readonly=False,
    )

    is_alcohol = fields.Boolean(
        string="Contain Alcohol",
        related="product_variant_ids.is_alcohol",
        readonly=False,
    )

    is_vegan = fields.Boolean(
        string="Is Vegan",
        related="product_variant_ids.is_vegan",
        readonly=False,
    )

    use_by_date_day = fields.Integer(
        string="Use-by Date Day",
        related="product_variant_ids.use_by_date_day",
        readonly=False,
    )

    best_before_date_day = fields.Integer(
        string="Best Before Date Day",
        related="product_variant_ids.best_before_date_day",
        readonly=False,
    )

    storage_method = fields.Selection(
        string="Storage Method",
        related="product_variant_ids.storage_method",
        selection=lambda self: self.env["product.product"]
        ._fields["storage_method"]
        .selection,
    )

    ingredients = fields.Text(
        string="Ingredients",
        related="product_variant_ids.ingredients",
        readonly=False,
    )

    allergen_ids = fields.Many2many(
        comodel_name="product.allergen",
        related="product_variant_ids.allergen_ids",
        string="Allergens",
        readonly=False,
    )

    trace_allergen_ids = fields.Many2many(
        comodel_name="product.allergen",
        related="product_variant_ids.trace_allergen_ids",
        string="Allergens (Traces)",
        readonly=False,
    )

    # Onchange Section
    @api.onchange("categ_id")
    def onchange_categ_id_product_food(self):
        ProductProduct.onchange_categ_id_product_food(self)

    @api.onchange("label_ids")
    def onchange_label_ids_product_food(self):
        ProductProduct.onchange_label_ids_product_food(self)

    @api.onchange("is_alimentary")
    def onchange_is_alimentary(self):
        ProductProduct.onchange_is_alimentary(self)

    @api.onchange("is_alcohol")
    def onchange_is_alcohol(self):
        ProductProduct.onchange_is_alcohol(self)
