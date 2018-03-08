# coding: utf-8
# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestModule(TransactionCase):

    def setUp(self):
        super(TestModule, self).setUp()
        self.wizard_obj = self.env['wizard.update.invoice.supplierinfo']
        self.supplierinfo_obj = self.env['product.supplierinfo']
        self.partnerinfo_obj = self.env['pricelist.partnerinfo']
        self.invoice = self.env.ref('account.demo_invoice_0')
        self.invoice_line_0 = self.env.ref(
            'account.demo_invoice_0_line_rpanrearpanelshe0')
        self.invoice_line_1 = self.env.ref(
            'account.demo_invoice_0_line_rckrackcm0')
        self.toner_template = self.env.ref(
            'product.product_product_39_product_template')
        self.transport_costs_product = self.env.ref(
            'account_invoice_supplierinfo_update_standard_price'
            '.transport_costs_product')
        self.dozen_unit = self.env.ref('product.product_uom_dozen')

    # Test Section
    def test_01_standard_price(self):
        # Set discounts on account lines
        self.invoice_line_0.write({
            'price_unit': 1000,
            'discount': 10.0,
            'discount2': 20.0,
            'discount3': 30.0,
            'uos_id': self.dozen_unit.id,
        })

        # Launch and confirm Wizard
        lines_for_update = self.invoice._get_update_supplierinfo_lines()
        wizard = self.wizard_obj.with_context(
            default_line_ids=lines_for_update,
            default_invoice_id=self.invoice.id).create({})
        wizard.update_supplierinfo()

        # Check Regressions
        supplierinfo = self.supplierinfo_obj.search([
            ('product_tmpl_id', '=', self.toner_template.id),
            ('name', '=', self.invoice.partner_id.id)])

        self.assertEqual(
            len(supplierinfo), 1,
            "Regression : Confirming wizard should have create a supplierinfo")
        partnerinfo = self.partnerinfo_obj.search([
            ('suppinfo_id', '=', supplierinfo.id)])
        self.assertEqual(
            len(partnerinfo), 1,
            "Regression : Confirming wizard should have create a partnerinfo")
        self.assertEqual(
            partnerinfo.discount, 10,
            "Regression : Confirming wizard should have update main discount")
        self.assertEqual(
            partnerinfo.discount2, 20,
            "Confirming wizard should have update discount #2")
        self.assertEqual(
            partnerinfo.discount3, 30,
            "Confirming wizard should have update discount #3")

        # Check Correct Standard Price
        self.assertEqual(
            self.invoice_line_0.product_id.standard_price,
            42,  # (1000 * 0.9 * 0.8 * 0.7) / 12
            "Confirming wizard should have updated Product standard price")

    # Test Section
    def test_02_shared_cost(self):
        # Adding transport cost of 7 € on an invoice of 14 € (14 + 10)
        self.invoice_line.create({
            'invoice_id': self.invoice.id,
            'product_id': self.transport_costs_product.id,
            'quantity': 1,
            'price_unit': 7,
        })

        self.assertEqual(
            self.invoice.product_expense_total, 14,
            "Bad computation of the field 'Product Expenses Total'")

        self.assertEqual(
            self.invoice.distributed_expense_total, 7,
            "Bad computation of the field 'Distributed Expenses Total'")

        # Check that transport cost are ignored from the wizard
        lines_for_update = self.invoice._get_update_supplierinfo_lines()
        self.assertEqual(
            len(lines_for_update), 2,
            "Update wizard should not update 'Impact Standard Price' Product.")

        # Launch and confirm Wizard
        wizard = self.wizard_obj.with_context(
            default_line_ids=lines_for_update,
            default_invoice_id=self.invoice.id).create({})
        wizard.update_supplierinfo()

        # Check Correct Standard Price
        self.assertEqual(
            self.invoice_line_0.product_id.standard_price,
            15,  # 10 (Unit Price) + 5 (= 7 * (10 / 14)
            "Landing cost should impact standard price of the purchased"
            " product")

        # Check Correct Standard Price
        self.assertEqual(
            self.invoice_line_1.product_id.standard_price,
            6,  # 4 (Unit Price) + 2 (= 7 * (4 / 14)
            "Landing cost should impact standard price of the purchased"
            " product")
