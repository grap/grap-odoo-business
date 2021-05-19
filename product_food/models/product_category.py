# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError


class ProductCategory(models.Model):
    _inherit = "product.category"

    is_alimentary = fields.Boolean(
        string="Contain Alimentary Products",
        help="If this box is checked, the"
        " products that belong to that category will be set as "
        "'Alimentary Product' by default",
    )

    is_vegan = fields.Boolean(
        string="Contain only vegan products",
        help="If this box is checked, the"
        " products that belong to that category will be set as "
        "'Vegan product' by default",
    )

    is_alcohol = fields.Boolean(
        string="Contain Alcohol Products",
        help="If this box is checked, the"
        " products that belong to that category will be set as"
        " 'Contain alcohol' by default",
    )

    @api.multi
    @api.constrains("is_alimentary", "is_alcohol")
    def _contrains_alimentary_alcohol(self):
        for category in self:
            if category.is_alcohol and not category.is_alimentary:
                raise UserError(
                    _(
                        "'Is Alimentary' should be checked for"
                        " categories set as 'Contain Alcohol'"
                    )
                )

    def button_apply_is_alimentary_settings(self):
        ProductTemplate = self.env["product.template"]
        for category in self:
            templates = (
                ProductTemplate.sudo()
                .with_context(active_test=False)
                .search([("categ_id", "=", category.id)])
            )
            templates.write({"is_alimentary": category.is_alimentary})
