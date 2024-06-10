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
