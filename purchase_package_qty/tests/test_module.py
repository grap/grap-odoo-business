# coding: utf-8
# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestModule(TransactionCase):
    """Tests for 'Purchase Package Quantity' Module"""

    def setUp(self):
        super(TestModule, self).setUp()

        self.order_line_obj = self.env['purchase.order.line']

        self.unit_uom = self.env.ref('product.product_uom_unit')
        self.supplier_with_package_strict = self.env.ref('base.res_partner_1')
        self.supplier_with_package_indicative = self.env.ref(
            'base.res_partner_2')
        self.supplier_without_package = self.env.ref(
            'base.res_partner_3')
        self.product = self.env.ref(
            'purchase_package_qty.product_product_package_6')

    # Test Section
    def test_01_purchase_order_line_onchange_package_strict(self):
        """[Functional Test] Check if onchange function changes
            quantity (strict context)"""
        value = self.order_line_obj.onchange_product_id(
            False, self.product.id, 5, self.unit_uom.id,
            self.supplier_with_package_strict.id).get('value', {})
        self.assertEqual(
            value.get('product_qty', False), 6,
            "On change on strict package should change quantity")

    def test_02_purchase_order_line_onchange_package_indicative(self):
        """[Functional Test] Check if onchange function doesn't change
            quantity (indicative context)"""
        value = self.order_line_obj.onchange_product_id(
            False, self.product.id, 5, self.unit_uom.id,
            self.supplier_with_package_indicative.id).get('value', {})
        self.assertEqual(
            value.get('product_qty', False), 5,
            "On change on indicative package should not change quantity")

    def test_03_purchase_order_line_onchange_no_package(self):
        """[Functional Test] Check if onchange function doesn't change
            quantity (no package context)"""
        value = self.order_line_obj.onchange_product_id(
            False, self.product.id, 5, self.unit_uom.id,
            self.supplier_without_package.id).get('value', {})
        self.assertEqual(
            value.get('product_qty', False), 5,
            "On change without package should not change quantity")
