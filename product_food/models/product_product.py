# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError


class ProductProduct(models.Model):
    _inherit = "product.product"

    _STORAGE_METHOD_SELECTION = [
        ("fresh", "Fresh (< 10°)"),
        ("cool", "Cool (< 4°)"),
        ("frozen", "Frozen (< -18°)"),
    ]

    is_alimentary = fields.Boolean()

    is_vegan = fields.Boolean()

    has_alcohol = fields.Boolean()

    alcohol_by_volume = fields.Float()

    use_by_date_day = fields.Integer()

    best_before_date_day = fields.Integer()

    storage_method = fields.Selection(selection=_STORAGE_METHOD_SELECTION)

    ingredients = fields.Html(sanitize=False)

    allergen_ids = fields.Many2many(
        comodel_name="product.allergen",
        relation="product_allergen_product_rel",
        column1="product_id",
        column2="allergen_id",
    )

    trace_allergen_ids = fields.Many2many(
        string="Allergens (Traces)",
        comodel_name="product.allergen",
        relation="product_allergen_trace_product_rel",
        column1="product_id",
        column2="allergen_id",
    )

    # Constrains Section
    @api.constrains("alcohol_by_volume")
    def _check_alcohol_by_volume(self):
        if self.filtered(
            lambda x: x.alcohol_by_volume < 0 or x.alcohol_by_volume > 100
        ):
            raise UserError(
                _(
                    "Incorrect Setting. Alcohol by volume should be"
                    " between 0 and 100."
                )
            )

    # Onchange Section
    @api.onchange("categ_id")
    def onchange_categ_id_product_food(self):
        if self.categ_id:
            self.is_alimentary = self.categ_id.is_alimentary
            self.has_alcohol = self.categ_id.has_alcohol
            self.is_vegan = self.categ_id.is_vegan

    @api.onchange("label_ids")
    def onchange_label_ids_product_food(self):
        if self.label_ids.filtered(lambda x: x.is_vegan):
            self.is_vegan = True

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if "categ_id" in vals:
                # Guess values if not present, based on the category
                categ = self.env["product.category"].browse(vals.get("categ_id"))
                if "is_alimentary" not in vals:
                    vals["is_alimentary"] = categ.is_alimentary
                if "has_alcohol" not in vals:
                    vals["has_alcohol"] = categ.has_alcohol
                if "is_vegan" not in vals:
                    vals["is_vegan"] = categ.is_vegan
        return super().create(vals_list)
