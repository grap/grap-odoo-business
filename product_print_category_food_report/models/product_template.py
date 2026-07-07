# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    pricetag_type_id = fields.Many2one(
        string="Pricetag Type",
        comodel_name="product.pricetag.type",
        compute="_compute_pricetag_type_id",
        inverse="_inverse_pricetag_type_id",
    )

    pricetag_uom_id = fields.Many2one(
        string="Pricetag UoM",
        comodel_name="uom.uom",
        domain="[('pricetag_available', '=', True)]",
        compute="_compute_pricetag_uom_id",
        inverse="_inverse_pricetag_uom_id",
        help="Set an alternative Unit of Mesure if you want to display"
        " the price on your pricetags relative to this Unit.",
    )

    def _get_related_fields_variant_template(self):
        res = super()._get_related_fields_variant_template()
        res += ["pricetag_type_id", "pricetag_uom_id"]
        return res

    @api.depends("product_variant_ids", "product_variant_ids.pricetag_type_id")
    def _compute_pricetag_type_id(self):
        unique_variants = self.filtered(
            lambda template: len(template.product_variant_ids) == 1
        )
        for template in unique_variants:
            template.pricetag_type_id = template.product_variant_ids.pricetag_type_id
        for template in self - unique_variants:
            template.pricetag_type_id = False

    def _inverse_pricetag_type_id(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.pricetag_type_id = (
                    template.pricetag_type_id
                )

    @api.depends("product_variant_ids", "product_variant_ids.pricetag_uom_id")
    def _compute_pricetag_uom_id(self):
        unique_variants = self.filtered(
            lambda template: len(template.product_variant_ids) == 1
        )
        for template in unique_variants:
            template.pricetag_uom_id = template.product_variant_ids.pricetag_uom_id
        for template in self - unique_variants:
            template.pricetag_uom_id = False

    def _inverse_pricetag_uom_id(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.pricetag_uom_id = template.pricetag_uom_id
