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

    certifier_organization_id = fields.Many2one(
        comodel_name="certifier.organization",
        string="Certifier Organization",
        related="product_variant_ids.certifier_organization_id",
        readonly=False,
    )

    is_uncertifiable = fields.Boolean(
        string="Not Certifiable",
        related="product_variant_ids.is_uncertifiable",
        readonly=False,
        help="Check this box for alimentary products that are"
        " uncertifiable by definition. For exemple: Products"
        " that comes from the sea",
    )

    is_alcohol = fields.Boolean(
        string="Contain Alcohol",
        related="product_variant_ids.is_alcohol",
        readonly=False,
    )

    best_before_date_day = fields.Integer(
        string="Best Before Date Day",
        related="product_variant_ids.best_before_date_day",
        readonly=False,
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

    allergens = fields.Text(
        string="Allergens Complement",
        related="product_variant_ids.allergens",
        readonly=False,
    )

    organic_type = fields.Selection(
        selection=lambda self: self.env["product.product"]
        ._fields["organic_type"]
        .selection,
        string="Organic Category",
        compute="_compute_organic_type",
    )

    origin_type = fields.Selection(
        selection=lambda self: self.env["product.product"]
        ._fields["origin_type"]
        .selection,
        string="Origin Type",
        related="product_variant_ids.origin_type",
        readonly=False,
    )

    price_per_unit = fields.Float(
        string="Unit Price",
        compute="_compute_price_per_unit",
    )

    # Compute Section
    @api.depends("label_ids.organic_type", "is_alimentary", "is_uncertifiable")
    def _compute_organic_type(self):
        ProductProduct._compute_organic_type(self)

    @api.depends("weight", "volume", "list_price")
    def _compute_price_per_unit(self):
        ProductProduct._compute_price_per_unit(self)

    # Onchange Section
    @api.onchange("categ_id")
    def onchange_categ_id_is_alimentary(self):
        ProductProduct.onchange_categ_id_is_alimentary(self)

    @api.onchange("is_alimentary")
    def onchange_is_alimentary(self):
        ProductProduct.onchange_is_alimentary(self)

    @api.onchange("is_alcohol")
    def onchange_is_alcohol(self):
        ProductProduct.onchange_is_alcohol(self)
