# Copyright (C) 2021 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class ResCountryState(models.Model):
    _name = "res.country.state"
    _inherit = ["res.country.state", "eshop.mixin"]

    # Inherit Section
    _eshop_invalidation_type = "multiple"

    _eshop_fields = ["name"]
