# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError


class ProductProduct(models.Model):
    _inherit = "product.product"

    # Constant Section
    _ORIGIN_TYPE_SELECTION = [
        ("eu", "EU"),
        ("no_eu", "No EU"),
        ("eu_no_eu", "EU / No EU"),
    ]

    _ORGANIC_TYPE_SELECTION = [
        ("01_organic", "Organic"),
        ("02_agroecological", "Agroecological"),
        ("03_uncertifiable", "Aliment Uncertifiable"),
        ("04_uncertified", "Aliment Not Certified"),
        ("05_not_alimentary", "Not Alimentary"),
    ]

    # Column Section
    is_alimentary = fields.Boolean(string="Is Alimentary")

    is_vegan = fields.Boolean(string="Vegan product")

    certifier_organization_id = fields.Many2one(
        comodel_name="certifier.organization",
        string="Certifier Organization",
    )

    is_uncertifiable = fields.Boolean(
        string="Not Certifiable",
        help="Check this box for alimentary products that are"
        " uncertifiable by definition. For exemple: Products"
        " that comes from the sea",
    )

    is_alcohol = fields.Boolean(string="Contain Alcohol")

    best_before_date_day = fields.Integer(string="Best Before Date Day")

    ingredients = fields.Text(string="Ingredients")

    allergen_ids = fields.Many2many(
        comodel_name="product.allergen",
        relation="product_allergen_product_rel",
        column1="product_id",
        column2="allergen_id",
        string="Allergens",
    )

    allergens = fields.Text(string="Allergens Complement")

    organic_type = fields.Selection(
        selection=_ORGANIC_TYPE_SELECTION,
        string="Organic Category",
        compute="_compute_organic_type",
    )

    origin_type = fields.Selection(
        selection=_ORIGIN_TYPE_SELECTION,
        string="Origin Type",
    )

    price_per_unit = fields.Float(
        compute="_compute_price_per_unit", string="Unit Price"
    )

    # Compute Section
    @api.depends("label_ids.organic_type", "is_alimentary", "is_uncertifiable")
    def _compute_organic_type(self):
        for product in self:
            types = product.mapped("label_ids.organic_type")
            if "01_organic" in types:
                product.organic_type = "01_organic"
            elif "02_agroecological" in types:
                product.organic_type = "02_agroecological"
            elif product.is_alimentary:
                if product.is_uncertifiable:
                    product.organic_type = "03_uncertifiable"
                else:
                    product.organic_type = "04_uncertified"
            else:
                product.organic_type = "05_not_alimentary"

    @api.depends("weight", "volume", "list_price")
    def _compute_price_per_unit(self):
        for product in self:
            if product.weight != 0 and product.volume != 0:
                product.price_per_unit = 0
            elif product.weight not in [0, 1]:
                product.price_per_unit = product.list_price / product.weight
            elif product.volume not in [0, 1]:
                product.price_per_unit = product.list_price / product.volume
            else:
                product.price_per_unit = 0

    # Constrains Section
    @api.multi
    @api.constrains("weight", "volume")
    def _check_weight_volume(self):
        for product in self:
            if product.weight and product.volume:
                raise UserError(
                    _(
                        "Incorrect Setting. "
                        "The product %s could not have"
                        " volume AND weight at the same time."
                    )
                    % (product.name)
                )

    @api.multi
    @api.constrains("is_alcohol", "label_ids")
    def _check_alcohol_labels(self):
        ProductLabel = self.env["product.label"]
        for product in self:
            if product.is_alcohol:
                # Check that all the alcohol labels are set
                alcohol_label_ids = ProductLabel.search([("is_alcohol", "=", True)]).ids
                if [x for x in alcohol_label_ids if x not in product.label_ids.ids]:
                    raise UserError(
                        _(
                            "Incorrect Setting. the product %s is checked as"
                            " 'Contain Alcohol' but some related labels are"
                            " not set."
                        )
                        % (product.name)
                    )
            if product.label_ids.filtered(lambda x: x.is_alcohol):
                # Check that 'contain Alcohol' is checked
                if not product.is_alcohol:
                    raise UserError(
                        _(
                            "Incorrect Setting. the product %s has a label"
                            " that mentions that the product contains "
                            " alcohol, but the 'Contain Alcohol' is not"
                            " checked."
                        )
                        % (product.name)
                    )

    @api.multi
    @api.constrains("is_vegan", "label_ids")
    def _check_is_vegan_labels(self):
        for product in self:
            if product.label_ids.filtered(lambda x: x.is_vegan):
                # Check that 'Vegan product' is checked
                if not product.is_vegan:
                    raise UserError(
                        _(
                            "Incorrect Setting. the product %s has a label"
                            " that mentions that the product is vegan"
                            " but the 'Vegan product' is not"
                            " checked."
                        )
                        % (product.name)
                    )

    # Onchange Section
    @api.onchange("categ_id")
    def onchange_categ_id_is_alimentary(self):
        if self.categ_id:
            self.is_alimentary = self.categ_id.is_alimentary
            self.is_alcohol = self.categ_id.is_alcohol

    @api.onchange("is_alimentary")
    def onchange_is_alimentary(self):
        if not self.is_alimentary:
            self.is_alcohol = False

    @api.onchange("label_ids", "categ_id")
    def onchange_label_ids(self):
        labels_vegan = self.label_ids.filtered(lambda x: x.is_vegan)
        if len(labels_vegan) > 0:
            self.is_vegan = True
        else:
            self.is_vegan = self.categ_id.is_vegan

    @api.onchange("is_alcohol")
    def onchange_is_alcohol(self):
        ProductLabel = self.env["product.label"]
        if self.is_alcohol:
            self.is_alimentary = True
            alcohol_label_ids = ProductLabel.search([("is_alcohol", "=", True)]).ids
            for alcohol_label_id in alcohol_label_ids:
                self.label_ids = [(4, alcohol_label_id)]
        else:
            self.label_ids = self.label_ids.filtered(lambda x: not x.is_alcohol)

    @api.model
    def create(self, vals):
        if "categ_id" in vals:
            # Guess values if not present, based on the category
            categ = self.env["product.category"].browse(vals.get("categ_id"))
            if "is_alimentary" not in vals:
                vals["is_alimentary"] = categ.is_alimentary
            if "is_alcohol" not in vals:
                vals["is_alcohol"] = categ.is_alcohol
            if "is_vegan" not in vals:
                vals["is_vegan"] = categ.is_vegan
        return super().create(vals)
