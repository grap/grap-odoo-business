# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    ingredient_origin_type = fields.Selection(
        string="Origin of Ingredients",
        selection=lambda self: self.env["product.product"]
        ._fields["ingredient_origin_type"]
        .selection,
        related="product_variant_ids.ingredient_origin_type",
        readonly=False,
        help="The place of production of the agricultural"
        " raw materials making up the product."
        " This information is mandatory if the 'Euro leaf' logo is used.\n\n"
        " More information :"
        " https://www.inao.gouv.fr/Les-signes-officiels-de-la-qualite-et-de-l-origine-SIQO/Agriculture-biologique#logosab",  # noqa: B950
    )
