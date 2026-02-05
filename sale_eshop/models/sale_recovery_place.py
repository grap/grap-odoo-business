# Copyright (C) 2026 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class SaleRecoveryPlace(models.Model):
    _name = "sale.recovery.place"
    _inherit = ["sale.recovery.place", "eshop.mixin"]

    # Inherit Section
    _eshop_fields = [
        "name",
        "complete_name",
        "shipping_product_id",
    ]
