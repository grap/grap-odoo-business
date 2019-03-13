# coding: utf-8
# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from openerp.exceptions import Warning as UserError
from openerp.exceptions import ValidationError


class TestRecurringConsignment(TransactionCase):
    """Tests for 'Recurring Consignment' Module"""

    def setUp(self):
        super(TestRecurringConsignment, self).setUp()

        self.product_obj = self.env['product.product']
        self.session_obj = self.env['pos.session']
        self.order_obj = self.env['pos.order']
        self.invoice_obj = self.env['account.invoice']
        self.wizard_obj = self.env['invoice.commission.wizard']
        self.report_obj = self.env['report']
        self.sale_order = self.env.ref('recurring_consignment.sale_order_1')
        self.consigned_product_vat_5 = self.env.ref(
            'recurring_consignment.consigned_product_consignor_1_vat_5')
        self.consigned_product_vat_5_2 = self.env.ref(
            'recurring_consignment.consigned_product_consignor_1_vat_5_2')
        self.consignor_1 = self.env.ref(
            'recurring_consignment.consignor_1')
        self.consignor_2 = self.env.ref(
            'recurring_consignment.consignor_2')
        self.sale_pricelist_10 = self.env.ref(
            'recurring_consignment.sale_pricelist_10')
        self.sale_pricelist_50 = self.env.ref(
            'recurring_consignment.sale_pricelist_50')
        self.customer_invoice_1 = self.env.ref(
            'recurring_consignment.customer_invoice_1')
        self.customer_invoice_2 = self.env.ref(
            'recurring_consignment.customer_invoice_2')
        self.commission_product_vat_5 = self.env.ref(
            'recurring_consignment.commission_product_vat_5')
        self.commission_product_vat_20 = self.env.ref(
            'recurring_consignment.commission_product_vat_20')
        self.vat_5_exclude = self.env.ref(
            'recurring_consignment.vat_5_exclude')
        self.product_category = self.env.ref('product.product_category_all')
        self.main_config = self.env.ref('point_of_sale.pos_config_main')

    # Test Section
    def test_01_change_consignor_possible(self):
        """Test if it's possible to change a consignor for an unmoved
        Product."""
        self.consigned_product_vat_5_2.consignor_partner_id =\
            self.consignor_2.id

    def test_02_change_consignor_impossible_moved(self):
        """Test if it's possible to change a consignor for an moved
        Product."""
        self.sale_order.action_button_confirm()
        with self.assertRaises(UserError):
            self.consigned_product_vat_5_2.consignor_partner_id =\
                self.consignor_2.id

    def test_03_change_consignor_impossible_invoiced(self):
        """Test if it's possible to change a consignor for an invoiced
        Product."""
        with self.assertRaises(UserError):
            self.consigned_product_vat_5.consignor_partner_id =\
                self.consignor_2.id

    def test_04_pricelist_existing_product_alternative(self):
        """Test if alternative pricelist mechanism works fine for existing
        products"""
        self.sale_pricelist_50.consignment_pricelist_id = False
        self.sale_pricelist_50.consignment_pricelist_id =\
            self.sale_pricelist_10
        self._test_pricelist(self.consigned_product_vat_5, True)

    def test_05_pricelist_existing_product_normal(self):
        """Test if normal pricelist mechanism works fine for existing
        products"""
        self.sale_pricelist_50.consignment_pricelist_id = False
        self._test_pricelist(self.consigned_product_vat_5, False)

    def test_06_pricelist_create_product_alternative(self):
        """Test if pricelist mechanism works fine for created products"""
        self.sale_pricelist_50.consignment_pricelist_id =\
            self.sale_pricelist_10
        product = self.product_obj.create({
            'name': 'New Product',
            'categ_id': self.product_category.id,
            'list_price': 100,
            'consignor_partner_id': self.consignor_1.id,
        })
        self._test_pricelist(product, True)

    def test_07_pricelist_create_product_normal(self):
        """Test if pricelist mechanism works fine for created products"""
        self.sale_pricelist_50.consignment_pricelist_id = False
        product = self.product_obj.create({
            'name': 'New Product',
            'categ_id': self.product_category.id,
            'list_price': 100,
            'consignor_partner_id': self.consignor_1.id,
        })
        self._test_pricelist(product, False)

    def test_08_commission(self):
        self.customer_invoice_1.signal_workflow('invoice_open')
        self.customer_invoice_2.signal_workflow('invoice_open')
        wizard = self.wizard_obj.create({
            'consignor_partner_id': self.consignor_1.id,
            'period_id': self.customer_invoice_1.period_id.id,
        })
        wizard.invoice_commission()
        commission_invoices = self.invoice_obj.search([
            ('partner_id', '=', self.consignor_1.id),
            ('is_consignment_invoice', '=', True)])
        self.assertEqual(
            len(commission_invoices), 1,
            "It should generate one invoice commission")
        commission_invoice = commission_invoices[0]
        lines_5 = commission_invoice.invoice_line.filtered(
            lambda x: x.product_id.id == self.commission_product_vat_5.id)
        lines_20 = commission_invoice.invoice_line.filtered(
            lambda x: x.product_id.id == self.commission_product_vat_20.id)
        # check invoice lines generated
        self.assertEqual(
            len(commission_invoice.invoice_line), 2,
            "Two commission lines should be generated")
        self.assertEqual(
            len(lines_5), 1, "One 5% commission line should be generated")
        self.assertEqual(
            len(lines_20), 1, "One 20% commission line should be generated")

        # Check first line details
        line_5 = lines_5[0]
        self.assertEqual(
            line_5.quantity, 1, "Incorrect Commission Price Unit.")
        self.assertEqual(
            line_5.price_unit, 2100, "Incorrect Commission Price Unit.")
        self.assertEqual(
            line_5.invoice_line_tax_id.ids, [self.vat_5_exclude.id],
            "Incorrect Commission VAT.")

        self.report_obj.get_action(
            commission_invoice,
            'recurring_consignment.template_account_invoice_consignment')
        self.report_obj.get_html(
            commission_invoice,
            'recurring_consignment.template_account_invoice_consignment')

    # Test Section
    def test_09_pos_order_constrains(self):
        """[Functional Test] Check if creating a pos order with consignor
        is blocked"""
        self.session = self.session_obj.create(
            {'config_id': self.main_config.id})
        self.session.open_cb()
        with self.assertRaises(ValidationError):
            self.order_obj.create({
                'session_id': self.session.id,
                'partner_id': self.consignor_1.id,
            })

    def _test_pricelist(self, product, alternative):
        list_price = product.list_price
        res = self.sale_pricelist_50.price_get(product.id, 1)
        if alternative:
            self.assertEqual(
                res[self.sale_pricelist_50.id], list_price * 0.9,
                "Alternative Pricelist should be applyed if it is set")
        else:
            res = self.sale_pricelist_50.price_get(product.id, 1)
            self.assertEqual(
                res[self.sale_pricelist_50.id], list_price * 0.5,
                "Default pricelist should be applyed if pricelist"
                " if no alternative pricelist is set.")
