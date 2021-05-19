# Copyright (C) 2021 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT (quentin.dupont@grap.coop)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResCountryGroup(models.Model):
    _inherit = "res.country.group"

    # Constant Section
    _EUROPEAN_CLASSIFICATION = [
        ("default", "Unknown"),
        ("UE", "European"),
        ("no_UE", "Not European"),
        ("UE_noUE", "European / Not European"),
    ]

    # Column Section
    european_classification = fields.Selection(
        selection=_EUROPEAN_CLASSIFICATION,
        string="European classification",
        required=True,
        default="default",
    )
