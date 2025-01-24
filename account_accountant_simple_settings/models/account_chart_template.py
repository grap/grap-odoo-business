# Copyright (C) 2025 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models


class AccountChartTemplate(models.Model):
    _inherit = "account.chart.template"

    def _load(self, company):
        # Allow accountant to install chart templates
        if not self.env.is_admin() and self.env.user.has_group(
            "account.group_account_manager"
        ):
            return super(AccountChartTemplate, self.sudo())._load(company)
        else:
            return super()._load(company)
