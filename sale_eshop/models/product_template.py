# Copyright (C) 2025 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import api, fields, models

from .product_product import ProductProduct


class ProductTemplate(models.Model):
    _inherit = ["product.template"]

    eshop_category_id = fields.Many2one(
        comodel_name="eshop.category",
        compute=lambda x: x._compute_template_field_from_variant_field(
            "eshop_category_id"
        ),
        inverse=lambda x: x._set_product_variant_field("eshop_category_id"),
        readonly=False,
        store=True,
    )

    eshop_start_date = fields.Date(
        compute=lambda x: x._compute_template_field_from_variant_field(
            "eshop_start_date"
        ),
        inverse=lambda x: x._set_product_variant_field("eshop_start_date"),
        readonly=False,
    )

    eshop_end_date = fields.Date(
        compute=lambda x: x._compute_template_field_from_variant_field(
            "eshop_end_date"
        ),
        inverse=lambda x: x._set_product_variant_field("eshop_end_date"),
        readonly=False,
    )

    eshop_state = fields.Selection(
        compute=lambda x: x._compute_template_field_from_variant_field("eshop_state"),
        selection=lambda self: self.env["product.product"]
        ._fields["eshop_state"]
        .selection,
        store=True,
    )

    eshop_minimum_qty = fields.Float(
        compute=lambda x: x._compute_template_field_from_variant_field(
            "eshop_minimum_qty"
        ),
        inverse=lambda x: x._set_product_variant_field("eshop_minimum_qty"),
        readonly=False,
        required=True,
        default=0,
    )

    eshop_rounded_qty = fields.Float(
        compute=lambda x: x._compute_template_field_from_variant_field(
            "eshop_rounded_qty"
        ),
        inverse=lambda x: x._set_product_variant_field("eshop_rounded_qty"),
        readonly=False,
        required=True,
        default=0,
    )

    eshop_description = fields.Html(
        compute=lambda x: x._compute_template_field_from_variant_field(
            "eshop_description"
        ),
        inverse=lambda x: x._set_product_variant_field("eshop_description"),
        readonly=False,
    )

    eshop_taxes_description = fields.Char(
        compute=lambda x: x._compute_template_field_from_variant_field(
            "eshop_taxes_description"
        ),
        inverse=lambda x: x._set_product_variant_field("eshop_taxes_description"),
        readonly=False,
    )

    @api.onchange(
        "eshop_category_id",
        "sale_ok",
        "active",
        "eshop_start_date",
        "eshop_end_date",
    )
    def _onchange_compute_eshop_state(self):
        ProductProduct._get_eshop_state(self)

    def _get_related_fields_variant_template(self):
        res = super()._get_related_fields_variant_template()
        res += [
            "eshop_category_id",
            "eshop_start_date",
            "eshop_end_date",
            "eshop_state",
            "eshop_minimum_qty",
            "eshop_rounded_qty",
            "eshop_description",
            "eshop_taxes_description",
        ]
        return res
