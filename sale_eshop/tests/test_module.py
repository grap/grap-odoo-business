# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase
from odoo.tools import config


class TestModule(TransactionCase):
    def setUp(self):
        super().setUp()
        # We disable queue job for test
        self.env = self.env(
            context=dict(
                self.env.context,
                test_queue_job_no_delay=True,
            )
        )

        self.eshop_user = self.env.ref("sale_eshop.eshop_user")
        self.ResPartner = self.env["res.partner"].sudo(self.eshop_user)
        self.SaleOrder = self.env["sale.order"].sudo(self.eshop_user)
        self.ProductProduct = self.env["product.product"].sudo(self.eshop_user)
        self.customer = self.env.ref("sale_eshop.demo_eshop_user")
        self.banana = self.env.ref("sale_eshop.product_banana")
        self.apple = self.env.ref("sale_eshop.product_apple")
        self.product_disabled = self.env.ref("sale_eshop.product_disabled")
        self.product_not_available = self.env.ref("product.product_product_4d")
        self.recovery_moment = self.env.ref("sale_recovery_moment.recovery_moment_1")
        self.sysadmin_passkey = "SysAdminPasskeyPa$$w0rd"

    # Test Section
    def test_01_login(self):
        # The following line make the test working if user_partners_access
        # is installed
        self.customer.active = True
        res = self.ResPartner.eshop_login(
            self.customer.email, self.customer.eshop_password
        )
        self.assertNotEqual(res, False, "Correct Credentials should be accepted")

        res = self.ResPartner.eshop_login(self.customer.email, "BAD_PASSWORD")
        self.assertEqual(res, False, "Bad Credentials should be refused")

        res = self.ResPartner.eshop_login(self.customer.email, self.sysadmin_passkey)
        self.assertEqual(
            res,
            False,
            "Admin Password should not be accepted if `auth_admin_passkey`"
            " is not set",
        )

        config["auth_admin_passkey_password"] = self.sysadmin_passkey
        res = self.ResPartner.eshop_login(self.customer.email, self.sysadmin_passkey)
        self.assertNotEqual(res, False, "Admin Password should be accepted")

    def test_02_load_products(self):
        result = self.ProductProduct.get_current_eshop_product_list()
        self.assertNotEqual(
            len(result), 0, "Loading products should return a non empty list"
        )

    def test_03_product_available(self):
        self.assertEqual(
            self.product_not_available.eshop_state,
            "unavailable",
            "Bad state for unavailable product",
        )

        self.assertEqual(
            self.banana.eshop_state,
            "available",
            "Bad state for available product",
        )

        self.assertEqual(
            self.product_disabled.eshop_state,
            "disabled",
            "Bad state for disabled product",
        )

    def test_03_sale_order_process(self):
        # Create Order
        self.SaleOrder.eshop_set_quantity(self.customer.id, self.banana.id, 3, "add")
        order = self.SaleOrder.eshop_get_current_sale_order(self.customer.id)
        self.assertNotEqual(
            order,
            False,
            "Adding a product for a customer that don't have sale order"
            " should create a new sale order",
        )

        order_line = order.order_line[0]
        self.assertEqual(
            order_line.product_uom_qty,
            3,
            "Adding a quantity should create a line with that quantity",
        )

        # Add quantity to the same product
        self.SaleOrder.eshop_set_quantity(self.customer.id, self.banana.id, 2, "add")
        order_line = order.order_line[0]
        self.assertEqual(
            order_line.product_uom_qty,
            5,
            "Adding a quantity should sum with the previous quantity",
        )

        # set new quantity to the same product
        self.SaleOrder.eshop_set_quantity(self.customer.id, self.banana.id, 1, "set")
        self.assertEqual(
            order_line.product_uom_qty,
            1,
            "setting a quantity should erase previous quantity",
        )

        # set new quantity below the limit
        self.SaleOrder.eshop_set_quantity(self.customer.id, self.banana.id, 0.2, "set")
        self.assertEqual(
            order_line.product_uom_qty,
            0.5,
            "setting a quantity should not be bellow the limit",
        )

        # set new quantity to round
        self.SaleOrder.eshop_set_quantity(
            self.customer.id, self.banana.id, 0.555, "set"
        )
        self.assertEqual(
            order_line.product_uom_qty,
            0.6,
            "Setting an invalidd quantity should round the final quantity",
        )

        # Select a recovery moment
        self.SaleOrder.eshop_select_recovery_moment(
            self.customer.id, self.recovery_moment.id
        )
        self.assertEqual(
            order.state,
            "sale",
            "Finishing an order in the eshop should set the order as 'sale'",
        )
