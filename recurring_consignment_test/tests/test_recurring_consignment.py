# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from dateutil.relativedelta import relativedelta

from odoo.exceptions import Warning as UserError
from odoo.tests.common import TransactionCase


class TestRecurringConsignment(TransactionCase):

    def setUp(self):
        super().setUp()

        self.ProductProduct = self.env['product.product']
        self.AccountInvoice = self.env['account.invoice']
        self.CommissionWizard = self.env['invoice.commission.wizard']
        # self.report_obj = self.env['report']
        self.consigned_product_vat_5 = self.env.ref(
            'recurring_consignment_test.consigned_product_consignor_1_vat_5')
        self.consigned_product_vat_5_2 = self.env.ref(
            'recurring_consignment_test.consigned_product_consignor_1_vat_5_2')
        self.consignor_1 = self.env.ref(
            'recurring_consignment_test.consignor_1')
        self.consignor_2 = self.env.ref(
            'recurring_consignment_test.consignor_2')
        self.sale_pricelist_10 = self.env.ref(
            'recurring_consignment_test.sale_pricelist_10')
        self.sale_pricelist_50 = self.env.ref(
            'recurring_consignment_test.sale_pricelist_50')
        self.customer_invoice_1 = self.env.ref(
            'recurring_consignment_test.customer_invoice_1')
        self.customer_invoice_2 = self.env.ref(
            'recurring_consignment_test.customer_invoice_2')
        self.commission_product_vat_5 = self.env.ref(
            'recurring_consignment_test.commission_product_vat_5')
        self.commission_product_vat_20 = self.env.ref(
            'recurring_consignment_test.commission_product_vat_20')
        self.vat_5_include = self.env.ref(
            'recurring_consignment_test.vat_5_include')
        self.vat_20_exclude = self.env.ref(
            'recurring_consignment_test.vat_20_exclude')
        self.product_category = self.env.ref('product.product_category_all')
        self.invoice_report = self.env.ref('account.account_invoices')

    # Private Section
    def _test_pricelist(self, product, alternative):
        list_price = product.list_price
        res = self.sale_pricelist_50.price_get(product.id, 1)
        if alternative:
            self.assertEqual(
                res[self.sale_pricelist_50.id], list_price * 0.9,
                "Alternative Pricelist should be applyed if it is set")
        else:
            self.assertEqual(
                res[self.sale_pricelist_50.id], list_price * 0.5,
                "Default pricelist should be applyed if pricelist"
                " if no alternative pricelist is set.")

    # Test Section
    def test_01_change_consignor_possible(self):
        """Test if it's possible to change a consignor for an unmoved
        Product."""
        self.consigned_product_vat_5_2.consignor_partner_id =\
            self.consignor_2.id

    def test_02_change_consignor_impossible_invoiced(self):
        """Test if it's possible to change a consignor for an invoiced
        Product."""
        with self.assertRaises(UserError):
            self.consigned_product_vat_5.consignor_partner_id =\
                self.consignor_2.id

    def test_03_pricelist_existing_product_alternative(self):
        """Test if alternative pricelist mechanism works fine for existing
        products"""
        self.sale_pricelist_50.consignment_pricelist_id = False
        self.sale_pricelist_50.consignment_pricelist_id =\
            self.sale_pricelist_10
        self._test_pricelist(self.consigned_product_vat_5, True)

    def test_04_pricelist_existing_product_normal(self):
        """Test if normal pricelist mechanism works fine for existing
        products"""
        self.sale_pricelist_50.consignment_pricelist_id = False
        self._test_pricelist(self.consigned_product_vat_5, False)

    def test_05_pricelist_create_product_alternative(self):
        """Test if pricelist mechanism works fine for created products"""
        self.sale_pricelist_50.consignment_pricelist_id =\
            self.sale_pricelist_10
        product = self.ProductProduct.create({
            'name': 'New Product',
            'categ_id': self.product_category.id,
            'list_price': 100,
            'consignor_partner_id': self.consignor_1.id,
        })
        self._test_pricelist(product, True)

    def test_06_pricelist_create_product_normal(self):
        """Test if pricelist mechanism works fine for created products"""
        self.sale_pricelist_50.consignment_pricelist_id = False
        product = self.ProductProduct.create({
            'name': 'New Product',
            'categ_id': self.product_category.id,
            'list_price': 100,
            'consignor_partner_id': self.consignor_1.id,
        })
        self._test_pricelist(product, False)

    def test_07_commission(self):
        self.customer_invoice_1.action_invoice_open()
        self.customer_invoice_2.action_invoice_open()

        wizard = self.CommissionWizard.with_context(
            active_ids=[self.consignor_1.id]).create({})

        # import pdb; pdb.set_trace()
        wizard.max_date += relativedelta(months=1)
        wizard._onchange_max_date()

        wizard.invoice_commission()
        commission_invoices = self.AccountInvoice.search([
            ('partner_id', '=', self.consignor_1.id),
            ('is_consignment_invoice', '=', True)])
        self.assertEqual(
            len(commission_invoices), 1,
            "It should generate one invoice commission")

        commission_invoice = commission_invoices[0]
        lines_5 = commission_invoice.invoice_line_ids.filtered(
            lambda x: x.product_id.id == self.commission_product_vat_5.id)
        lines_20 = commission_invoice.invoice_line_ids.filtered(
            lambda x: x.product_id.id == self.commission_product_vat_20.id)
        # check invoice lines generated
        self.assertEqual(
            len(commission_invoice.invoice_line_ids), 2,
            "Two commission lines should be generated")
        self.assertEqual(
            len(lines_5), 1, "One 5% commission line should be generated")
        self.assertEqual(
            len(lines_20), 1, "One 20% commission line should be generated")

        # Check line #1 details (Tax Incl)
        line_5 = lines_5[0]
        self.assertEqual(
            line_5.quantity, 1, "Incorrect Commission Quantity.")
        self.assertEqual(
            line_5.price_unit, 2100 * 1.05,
            "Incorrect Commission Price Unit, awaiing "
            "(10,000 + 500) * 0.2 * 1.05")
        self.assertEqual(
            line_5.invoice_line_tax_ids.ids, [self.vat_5_include.id],
            "Incorrect Commission Tax.")

        # Check line #2 details (Tax Excl)
        line_20 = lines_20[0]
        self.assertEqual(
            line_20.quantity, 1, "Incorrect Commission Quantity.")
        self.assertEqual(
            line_20.price_unit, 20,
            "Incorrect Commission Price Unit, awaiting 100 * 0.2")
        self.assertEqual(
            line_20.invoice_line_tax_ids.ids, [self.vat_20_exclude.id],
            "Incorrect Commission Tax.")

        self.invoice_report.render_qweb_html(commission_invoices.ids)
