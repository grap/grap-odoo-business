# Copyright (C) 2022 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.addons.stock_picking_report_summary.tests.test_module import (
    TestModule as TestModuleReport,
)


class TestPickingSummaryReport(TestModuleReport):
    def setUp(self):
        super().setUp()
        self.sale_order = self.env.ref("sale_recovery_moment.sale_order_1")

    def _confirm_order_generate_summary_report(self):
        self.sale_order.action_confirm()

        pickings = self.sale_order.picking_ids
        wizard = self.PickingReportWizard.with_context(
            active_model="stock.picking",
            active_ids=pickings.ids,
        ).create({})

        return str(
            self.ir_actions_report._render_qweb_html(self.report_name, wizard.ids)[0]
        )

    def test_01_wizard_report_summary_with_recovery_moment(self):
        result = self._confirm_order_generate_summary_report()
        self.assertIn("Recovery:", result)

    def test_02_wizard_report_summary_without_recovery_moment(self):
        self.sale_order.recovery_moment_id = False
        result = self._confirm_order_generate_summary_report()
        self.assertNotIn("Recovery:", result)
