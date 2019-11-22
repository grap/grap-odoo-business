# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestModule(TransactionCase):

    def setUp(self):
        super().setUp()

        self.unit_uom = self.env.ref('uom.product_uom_unit')
        self.supplier_with_package = self.env.ref('base.res_partner_1')
        self.supplier_without_package = self.env.ref('base.res_partner_2')
        self.product = self.env.ref(
            'purchase_package_qty.product_product_package_6')
        self.purchase_order = self.env.ref(
            "purchase_package_qty.purchase_order")
        self.purchase_order_line = self.env.ref(
            "purchase_package_qty.purchase_order_line")

    # Test Section
    def test_01_purchase_order_line_onchange_package_strict(self):
        # [Functional Test] Check if onchange function changes
        # quantity (strict context)
        self.purchase_order.partner_id = self.supplier_with_package
        self.purchase_order_line.product_qty = 5
        self.purchase_order_line.onchange_product_id()
        self.assertEqual(
            self.purchase_order_line.product_qty, 6,
            "On change with package defined should round quantity")

    def test_02_purchase_order_line_onchange_no_package(self):
        # [Functional Test] Check if onchange function doesn't change
        # quantity (no package context)
        self.purchase_order.partner_id = self.supplier_without_package
        self.purchase_order_line.product_qty = 5
        self.purchase_order_line.onchange_product_id()
        self.assertEqual(
            self.purchase_order_line.product_qty, 5,
            "On change without package defined should not change quantity")
