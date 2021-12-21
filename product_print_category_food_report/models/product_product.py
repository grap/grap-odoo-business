# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models

import odoo.addons.decimal_precision as dp


class ProductProduct(models.Model):
    _inherit = "product.product"

    pricetag_type_id = fields.Many2one(
        comodel_name="product.pricetag.type", string="Pricetag Type"
    )

    pricetag_color = fields.Char(compute="_compute_pricetag_color")

    pricetag_organic_text = fields.Char(compute="_compute_pricetag_organic_text")

    pricetag_display_spider_chart = fields.Boolean(
        compute="_compute_pricetag_display_spider_chart"
    )

    pricetag_origin = fields.Char(
        string="Origin on pricetag", compute="_compute_pricetag_origin"
    )

    pricetag_special_quantity_price = fields.Boolean(
        default=False,
        compute="_compute_pricetag_second_price",
        multi="pricetag_second_price",
    )

    pricetag_is_second_price = fields.Boolean(
        compute="_compute_pricetag_second_price", multi="pricetag_second_price"
    )

    pricetag_second_price = fields.Float(
        compute="_compute_pricetag_second_price",
        digits=dp.get_precision("Product Price"),
        multi="pricetag_second_price",
    )

    pricetag_second_price_uom_text = fields.Char(
        compute="_compute_pricetag_second_price", multi="pricetag_second_price"
    )

    pricetag_uom_id = fields.Many2one(
        comodel_name="uom.uom",
        string="Pricetag UoM",
        domain="[('pricetag_available', '=', True)]",
        help="Set an alternative Unit of Mesure if you want to display"
        " the price on your pricetags relative to this Unit.",
    )

    # Compute Section
    @api.multi
    def _compute_pricetag_color(self):
        for product in self:
            if product.pricetag_type_id:
                product.pricetag_color = product.pricetag_type_id.color
            else:
                product.pricetag_color = product.company_id.pricetag_color

    @api.multi
    def _compute_pricetag_organic_text(self):
        for product in self:
            res = ""
            # We need organic text only in weighed product
            if (
                product.uom_id.category_id.measure_type == "weight"
                and product.is_alimentary is True
            ):
                if product.organic_type in ["01_organic"]:
                    if product.company_id.certifier_organization_id:
                        res = _("Organic Product, certified by %s") % (
                            product.company_id.certifier_organization_id.code
                        )
                else:
                    res = _("Not From Organic Farming")
            product.pricetag_organic_text = res

    @api.multi
    def _compute_pricetag_display_spider_chart(self):
        for product in self:
            notation = [
                product.social_notation,
                product.organic_notation,
                product.packaging_notation,
                product.local_notation,
            ]
            result = [x for x in notation if x != "0"]
            product.pricetag_display_spider_chart = len(result) >= 3

    @api.depends(
        "origin_description", "state_id", "country_id", "country_group_id", "label_ids"
    )
    @api.multi
    def _compute_pricetag_origin(self):
        for product in self:
            localization_info = ""
            if product.department_id:
                localization_info = "{} ({})".format(
                    product.department_id.name,
                    product.department_id.code,
                )
            elif product.state_id:
                localization_info = product.state_id.name
            elif product.country_id:
                localization_info = product.country_id.name

            if product.origin_description:
                if localization_info:
                    product.pricetag_origin = "{} - {}".format(
                        localization_info,
                        product.origin_description,
                    )
                else:
                    product.pricetag_origin = product.origin_description
            else:
                product.pricetag_origin = localization_info
            eu_add = ""
            if product.organic_type in ["01_organic"]:
                eu_classification = product.country_group_id.european_classification
                if eu_classification == "UE":
                    eu_add = _("(UE) ")
                elif eu_classification == "no_UE":
                    eu_add = _("(no UE) ")
                elif eu_classification == "UE_noUE":
                    eu_add = _("(UE / no UE) ")
            product.pricetag_origin = eu_add + product.pricetag_origin

    @api.multi
    def _compute_pricetag_second_price(self):
        for product in self.filtered(lambda x: x.list_price):
            if product.pricetag_uom_id:
                product.pricetag_is_second_price = True
                product.pricetag_special_quantity_price = True
                product.pricetag_second_price_uom_text = (
                    _("For %s") % product.pricetag_uom_id.name
                )
                product.pricetag_second_price = (
                    product.list_price / product.pricetag_uom_id.factor
                )
            elif product.volume:
                product.pricetag_is_second_price = True
                product.pricetag_second_price_uom_text = _("Price per Liter")
                product.pricetag_second_price = product.list_price / product.volume
            elif product.net_weight:
                product.pricetag_is_second_price = True
                product.pricetag_second_price_uom_text = _("Price per Kilo")
                product.pricetag_second_price = product.list_price / product.net_weight
