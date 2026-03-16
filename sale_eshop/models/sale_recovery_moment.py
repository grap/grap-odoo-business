# Copyright (C) 2026 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class SaleRecoveryMoment(models.Model):
    _name = "sale.recovery.moment"
    _inherit = ["sale.recovery.moment", "eshop.mixin"]

    # Inherit Section
    _eshop_fields = [
        "description",
        "is_complete",
        "min_recovery_date",
        "max_recovery_date",
        "place_id",
    ]
