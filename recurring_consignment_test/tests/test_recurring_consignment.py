# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from datetime import timedelta

from odoo import fields
from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase, at_install, post_install


@at_install(False)
@post_install(True)
class TestRecurringConsignment(TransactionCase):
    def setUp(self):
        super().setUp()

        self.ProductProduct = self.env["product.product"]
        self.ResPartner = self.env["res.partner"]
        self.AccountProductFiscalClassification = self.env[
            "account.product.fiscal.classification"
        ]
        self.AccountInvoice = self.env["account.invoice"]
        self.CommissionWizard = self.env["invoice.commission.wizard"]
        self.ConsignorCreateWizard = self.env["consignor.create.wizard"]
        # self.report_obj = self.env['report']
        self.consigned_product_vat_5_A = self.env.ref(
            "recurring_consignment_test.consigned_product_consignor_1_vat_5_A"
        )
        self.consigned_product_vat_5_B = self.env.ref(
            "recurring_consignment_test.consigned_product_consignor_1_vat_5_B"
        )
        self.consignor_1 = self.env.ref("recurring_consignment_test.consignor_1")
        self.consignor_2 = self.env.ref("recurring_consignment_test.consignor_2")
        self.fiscal_classification_5_consignor_1 = self.env.ref(
            "recurring_consignment_test.fiscal_classification_5_consignor_1"
        )
        self.fiscal_classification_0_consignor_2 = self.env.ref(
            "recurring_consignment_test.fiscal_classification_0_consignor_2"
        )
        self.sale_pricelist_10 = self.env.ref(
            "recurring_consignment_test.sale_pricelist_10"
        )
        self.sale_pricelist_50 = self.env.ref(
            "recurring_consignment_test.sale_pricelist_50"
        )
        self.customer_invoice_1 = self.env.ref(
            "recurring_consignment_test.customer_invoice_1"
        )
        self.customer_invoice_2 = self.env.ref(
            "recurring_consignment_test.customer_invoice_2"
        )
        self.commission_product_vat_20 = self.env.ref(
            "recurring_consignment_test.commission_product_vat_20"
        )
        self.vat_5_include = self.env.ref("recurring_consignment_test.vat_5_include")
        self.vat_20_exclude = self.env.ref("recurring_consignment_test.vat_20_exclude")
        self.product_category = self.env.ref("product.product_category_all")
        self.invoice_report = self.env.ref("account.account_invoices")

    # Private Section
    def _test_pricelist(self, product, alternative):
        list_price = product.list_price
        res = self.sale_pricelist_50.price_get(product.id, 1)
        if alternative:
            self.assertEqual(
                res[self.sale_pricelist_50.id],
                list_price * 0.9,
                "Alternative Pricelist should be applyed if it is set",
            )
        else:
            self.assertEqual(
                res[self.sale_pricelist_50.id],
                list_price * 0.5,
                "Default pricelist should be applyed if pricelist"
                " if no alternative pricelist is set.",
            )

    def _make_commission(self, consignors):
        wizard = self.CommissionWizard.with_context(active_ids=consignors.ids).create(
            {}
        )

        # Set max date to the last day of the current month
        today = fields.date.today()
        if today.month < 12:
            wizard.max_date = fields.date(today.year, today.month + 1, 1) - timedelta(
                days=1
            )
        else:
            wizard.max_date = fields.date(today.year + 1, 1, 1) - timedelta(days=1)

        wizard._onchange_max_date()

        wizard.invoice_commission()

        return self.AccountInvoice.search(
            [
                ("partner_id", "=", self.consignor_1.id),
                ("is_consignment_invoice", "=", True),
            ]
        )

    # Test Section
    def test_01_change_consignor_possible(self):
        """Test if it's possible to change a consignor for an unmoved
        Product."""
        vals = {
            "consignor_partner_id": self.consignor_2.id,
            "fiscal_classification_id": self.fiscal_classification_0_consignor_2.id,
        }
        self.consigned_product_vat_5_B.write(vals)

    def test_02_change_consignor_impossible_invoiced(self):
        """Test if it's possible to change a consignor for an invoiced
        Product."""
        vals = {
            "consignor_partner_id": self.consignor_2.id,
            "fiscal_classification_id": self.fiscal_classification_0_consignor_2.id,
        }
        with self.assertRaises(ValidationError):
            self.consigned_product_vat_5_A.write(vals)

    def test_03_change_standard_price(self):
        """Test the prevention to set a not null standard price
        Product."""
        self.consigned_product_vat_5_B.write({"standard_price": 0.0})

        with self.assertRaises(ValidationError):
            self.consigned_product_vat_5_B.write({"standard_price": 5.0})

    def test_10_pricelist_existing_product_alternative(self):
        """Test if alternative pricelist mechanism works fine for existing
        products"""
        self.sale_pricelist_50.consignment_pricelist_id = False
        self.sale_pricelist_50.consignment_pricelist_id = self.sale_pricelist_10
        self._test_pricelist(self.consigned_product_vat_5_A, True)

    def test_11_pricelist_existing_product_normal(self):
        """Test if normal pricelist mechanism works fine for existing
        products"""
        self.sale_pricelist_50.consignment_pricelist_id = False
        self._test_pricelist(self.consigned_product_vat_5_A, False)

    def test_12_pricelist_create_product_alternative(self):
        """Test if pricelist mechanism works fine for created products"""
        self.sale_pricelist_50.consignment_pricelist_id = self.sale_pricelist_10
        product = self.ProductProduct.create(
            {
                "name": "New Product",
                "categ_id": self.product_category.id,
                "list_price": 100,
                "consignor_partner_id": self.consignor_1.id,
                "fiscal_classification_id": self.fiscal_classification_5_consignor_1.id,
            }
        )
        self._test_pricelist(product, True)

    def test_13_pricelist_create_product_normal(self):
        """Test if pricelist mechanism works fine for created products"""
        self.sale_pricelist_50.consignment_pricelist_id = False
        product = self.ProductProduct.create(
            {
                "name": "New Product",
                "categ_id": self.product_category.id,
                "list_price": 100,
                "consignor_partner_id": self.consignor_1.id,
                "fiscal_classification_id": self.fiscal_classification_5_consignor_1.id,
            }
        )
        self._test_pricelist(product, False)

    def test_20_consingor_creation_wizard(self):
        vals = {
            "name": "My Consignor",
            "account_suffix": "MYC1",
            "rate": 20.0,
            "is_vat_subject": True,
            "has_vat_000": False,
            "has_vat_021": False,
            "has_vat_055": True,
            "has_vat_100": False,
            "has_vat_200": True,
        }
        # Create consignor VAT Subject
        wizard = self.ConsignorCreateWizard = self.env[
            "consignor.create.wizard"
        ].create(vals)
        partner_id = wizard.create_consignor()["res_id"]
        partner = self.ResPartner.browse(partner_id)
        self.assertTrue(partner.is_consignor)
        self.assertEqual(partner.consignment_commission, 20)
        classifications = self.AccountProductFiscalClassification.search(
            [("consignor_partner_id", "=", partner.id)]
        )
        self.assertEqual(len(classifications), 2)

        # Create consignor not VAT Subject with bad configuration
        vals.update(
            {
                "account_suffix": "MYC2",
                "is_vat_subject": False,
            }
        )
        with self.assertRaises(ValidationError):
            self.ConsignorCreateWizard = self.env["consignor.create.wizard"].create(
                vals
            )

        # Create consignor not VAT Subject with correct configuration
        vals.update(
            {
                "has_vat_000": True,
                "has_vat_055": False,
                "has_vat_200": False,
            }
        )
        wizard = self.ConsignorCreateWizard = self.env[
            "consignor.create.wizard"
        ].create(vals)
        partner_id = wizard.create_consignor()["res_id"]
        partner = self.ResPartner.browse(partner_id)
        classifications = self.AccountProductFiscalClassification.search(
            [("consignor_partner_id", "=", partner.id)]
        )
        self.assertEqual(classifications[0].sale_tax_ids[0].amount, 0.0)

    def test_30_commission_workflow(self):
        self.customer_invoice_1.action_invoice_open()
        self.customer_invoice_2.action_invoice_open()

        commission_invoices = self._make_commission(self.consignor_1)

        self.assertEqual(
            len(commission_invoices), 1, "It should generate one invoice commission"
        )

        commission_invoice = commission_invoices[0]
        lines_20 = commission_invoice.invoice_line_ids.filtered(
            lambda x: x.product_id.id == self.commission_product_vat_20.id
        )
        # check invoice lines generated
        self.assertEqual(
            len(commission_invoice.invoice_line_ids),
            1,
            "Two commission lines should be generated",
        )
        self.assertEqual(
            len(lines_20), 1, "One 20% commission line should be generated"
        )

        # Check line #2 details (Tax Excl)
        line_20 = lines_20[0]
        self.assertEqual(line_20.quantity, 1, "Incorrect Commission Quantity.")
        self.assertEqual(
            line_20.price_unit,
            2100 + 20,
            "Incorrect Commission Price Unit, awaiting"
            " (10,000 + 500) * 0.2"
            " + 100 * 0.2",
        )
        self.assertEqual(
            line_20.invoice_line_tax_ids.ids,
            [self.vat_20_exclude.id],
            "Incorrect Commission Tax.",
        )

        self.invoice_report.render_qweb_html(commission_invoices.ids)

    def test_31_commission_refund(self):
        # confirm sale of (+50) unit
        self.customer_invoice_2.action_invoice_open()

        # Copy, change quantity (+90) and confirm
        copy_invoice = self.customer_invoice_2.copy()
        copy_invoice.invoice_line_ids[0].quantity = 90
        copy_invoice.action_invoice_open()

        # Make a refund change quantity (-20) and confirm.
        refund_invoice = self.customer_invoice_2.refund()
        refund_invoice.invoice_line_ids[0].quantity = 20
        refund_invoice.action_invoice_open()

        commission_invoices = self._make_commission(self.consignor_1)

        res = self.AccountInvoice.get_commission_information_product_detail(
            commission_invoices
        )[0]
        self.assertEqual(
            res["quantity"],
            50 + 90 - 20,
            "Error with refunded sale invoices : Bad quantity of product.",
        )

        self.assertEqual(
            res["total_vat_excl"],
            10 * (50 + 90 - 20),
            "Error with refunded sale invoices : Bad price subtotal vat excl.",
        )
