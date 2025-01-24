# Copyright (C) 2025 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields

from odoo.addons.account.models.res_config_settings import ResConfigSettings


class AccountingConfigSettings(ResConfigSettings):
    _name = "account.config.settings"
    _description = "Accounting Settings"

    company_id = fields.Many2one(
        comodel_name="res.company", default=lambda self: self.env.company
    )

    has_accounting_entries = fields.Boolean(compute="_compute_has_chart_of_accounts")

    has_chart_of_accounts = fields.Boolean(compute="_compute_has_chart_of_accounts")

    chart_template_id = fields.Many2one(
        comodel_name="account.chart.template",
        default=lambda self: self.env.company.chart_template_id,
        domain="[('visible','=', True)]",
    )

    period_lock_date = fields.Date(
        related="company_id.period_lock_date",
        readonly=False,
    )
    fiscalyear_lock_date = fields.Date(
        related="company_id.fiscalyear_lock_date",
        readonly=False,
    )

    def name_get(self):
        """
        OVERWRITE Odoo original function name_get()

        Call with sudo. Otherwise, an ACL read error will be raised
        on ir.actions.act_window model.
        """
        action = (
            self.env["ir.actions.act_window"]
            .sudo()
            .search([("res_model", "=", self._name)], limit=1)
        )
        name = action.name or self._name
        return [(record.id, name) for record in self]

    def execute(self):
        """
        OVERWRITE Odoo original function execute().

        Called when settings are saved.
        - call `set_values`
        - do NOT check if user is admin
        - do NOT handle modules installation
        - trigger a web client reload.
        """
        self.ensure_one()
        # sudo to avoid error if some extra module add extra read configuration
        # in set_values().
        # (For exemple, in sale module set_values try to read ir.cron)
        self.sudo().set_values()
        return {
            "type": "ir.actions.client",
            "tag": "reload",
        }
