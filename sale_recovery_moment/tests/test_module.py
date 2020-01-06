# coding: utf-8
# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestModule(TransactionCase):
    def setUp(self):
        super(TestModule, self).setUp()
        self.sale_order = self.env.ref("sale_recovery_moment.sale_order_1")
        self.recovery_moment_with = self.env.ref(
            "sale_recovery_moment.recovery_moment_1"
        )
        self.recovery_moment_without = self.env.ref(
            "sale_recovery_moment.recovery_moment_2"
        )
        self.order_line_qty = len(self.sale_order.order_line)

    def test_01_confirm_without_shipping(self):

        self.sale_order.recovery_moment_id = self.recovery_moment_without
        self.sale_order.action_button_confirm()
        self.assertEqual(
            len(self.sale_order.order_line),
            self.order_line_qty,
            "Confirming a sale order associated to a recovery place without"
            " shipping cost should not create extra order line.",
        )

    def test_02_confirm_with_shipping(self):

        self.sale_order.recovery_moment_id = self.recovery_moment_with
        self.sale_order.action_button_confirm()
        self.assertEqual(
            len(self.sale_order.order_line),
            self.order_line_qty + 1,
            "Confirming a sale order associated to a recovery place with"
            " shipping cost should add an extra order line.",
        )
