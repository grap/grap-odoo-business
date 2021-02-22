# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models


class SaleRecoveryMomentGroupWizardDuplicate(models.TransientModel):
    _name = "sale.recovery.moment.group.wizard.duplicate"
    _description = "Recovery Group Duplication Wizard"

    # Columns Section
    group_id = fields.Many2one(
        "sale.recovery.moment.group",
        "Group to Duplicate",
        required=True,
        default=lambda x: x._default_group_id(),
    )

    day_delay = fields.Integer(
        string="Delay (Day)",
        required=True,
        help="Please set a positive number here.\n"
        "The wizard will duplicate the current group moving forward"
        " all the dates by the delay.",
    )

    short_name = fields.Char(string="Short Name", required=True)

    next_min_sale_date = fields.Datetime(string="Next Minimum Sale Date", readonly=True)

    next_max_sale_date = fields.Datetime(
        string="Next Maximum Sale Date",
        readonly=True,
    )

    # Defaults Section
    @api.model
    def _default_group_id(self):
        return self.env.context.get("active_id", False)

    # View Sections
    @api.multi
    def duplicate_group(self):
        self.ensure_one()
        SaleRecoveryMoment = self.env["sale.recovery.moment"]
        SaleRecoveryMomentGroup = self.env["sale.recovery.moment.group"]

        # Create new group
        new_group = SaleRecoveryMomentGroup.create(self._prepare_group_vals())

        # Create New Moment
        for moment in self.group_id.moment_ids:
            moment_vals = {
                "group_id": new_group.id,
                "min_recovery_date": moment.min_recovery_date
                + relativedelta(days=self.day_delay),
                "max_recovery_date": moment.max_recovery_date
                + relativedelta(days=self.day_delay),
                "place_id": moment.place_id.id,
                "max_order_qty": moment.max_order_qty,
                "description": moment.description,
            }
            SaleRecoveryMoment.create(moment_vals)

        action_data = self.env.ref(
            "sale_recovery_moment.action_sale_recovery_moment_group"
        ).read()[0]
        view = self.env.ref("sale_recovery_moment.view_sale_recovery_moment_group_form")
        action_data["views"] = [(view.id, "form")]
        action_data["res_id"] = new_group.id
        return action_data

    # View Section
    @api.onchange("group_id", "day_delay")
    def onchange_day_delay(self):
        if self.day_delay and self.group_id:
            self.next_min_sale_date = self.group_id.min_sale_date + relativedelta(
                days=self.day_delay
            )
            self.next_max_sale_date = self.group_id.max_sale_date + relativedelta(
                days=self.day_delay
            )
        else:
            self.next_min_sale_date = False
            self.next_max_sale_date = False

    @api.multi
    def _prepare_group_vals(self):
        return {
            "short_name": self.short_name,
            "min_sale_date": self.next_min_sale_date,
            "max_sale_date": self.next_max_sale_date,
            "company_id": self.group_id.company_id.id,
        }
