# Copyright (C) 2022 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.addons.stock_picking_report_summary.tests.test_module import (
    TestModule as TestModuleReport,
)


class TestModule(TestModuleReport):
    def setUp(self):
        super().setUp()
        self.sale_order = self.env.ref("sale_recovery_moment.sale_order_1")
        self.recovery_moment = self.env.ref("sale_recovery_moment.recovery_moment_1")

    def test_01_wizard_report_summary(self):
        self.sale_order.recovery_moment_id = self.recovery_moment
        self.sale_order.action_confirm()

        self._test_wizard(self.sale_order.picking_ids)
