# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class SaleRecoveryMomentGroupWizardDuplicate(models.TransientModel):
    _name = "sale.recovery.moment.group.wizard.duplicate"
    _description = "Recovery Group Duplication Wizard"

    # Columns Section
    group_ids = fields.Many2many(
        string="Group to Duplicate",
        comodel_name="sale.recovery.moment.group",
        relation="sale_recovery_moment_group_wizard_duplicate_group_rel",
        required=True,
        default=lambda x: x._default_group_ids(),
    )

    group_qty = fields.Integer(string="Groups Quantity", compute="_compute_group_qty")

    day_delay = fields.Integer(
        string="Delay (Day)",
        required=True,
        help="Please set a positive number here.\n"
        "The wizard will duplicate the selected groups moving forward"
        " all the dates by the delay.",
    )

    next_min_sale_date = fields.Datetime(
        string="Next Minimum Sale Date",
        readonly=True,
    )

    next_max_sale_date = fields.Datetime(
        string="Next Maximum Sale Date",
        readonly=True,
    )

    @api.constrains("day_delay")
    def _check_day_delay(self):
        if self.day_delay <= 0:
            raise ValidationError(_("Delay should be strictly positive."))

    @api.depends("group_ids")
    def _compute_group_qty(self):
        for wizard in self:
            wizard.group_qty = len(wizard.group_ids)

    # Defaults Section
    @api.model
    def _default_group_ids(self):
        return self.env.context.get("active_ids", [])

    # View Sections
    @api.multi
    def duplicate_groups(self):
        self.ensure_one()
        SaleRecoveryMoment = self.env["sale.recovery.moment"]
        SaleRecoveryMomentGroup = self.env["sale.recovery.moment.group"]

        # Create New Groups
        new_groups = []
        for old_group in self.group_ids:
            new_group = SaleRecoveryMomentGroup.create(
                self._prepare_group_vals(old_group)
            )

            # Create New Moments
            for moment in old_group.moment_ids:
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
            new_groups.append(new_group)

        action_data = self.env.ref(
            "sale_recovery_moment.action_sale_recovery_moment_group"
        ).read()[0]
        if len(self.group_ids) == 1:
            view = self.env.ref(
                "sale_recovery_moment.view_sale_recovery_moment_group_form"
            )
            action_data["views"] = [(view.id, "form")]
            action_data["res_id"] = new_groups[0].id
        else:
            action_data["domain"] = [("id", "in", [x.id for x in new_groups])]
        return action_data

    # View Section
    @api.onchange("group_ids", "day_delay")
    def onchange_day_delay(self):
        if self.day_delay and len(self.group_ids) == 1:
            self.next_min_sale_date = self.group_ids[0].min_sale_date + relativedelta(
                days=self.day_delay
            )
            self.next_max_sale_date = self.group_ids[0].max_sale_date + relativedelta(
                days=self.day_delay
            )
        else:
            self.next_min_sale_date = False
            self.next_max_sale_date = False

    @api.multi
    def _prepare_group_vals(self, old_group):
        return {
            "short_name": _("%s (Copy)") % (old_group.short_name),
            "min_sale_date": old_group.min_sale_date
            + relativedelta(days=self.day_delay),
            "max_sale_date": old_group.max_sale_date
            + relativedelta(days=self.day_delay),
            "company_id": old_group.company_id.id,
        }
