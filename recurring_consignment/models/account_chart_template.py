# Copyright (C) 2026 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import fields, models


class AccountChartTemplate(models.Model):
    _inherit = "account.chart.template"

    recurring_consignment_account_prefix = fields.Char(
        help="Code used as prefix to generate account code of the consignors."
    )

    def _load_template(
        self, company, code_digits=None, account_ref=None, taxes_ref=None
    ):
        res = super()._load_template(
            company, code_digits=None, account_ref=None, taxes_ref=None
        )
        company.recurring_consignment_account_prefix = (
            self.recurring_consignment_account_prefix
        )
        return res
