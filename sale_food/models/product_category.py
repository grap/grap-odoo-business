# coding: utf-8
# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class ProductCategory(models.Model):
    _inherit = 'product.category'

    is_food = fields.Boolean(
        string='Contain Food Products', help="If this box is checked, the"
        " products that belong to that category will be set as 'Food Product'"
        " by default")
