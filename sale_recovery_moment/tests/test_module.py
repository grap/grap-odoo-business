# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields
from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


class TestModule(TransactionCase):
    def setUp(self):
        super().setUp()
        self.SaleRecoveryMomentWizardDuplicate = self.env[
            "sale.recovery.moment.wizard.duplicate"
        ]

        self.SaleRecoveryMomentGroupWizardDuplicate = self.env[
            "sale.recovery.moment.group.wizard.duplicate"
        ]
        self.SaleRecoveryMoment = self.env["sale.recovery.moment"]
        self.SaleRecoveryMomentGroup = self.env["sale.recovery.moment.group"]
        self.sale_order = self.env.ref("sale_recovery_moment.sale_order_1")
        self.moment_group = self.env.ref("sale_recovery_moment.recovery_moment_group_1")
        self.recovery_moment_with = self.env.ref(
            "sale_recovery_moment.recovery_moment_1"
        )
        self.recovery_moment_without = self.env.ref(
            "sale_recovery_moment.recovery_moment_2"
        )
        self.recovery_moment_without_group = self.env.ref(
            "sale_recovery_moment.recovery_moment_without_group"
        )
        self.order_line_qty = len(self.sale_order.order_line)

    def test_01_confirm_without_shipping(self):
        self.sale_order.recovery_moment_id = self.recovery_moment_without
        self.sale_order.action_confirm()
        self.assertEqual(
            len(self.sale_order.order_line),
            self.order_line_qty,
            "Confirming a sale order associated to a recovery place without"
            " shipping cost should not create extra order line.",
        )

    def test_02_confirm_with_shipping(self):
        self.sale_order.recovery_moment_id = self.recovery_moment_with
        self.sale_order.action_confirm()
        self.assertEqual(
            len(self.sale_order.order_line),
            self.order_line_qty + 1,
            "Confirming a sale order associated to a recovery place with"
            " shipping cost should add an extra order line.",
        )

    def test_03_wizard_duplicate_group(self):
        # Duplicate 1 group
        wizard = self.SaleRecoveryMomentGroupWizardDuplicate.with_context(
            active_ids=[self.moment_group.id]
        ).create(
            {
                "day_delay": 240,
            }
        )
        wizard.onchange_day_delay()
        action_data = wizard.duplicate_groups()
        new_group_id = action_data.get("res_id")
        new_group = self.SaleRecoveryMomentGroup.browse(new_group_id)
        self.assertEqual(
            new_group.state,
            "futur",
            "incorrect state of the group, when duplicating it",
        )

        # duplicate many groups
        wizard = self.SaleRecoveryMomentGroupWizardDuplicate.with_context(
            active_ids=[self.moment_group.id, new_group_id]
        ).create(
            {
                "day_delay": 700,
            }
        )
        action_data = wizard.duplicate_groups()

    def test_04_wizard_duplicate_moment(self):
        # Duplicate 1 moment
        wizard = self.SaleRecoveryMomentWizardDuplicate.with_context(
            active_ids=[self.recovery_moment_without_group.id]
        ).create(
            {
                "day_delay": 140,
            }
        )
        action_data = wizard.duplicate_moments()
        new_moment_id = action_data.get("res_id")
        new_moment = self.SaleRecoveryMoment.browse(new_moment_id)
        self.assertTrue(new_moment.specific_min_sale_date > fields.Datetime.today())

        # duplicate many moments
        wizard = self.SaleRecoveryMomentWizardDuplicate.with_context(
            active_ids=[self.recovery_moment_without_group.id, new_moment_id]
        ).create(
            {
                "day_delay": 700,
            }
        )
        action_data = wizard.duplicate_moments()

        # try to duplicate a moment related to a group should fail
        wizard = self.SaleRecoveryMomentWizardDuplicate.with_context(
            active_ids=[self.recovery_moment_with.id]
        ).create(
            {
                "day_delay": 140,
            }
        )

        with self.assertRaises(ValidationError):
            action_data = wizard.duplicate_moments()
