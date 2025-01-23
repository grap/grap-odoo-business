# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    _INGREDIENT_ORIGIN_TYPE_SELECTION = [
        ("fr", "France"),
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

    ingredient_origin_type = fields.Selection(
        string="Origin of Ingredients",
        selection=_INGREDIENT_ORIGIN_TYPE_SELECTION,
        help="The place of production of the agricultural"
        " raw materials making up the product."
        " This information is mandatory if the 'Euro leaf' logo is used.\n\n"
        " More information :"
        " https://www.inao.gouv.fr/Les-signes-officiels-de-la-qualite-et-de-l-origine-SIQO/Agriculture-biologique#logosab",  # noqa: B950
    )

    is_uncertifiable = fields.Boolean(
        string="Not Certifiable",
        help="Check this box for alimentary products that are"
        " uncertifiable by definition. For exemple: Products"
        " that comes from the sea",
    )

    organic_type = fields.Selection(
        selection=_ORGANIC_TYPE_SELECTION,
        string="Organic Category",
        compute="_compute_organic_type",
    )

    # Compute Section
    @api.depends("label_ids.organic_type", "is_alimentary", "is_uncertifiable")
    def _compute_organic_type(self):
        self._get_organic_type(self)

    @api.model
    def _get_organic_type(self, items):
        """
        - called by product.product in compute function
        - called by product.template in onchange function
        """
        for item in items:
            types = item.mapped("label_ids.organic_type")
            if "01_organic" in types:
                item.organic_type = "01_organic"
            elif "02_agroecological" in types:
                item.organic_type = "02_agroecological"
            elif item.is_alimentary:
                if item.is_uncertifiable:
                    item.organic_type = "03_uncertifiable"
                else:
                    item.organic_type = "04_uncertified"
            else:
                item.organic_type = "05_not_alimentary"
