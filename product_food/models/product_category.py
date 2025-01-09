# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = "product.category"

    is_alimentary = fields.Boolean(
        string="Contain Alimentary Products",
        help="If this box is checked, the"
        " products that belong to that category will be set as "
        "'Alimentary Product' by default",
    )

    is_vegan = fields.Boolean(
        string="Contain Vegan Products",
        help="If this box is checked, the"
        " products that belong to that category will be set as "
        "'Vegan product' by default",
    )

    has_alcohol = fields.Boolean(
        string="Contain Alcohol Products",
        help="If this box is checked, the"
        " products that belong to that category will be set as"
        " 'Contain alcohol' by default",
    )
