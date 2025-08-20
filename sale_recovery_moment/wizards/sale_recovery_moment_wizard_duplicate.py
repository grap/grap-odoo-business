# Copyright (C) 2022 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class SaleRecoveryMomentWizardDuplicate(models.TransientModel):
    _name = "sale.recovery.moment.wizard.duplicate"
    _description = "Recovery Duplication Wizard"

    # Columns Section
    moment_ids = fields.Many2many(
        string="Moment to Duplicate",
        comodel_name="sale.recovery.moment",
        relation="sale_recovery_moment_wizard_duplicate_moment_rel",
        required=True,
        default=lambda x: x._default_moment_ids(),
    )

    day_delay = fields.Integer(
        string="Delay (Day)",
        required=True,
        help="Please set a positive number here.\n"
        "The wizard will duplicate the selected moments moving forward"
        " all the dates by the delay.",
    )

    recurrence = fields.Integer(
        default=1,
        help="The wizard will duplicate the selected moments the specified number"
        " of times on this recurrence.",
    )

    @api.constrains("day_delay")
    def _check_day_delay(self):
        if self.day_delay <= 0:
            raise ValidationError(_("Delay should be strictly positive."))

    @api.constrains("recurrence")
    def _check_recurrence(self):
        if self.recurrence <= 0:
            raise ValidationError(_("Recurrence should be strictly positive."))

    # Defaults Section
    @api.model
    def _default_moment_ids(self):
        return self.env.context.get("active_ids", [])

    # View Sections
    def duplicate_moments(self):
        self.ensure_one()
        SaleRecoveryMoment = self.env["sale.recovery.moment"]

        # Check if selected moments are correct
        if self.moment_ids.filtered(lambda x: x.group_id):
            raise ValidationError(
                _("You can not duplicate moments related to a recovery moment group.")
            )

        # Create New Moments
        new_moments = []
        base_moments = self.moment_ids

        i = 0
        for i in range(self.recurrence):
            generated = []
            for old_moment in base_moments:
                new_moment = SaleRecoveryMoment.create(
                    self._prepare_moment_vals(old_moment)
                )
                generated.append(new_moment)
            new_moments.extend(generated)
            base_moments = generated
            i += 1

        action_data = self.env.ref(
            "sale_recovery_moment.action_sale_recovery_moment"
        ).read()[0]
        action_data["display_name"] = _("Duplicated Recovery Moments")
        if len(new_moments) == 1:
            view = self.env.ref("sale_recovery_moment.view_sale_recovery_moment_form")
            action_data["views"] = [(view.id, "form")]
            action_data["res_id"] = new_moments[0].id
        else:
            action_data["domain"] = [("id", "in", [x.id for x in new_moments])]
            action_data["views"] = [
                (False, "tree"),
                (False, "calendar"),
                (False, "form"),
            ]
            action_data["context"] = False
        return action_data

    def _prepare_moment_vals(self, old_moment):
        return {
            "min_sale_date": old_moment.min_sale_date
            + relativedelta(days=self.day_delay),
            "max_sale_date": old_moment.max_sale_date
            + relativedelta(days=self.day_delay),
            "min_recovery_date": old_moment.min_recovery_date
            + relativedelta(days=self.day_delay),
            "max_recovery_date": old_moment.max_recovery_date
            + relativedelta(days=self.day_delay),
            "company_id": old_moment.company_id.id,
            "place_id": old_moment.place_id.id,
            "max_order_qty": old_moment.max_order_qty,
            "description": old_moment.description,
        }
