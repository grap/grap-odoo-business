# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductLabel(models.Model):
    _inherit = "product.label"

    is_vegan = fields.Boolean(
        help="If this box is checked, the"
        " products that have this label will be set as "
        "'Vegan product' by default",
    )
