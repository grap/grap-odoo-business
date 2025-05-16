# Copyright (C) 2025 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ResPartnerBank(models.Model):
    _name = "res.partner.bank"
    _inherit = ["res.partner.bank", "eshop.mixin"]

    # Inherit Section
    _eshop_invalidation_type = "single"

    _eshop_fields = [
        "acc_number",
        "bank_id",
        "partner_id",
    ]
