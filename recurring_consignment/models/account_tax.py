# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import fields, models


class AccountTax(models.Model):
    _inherit = "account.tax"

    # Columns Section
    consignor_partner_id = fields.Many2one(
        string="Consignor",
        comodel_name="res.partner",
        domain="[('is_consignor', '=', True)]",
    )
