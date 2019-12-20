# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError


class ProductProduct(models.Model):
    _inherit = "product.product"

    # Constant Section
    _ORGANIC_TYPE_SELECTION = [
        ('01_organic', "Organic"),
        ('02_agroecological', "Agroecological"),
        ('03_uncertifiable', "Aliment Uncertifiable"),
        ('04_uncertified', "Aliment Not Certified"),
        ('05_not_alimentary', "Not Alimentary"),
    ]

    # Column Section
    is_alimentary = fields.Boolean(
        string="Is Alimentary")

    is_uncertifiable = fields.Boolean(
        string="Not Certifiable",
        help="Check this for alimentary products that are"
        " uncertifiable by definition. For exemple: Products"
        " that comes from the see")

    is_alcohol = fields.Boolean(string="Contain Alcohol")

    expiration_date_day = fields.Integer(
        string="Day quantity Before Expiration Date"
    )

    ingredients = fields.Text(string="Ingredients")

    allergens = fields.Text(string="Allergens")

    organic_type = fields.Selection(
        selection=_ORGANIC_TYPE_SELECTION, string="Organic Category",
        compute="_compute_organic_type"
    )

    # Compute Section
    @api.depends(
        "label_ids.organic_type", "is_alimentary", "is_uncertifiable")
    def _compute_organic_type(self):
        for product in self:
            types = product.mapped('label_ids.organic_type')
            if '01_organic' in types:
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

    # Constrains Section
    @api.multi
    @api.constrains("is_alcohol", "label_ids")
    def _check_alcohol_labels(self):
        label_obj = self.env["product.label"]
        for product in self:
            if product.is_alcohol:
                # Check that all the alcohol labels are set
                alcohol_label_ids = label_obj.search(
                    [("is_alcohol", "=", True)]
                ).ids
                if [
                    x
                    for x in alcohol_label_ids
                    if x not in product.label_ids.ids
                ]:
                    raise UserError(
                        _(
                            "Incorrect Setting. the product %s is checked as"
                            " 'Contain Alcohol' but some related labels are not"
                            " set."
                        )
                        % (product.name)
                    )
            if product.label_ids.filtered(lambda x: x.is_alcohol):
                # Check that 'contain Alcohol' is checked
                if not product.is_alcohol:
                    raise UserError(
                        _(
                            "Incorrect Setting. the product %s has a label"
                            " that mentions that the product contains alcohol, "
                            " but the 'Contain Alcohol' is not checked"
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

    @api.onchange("is_alcohol")
    def onchange_is_alcohol(self):
        label_obj = self.env["product.label"]
        if self.is_alcohol:
            self.is_alimentary = True
            alcohol_label_ids = label_obj.search(
                [("is_alcohol", "=", True)]
            ).ids
            for alcohol_label_id in alcohol_label_ids:
                self.label_ids = [(4, alcohol_label_id)]
        else:
            self.label_ids = self.label_ids.filtered(
                lambda x: not x.is_alcohol
            )
