# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    pricetag_color = fields.Char(
        string="Pricetag Color",
        required=True,
        size=7,
        default="#FFFFFF",
        help="Color of the Pricetag by default. Format #RRGGBB",
    )
