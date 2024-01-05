# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    _INGREDIENT_ORIGIN_TYPE_SELECTION = [
        ("fr", "France"),
        ("eu", "EU"),
        ("no_eu", "No EU"),
        ("eu_no_eu", "EU / No EU"),
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
