# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    ingredient_origin_type = fields.Selection(
        string="Origin of Ingredients",
        compute=lambda x: x._compute_template_field_from_variant_field(
            "ingredient_origin_type"
        ),
        inverse=lambda x: x._set_product_variant_field("ingredient_origin_type"),
        readonly=False,
        selection=lambda self: self.env["product.product"]
        ._fields["ingredient_origin_type"]
        .selection,
        help="The place of production of the agricultural"
        " raw materials making up the product."
        " This information is mandatory if the 'Euro leaf' logo is used.\n\n"
        " More information :"
        " https://www.inao.gouv.fr/Les-signes-officiels-de-la-qualite-et-de-l-origine-SIQO/Agriculture-biologique#logosab",  # noqa: B950
    )

    is_uncertifiable = fields.Boolean(
        string="Not Certifiable",
        compute=lambda x: x._compute_template_field_from_variant_field(
            "is_uncertifiable"
        ),
        inverse=lambda x: x._set_product_variant_field("is_uncertifiable"),
        readonly=False,
        help="Check this box for alimentary products that are"
        " uncertifiable by definition. For exemple: Products"
        " that comes from the sea",
    )

    organic_type = fields.Selection(
        string="Organic Category",
        # compute="_compute_organic_type",
        compute=lambda x: x._compute_template_field_from_variant_field("organic_type"),
        selection=lambda self: self.env["product.product"]
        ._fields["organic_type"]
        .selection,
    )

    @api.onchange("label_ids", "is_alimentary", "is_uncertifiable")
    def _onchange_to_compute_organic_type(self):
        self.env["product.product"]._get_organic_type(self)

    def _get_related_fields_variant_template(self):
        res = super()._get_related_fields_variant_template()
        res += ["ingredient_origin_type", "is_uncertifiable"]
        return res
