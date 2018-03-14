# coding: utf-8
# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError


class ProductCategory(models.Model):
    _inherit = 'product.category'

    is_food = fields.Boolean(
        string='Contain Food Products', help="If this box is checked, the"
        " products that belong to that category will be set as 'Food Product'"
        " by default")

    is_alcohol = fields.Boolean(
        string='Contain Alcohol', help="If this box is checked, the"
        " products that belong to that category will be set as"
        " 'Contain alcohol' by default")

    @api.multi
    @api.constrains('is_food', 'is_alcohol')
    def _contrains_food_alcohol(self):
        for category in self:
            if category.is_alcohol and not category.is_food:
                raise UserError(_(
                    "'Contain Food Products' should be checked for"
                    " categories set as 'Contain Alcohol'"))
