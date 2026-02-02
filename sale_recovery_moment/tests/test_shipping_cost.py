# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from dateutil.relativedelta import relativedelta

from odoo.fields import Datetime
from odoo.tests.common import TransactionCase


class TestShippingCost(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.company = cls.env.company
        cls.partner_1 = cls.env["res.partner"].create(
            {
                "name": "Partner Test 1",
            }
        )

        cls.shipping_product = cls.env["product.product"].create(
            {
                "name": "Shipping Cost",
                "type": "service",
            }
        )

        cls.recovery_place_white_house_without = cls.env["sale.recovery.place"].create(
            {
                "name": "The White House",
                "company_id": cls.company.id,
            }
        )
        cls.recovery_place_elysee_with = cls.env["sale.recovery.place"].create(
            {
                "name": "L'Élysée",
                "shipping_product_id": cls.shipping_product.id,
            }
        )

        # Recovery moments
        now = Datetime.now()
        cls.recovery_moment_with = cls.env["sale.recovery.moment"].create(
            {
                "place_id": cls.recovery_place_elysee_with.id,
                "min_recovery_date": now + relativedelta(days=1, hours=8),
                "max_recovery_date": now + relativedelta(days=1, hours=16),
            }
        )

        cls.recovery_moment_without = cls.env["sale.recovery.moment"].create(
            {
                "place_id": cls.recovery_place_white_house_without.id,
                "min_recovery_date": now + relativedelta(days=2, hours=12),
                "max_recovery_date": now + relativedelta(days=2, hours=15),
            }
        )

        # Products
        cls.product_1 = cls.env["product.product"].create(
            {
                "name": "A french Guillotine",
            }
        )

        # Sale Orders
        cls.sale_order = cls.env["sale.order"].create(
            {
                "partner_id": cls.partner_1.id,
            }
        )

        cls.env["sale.order.line"].create(
            {
                "order_id": cls.sale_order.id,
                "product_id": cls.product_1.id,
                "name": cls.product_1.name,
            }
        )
        cls.sale_order_lines_qty = 1

    def test_01_change_recovery_moment(self):
        self.assertEqual(
            len(self.sale_order.order_line),
            self.sale_order_lines_qty,
            "Test initialization is not correct.",
        )
        # Without
        self.sale_order.recovery_moment_id = self.recovery_moment_without
        self.assertEqual(
            len(self.sale_order.order_line),
            self.sale_order_lines_qty,
            "Setting recovery moment without shipping product should"
            " not create new line.",
        )
        # With
        self.sale_order.recovery_moment_id = self.recovery_moment_with
        self.assertEqual(
            len(self.sale_order.order_line),
            self.sale_order_lines_qty + 1,
            "Setting recovery moment with shipping product should"
            " create an extra order line",
        )
