# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class UomUom(models.Model):
    _name = "uom.uom"
    _inherit = ["uom.uom", "eshop.mixin"]

    # Inherit Section
    _eshop_invalidation_type = "multiple"

    _eshop_fields = ["id", "name", "eshop_description"]

    # Fields Section
    eshop_description = fields.Char(
        string="Description for the eShop", default="/"
    )

    # Overwrite section
    @api.model
    def _get_eshop_domain(self):
        return [("eshop_description", "!=", False)]
