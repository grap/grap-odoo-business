# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models

from .product_product import ProductProduct


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_alimentary = fields.Boolean(
        compute=lambda x: x._compute_template_field_from_variant_field("is_alimentary"),
        inverse=lambda x: x._set_product_variant_field("is_alimentary"),
        readonly=False,
    )

    alcohol_by_volume = fields.Float(
        compute=lambda x: x._compute_template_field_from_variant_field(
            "alcohol_by_volume"
        ),
        inverse=lambda x: x._set_product_variant_field("alcohol_by_volume"),
        readonly=False,
    )

    has_alcohol = fields.Boolean(
        compute=lambda x: x._compute_template_field_from_variant_field("has_alcohol"),
        inverse=lambda x: x._set_product_variant_field("has_alcohol"),
        readonly=False,
    )

    is_vegan = fields.Boolean(
        compute=lambda x: x._compute_template_field_from_variant_field("is_vegan"),
        inverse=lambda x: x._set_product_variant_field("is_vegan"),
        readonly=False,
    )

    use_by_date_day = fields.Integer(
        compute=lambda x: x._compute_template_field_from_variant_field(
            "use_by_date_day"
        ),
        inverse=lambda x: x._set_product_variant_field("use_by_date_day"),
        readonly=False,
    )

    best_before_date_day = fields.Integer(
        compute=lambda x: x._compute_template_field_from_variant_field(
            "best_before_date_day"
        ),
        inverse=lambda x: x._set_product_variant_field("best_before_date_day"),
        readonly=False,
    )

    storage_method = fields.Selection(
        compute=lambda x: x._compute_template_field_from_variant_field(
            "storage_method"
        ),
        inverse=lambda x: x._set_product_variant_field("storage_method"),
        readonly=False,
        selection=lambda self: self.env["product.product"]
        ._fields["storage_method"]
        .selection,
    )

    ingredients = fields.Text(
        compute=lambda x: x._compute_template_field_from_variant_field("ingredients"),
        inverse=lambda x: x._set_product_variant_field("ingredients"),
        readonly=False,
    )

    allergen_ids = fields.Many2many(
        comodel_name="product.allergen",
        compute=lambda x: x._compute_template_field_from_variant_field("allergen_ids"),
        inverse=lambda x: x._set_product_variant_field("allergen_ids"),
        readonly=False,
    )

    trace_allergen_ids = fields.Many2many(
        string="Allergens (Traces)",
        comodel_name="product.allergen",
        compute=lambda x: x._compute_template_field_from_variant_field(
            "trace_allergen_ids"
        ),
        inverse=lambda x: x._set_product_variant_field("trace_allergen_ids"),
        readonly=False,
    )

    def _get_related_fields_variant_template(self):
        res = super()._get_related_fields_variant_template()
        res += [
            "is_alimentary",
            "alcohol_by_volume",
            "has_alcohol",
            "use_by_date_day",
            "best_before_date_day",
            "storage_method",
            "ingredients",
            "allergen_ids",
            "trace_allergen_ids",
        ]
        return res

    # Onchange Section
    @api.onchange("categ_id")
    def onchange_categ_id_product_food(self):
        ProductProduct.onchange_categ_id_product_food(self)

    @api.onchange("label_ids")
    def onchange_label_ids_product_food(self):
        ProductProduct.onchange_label_ids_product_food(self)
