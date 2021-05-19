# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductLabel(models.Model):
    _inherit = "product.label"

    _ORGANIC_TYPE_SELECTION = [
        ("01_organic", "Organic"),
        ("02_agroecological", "Agroecological"),
    ]

    organic_type = fields.Selection(
        selection=_ORGANIC_TYPE_SELECTION, string="Organic Category"
    )

    is_alcohol = fields.Boolean(
        string="Is Alcohol",
        help="Check this box if this label is a label that mentions that"
        " products contain alcohol. If checked, the products that"
        " contains alcohol will have this label set automatically.",
    )

    is_vegan = fields.Boolean(
        string="Vegan products",
        help="If this box is checked, the"
        " products that have this label will be set as "
        "'Vegan product' by default",
    )
