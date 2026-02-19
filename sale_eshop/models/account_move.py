# Copyright (C) 2026 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class AccountMove(models.Model):
    _name = "account.move"
    _inherit = ["account.move", "eshop.mixin"]

    # Inherit Section
    _eshop_fields = [
        "display_name",
        "invoice_date",
        "amount_untaxed",
        "amount_total",
        "state",
    ]
