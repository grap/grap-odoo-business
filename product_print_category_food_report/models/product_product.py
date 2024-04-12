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

    pricetag_uom_id = fields.Many2one(
        comodel_name="uom.uom",
        string="Pricetag UoM",
        domain="[('pricetag_available', '=', True)]",
        help="Set an alternative Unit of Mesure if you want to display"
        " the price on your pricetags relative to this Unit.",
    )

    allergen_text = fields.Char(compute="_compute_allergen_text")

    trace_allergen_text = fields.Char(compute="_compute_trace_allergen_text")

    @api.depends("allergen_ids.name")
    def _compute_allergen_text(self):
        for product in self:
            product.allergen_text = ", ".join(product.mapped("allergen_ids.name"))

    @api.depends("trace_allergen_ids.name")
    def _compute_trace_allergen_text(self):
        for product in self:
            product.trace_allergen_text = ", ".join(
                product.mapped("trace_allergen_ids.name")
            )

    pricetag_color = fields.Char(compute="_compute_pricetag_color")

    @api.multi
    @api.depends("pricetag_type_id.color", "company_id.pricetag_color")
    def _compute_pricetag_color(self):
        for product in self:
            if product.pricetag_type_id:
                product.pricetag_color = product.pricetag_type_id.color
            else:
                product.pricetag_color = product.company_id.pricetag_color

    pricetag_print_date_text = fields.Char(compute="_compute_pricetag_print_date_text")

    @api.multi
    def _compute_pricetag_print_date_text(self):
        for product in self:
            product.pricetag_print_date_text = ("Modified on %s") % (
                product.write_date.strftime("%d/%m/%y - %H:%M")
            )

    pricetag_organic_text = fields.Char(compute="_compute_pricetag_organic_text")

    @api.multi
    @api.depends(
        "uom_id.category_id.measure_type",
        "is_alimentary",
        "organic_type",
        "company_id.certifier_organization_id",
        "company_id.certifier_organization_id.code",
    )
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

    pricetag_origin = fields.Char(
        string="Origin on pricetag", compute="_compute_pricetag_origin"
    )

    @api.depends("state_id", "country_id", "department_id", "origin_description")
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

    pricetag_main_price_value = fields.Float(
        compute="_compute_pricetag_main_price_info",
        digits=dp.get_precision("Product Price"),
    )

    pricetag_main_uom_text = fields.Char(
        compute="_compute_pricetag_main_price_info",
    )

    @api.multi
    @api.depends(
        "pricetag_uom_id.pricetag_name",
        "pricetag_uom_id.name",
        "pricetag_uom_id.factor",
        "list_price",
        "uom_id.name",
    )
    def _compute_pricetag_main_price_info(self):
        for product in self:
            if product.pricetag_uom_id:
                uom_name = (
                    product.pricetag_uom_id.pricetag_name
                    or product.pricetag_uom_id.name
                )
                main_price = product.list_price / product.pricetag_uom_id.factor
                main_uom_text = _("for %s") % (uom_name)
            else:
                main_price = product.list_price
                if product.uom_id == self.env.ref("uom.product_uom_unit"):
                    main_uom_text = ""
                elif product.uom_id == self.env.ref("uom.product_uom_kgm"):
                    main_uom_text = _(" per kilo")
                else:
                    main_uom_text = f" / {product.uom_id.name}"

            product.pricetag_main_price_value = main_price
            product.pricetag_main_uom_text = main_uom_text

    pricetag_secondary_price_value = fields.Float(
        compute="_compute_pricetag_secondary_price_info",
        digits=dp.get_precision("Product Price"),
    )

    pricetag_secondary_uom_text = fields.Char(
        compute="_compute_pricetag_secondary_price_info",
    )

    @api.multi
    @api.depends("list_price", "pricetag_uom_id", "uom_id.name", "net_weight", "volume")
    def _compute_pricetag_secondary_price_info(self):
        for product in self:
            price = 0.0
            uom_text = ""

            if product.list_price:
                if product.pricetag_uom_id:
                    price = product.list_price
                    if product.uom_id == self.env.ref("uom.product_uom_unit"):
                        uom_text = _(" per piece")
                    elif product.uom_id == self.env.ref("uom.product_uom_kgm"):
                        uom_text = _(" per kilo")
                    else:
                        uom_text = f" / {product.uom_id.name}"

                elif product.net_weight not in [0, 1]:
                    price = product.list_price / product.net_weight
                    uom_text = _(" per kilo")

                elif product.volume not in [0, 1]:
                    price = product.list_price / product.volume
                    uom_text = _(" per liter")

            product.pricetag_secondary_price_value = price
            product.pricetag_secondary_uom_text = uom_text

    pricetag_per_unit_quantity_text = fields.Char(
        compute="_compute_pricetag_per_unit_quantity_text"
    )

    @api.depends("net_weight", "volume")
    def _compute_pricetag_per_unit_quantity_text(self):
        for product in self:
            if product.net_weight > 1:
                product.pricetag_per_unit_quantity_text = (
                    _("Net Weight: %.3f kg") % product.net_weight
                )
            elif product.net_weight > 0:
                product.pricetag_per_unit_quantity_text = _("Net Weight: %.0f gr") % (
                    product.net_weight * 1000
                )
            elif product.volume > 1:
                product.pricetag_per_unit_quantity_text = (
                    _("Net Volume: %.3f L") % product.volume
                )
            elif product.volume > 0:
                product.pricetag_per_unit_quantity_text = _("Net Volume: %.0f mL") % (
                    product.volume * 1000
                )
            else:
                product.pricetag_per_unit_quantity_text = ""

    # TODO, REMOVE AFTER THAT LINES
    # TODO, REMOVE AFTER THAT LINES
    # TODO, REMOVE AFTER THAT LINES
    # TODO, REMOVE AFTER THAT LINES
    # TODO, REMOVE AFTER THAT LINES
    pricetag_special_quantity_price = fields.Boolean(
        default=False,
        compute="_compute_pricetag_second_price",
    )

    pricetag_is_second_price = fields.Boolean(
        compute="_compute_pricetag_second_price", multi="pricetag_second_price"
    )

    pricetag_second_price = fields.Float(
        compute="_compute_pricetag_second_price",
        digits=dp.get_precision("Product Price"),
    )

    pricetag_second_price_uom_text = fields.Char(
        compute="_compute_pricetag_second_price", multi="pricetag_second_price"
    )

    pricetag_price_per_unit_value = fields.Float(
        compute="_compute_pricetag_price_per_unit",
        digits=dp.get_precision("Product Price"),
    )

    pricetag_price_per_unit_text = fields.Char(
        compute="_compute_pricetag_price_per_unit",
    )

    # Compute Section
    @api.depends("net_weight", "volume", "list_price")
    def _compute_pricetag_price_per_unit(self):
        for product in self:
            if product.net_weight not in [0, 1]:
                product.pricetag_price_per_unit_value = (
                    product.list_price / product.net_weight
                )
                product.pricetag_price_per_unit_text = _("Price per kilo")
            elif product.volume not in [0, 1]:
                product.pricetag_price_per_unit_value = (
                    product.list_price / product.volume
                )
                product.pricetag_price_per_unit_text = _("Price per liter")
            else:
                product.pricetag_price_per_unit_value = 0
                product.pricetag_price_per_unit_text = ""

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
