# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models



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

    @api.depends("pricetag_type_id.color")
    def _compute_pricetag_color(self):
        for product in self.filtered(lambda x: x.pricetag_type_id):
            product.pricetag_color = product.pricetag_type_id.color

    pricetag_print_date_text = fields.Char(compute="_compute_pricetag_print_date_text")

    def _compute_pricetag_print_date_text(self):
        for product in self:
            product.pricetag_print_date_text = _("Modified on %s") % (
                product.write_date.strftime("%d/%m/%y - %H:%M")
            )

    pricetag_organic_text = fields.Char(compute="_compute_pricetag_organic_text")

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
            if not product.is_alimentary:
                continue

            if product.ingredient_origin_type:
                if product.ingredient_origin_type == "fr":
                    origin = _("France")
                elif product.ingredient_origin_type == "eu":
                    origin = _("EU")
                elif product.ingredient_origin_type == "no_eu":
                    origin = _("No EU")
                else:
                    origin = _("EU / No EU")
                res += _("Origin of Ingredients: %s. ") % (origin)

            # We need organic text only in weighed product
            # for companies that are certified
            if (
                product.uom_id.category_id.measure_type == "weight"
                and product.company_id.certifier_organization_id
            ):
                if product.organic_type in ["01_organic"]:
                    res += _("Organic Product, certified by %s. ") % (
                        product.company_id.certifier_organization_id.code
                    )
                else:
                    res += _("Not From Organic Farming. ")

            product.pricetag_organic_text = res

    pricetag_origin = fields.Char(
        string="Origin on pricetag", compute="_compute_pricetag_origin"
    )

    @api.depends("state_id", "country_id", "department_id")
    def _compute_pricetag_origin(self):
        for product in self:
            if product.department_id:
                product.pricetag_origin = (
                    f"{product.department_id.name} ({product.department_id.code})"
                )
            elif product.state_id:
                product.pricetag_origin = product.state_id.name

            elif product.country_id:
                product.pricetag_origin = product.country_id.name
            else:
                product.pricetag_origin = False

    pricetag_main_price_value = fields.Float(
        compute="_compute_pricetag_main_price_info",
        digits="Product Price",
    )

    pricetag_main_uom_text = fields.Char(
        compute="_compute_pricetag_main_price_info",
    )

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
        digits="Product Price",
    )

    pricetag_secondary_uom_text = fields.Char(
        compute="_compute_pricetag_secondary_price_info",
    )

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

    pricetag_per_unit_quantity_value = fields.Char(
        compute="_compute_pricetag_per_unit_quantity_text"
    )

    pricetag_per_unit_quantity_text = fields.Char(
        compute="_compute_pricetag_per_unit_quantity_text"
    )

    @api.depends("net_weight", "volume")
    def _compute_pricetag_per_unit_quantity_text(self):
        for product in self:
            if product.net_weight > 0:
                product.pricetag_per_unit_quantity_text = _("Net Weight")
                if product.net_weight >= 1:
                    product.pricetag_per_unit_quantity_value = (
                        _("%.3f kg") % product.net_weight
                    )
                else:
                    product.pricetag_per_unit_quantity_value = _("%.0f gr") % (
                        product.net_weight * 1000
                    )
            elif product.volume > 0:
                product.pricetag_per_unit_quantity_text = _("Net Volume")
                if product.volume > 1:
                    product.pricetag_per_unit_quantity_value = (
                        _("%.2f L") % product.volume
                    )
                else:
                    product.pricetag_per_unit_quantity_value = _("%.0f mL") % (
                        product.volume * 1000
                    )
            else:
                product.pricetag_per_unit_quantity_text = ""
