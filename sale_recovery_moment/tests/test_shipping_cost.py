# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestShippingCost(TransactionCase):
    def setUp(self):
        super().setUp()
        # With
        self.sale_order_with = self.env.ref("sale_recovery_moment.sale_order_1")
        self.sale_order_with_qty = 3
        # Without
        self.sale_order_without = self.env.ref("sale_recovery_moment.sale_order_2")
        self.sale_order_without_qty = 1
        # Recovery Moment
        self.recovery_moment_with = self.env.ref(
            "sale_recovery_moment.recovery_moment_1"
        )
        self.recovery_moment_without = self.env.ref(
            "sale_recovery_moment.recovery_moment_2"
        )

    def test_01_with_change_to_without(self):
        # Shipping product is written on first write
        self.assertEqual(
            len(self.sale_order_with.order_line),
            self.sale_order_with_qty,
            "Write a sale order associated to a recovery place with"
            " shipping cost should create extra order line.",
        )
        self.sale_order_with.recovery_moment_id = self.recovery_moment_without
        self.assertEqual(
            len(self.sale_order_with.order_line),
            self.sale_order_with_qty - 1,
            "Setting recovery moment without shipping product should"
            " remove associated line",
        )

    def test_02_without_change_to_with(self):
        self.assertEqual(
            len(self.sale_order_without.order_line),
            self.sale_order_without_qty,
            "Write a sale order associated to a recovery place without"
            " shipping cost should not create extra order line.",
        )
        self.sale_order_without.recovery_moment_id = self.recovery_moment_with
        self.assertEqual(
            len(self.sale_order_without.order_line),
            self.sale_order_without_qty + 1,
            "Setting recovery moment with shipping product should"
            " create an extra order line",
        )
