# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestModule(TransactionCase):
    def setUp(self):
        super().setUp()
        self.WizardUpdate = self.env["wizard.update.invoice.supplierinfo"]
        self.ProductSupplierinfo = self.env["product.supplierinfo"]
        self.invoice_1 = self.env.ref(
            "account_invoice_supplierinfo_update_standard_price.invoice_1"
        )
        self.line_1_1 = self.env.ref(
            "account_invoice_supplierinfo_update_standard_price.line_1_1"
        )
        self.line_1_2 = self.env.ref(
            "account_invoice_supplierinfo_update_standard_price.line_1_2"
        )
        self.invoice_2 = self.env.ref(
            "account_invoice_supplierinfo_update_standard_price.invoice_2"
        )
        self.line_2_1 = self.env.ref(
            "account_invoice_supplierinfo_update_standard_price.line_2_1"
        )
        self.dozen_unit = self.env.ref("uom.product_uom_dozen")
        self.uom_unit = self.env.ref("uom.product_uom_unit")

    # Test Section
    def test_01_standard_price(self):
        # Set discounts on account lines
        self.line_2_1.write(
            {
                "price_unit": 1000,
                "discount": 10.0,
                "discount2": 20.0,
                "discount3": 30.0,
                "uom_id": self.uom_unit.id,
            }
        )

        # Launch and confirm Wizard
        lines_for_update = self.invoice_2._get_update_supplierinfo_lines()
        wizard = self.WizardUpdate.with_context(
            default_line_ids=lines_for_update, default_invoice_id=self.invoice_2.id
        ).create({})
        wizard.update_supplierinfo()

        # Check Regressions
        supplierinfo = self.ProductSupplierinfo.search(
            [
                ("product_tmpl_id", "=", self.line_2_1.product_id.product_tmpl_id.id),
                ("name", "=", self.invoice_2.partner_id.id),
            ]
        )

        self.assertEqual(
            len(supplierinfo),
            1,
            "Regression : Confirming wizard should have create a supplierinfo",
        )

        self.assertEqual(
            supplierinfo.discount,
            10,
            "Regression : Confirming wizard should have update main discount",
        )
        self.assertEqual(
            supplierinfo.discount2,
            20,
            "Confirming wizard should have update discount #2",
        )
        self.assertEqual(
            supplierinfo.discount3,
            30,
            "Confirming wizard should have update discount #3",
        )

        # Check Correct Standard Price
        self.assertEqual(
            self.line_2_1.product_id.standard_price,
            504,  # (1000 * 0.9 * 0.8 * 0.7)
            "Confirming wizard should have updated Product standard price",
        )

    def test_02_standard_price_different_uom(self):
        # Set discounts on account lines
        self.line_2_1.write(
            {
                "price_unit": 1000,
                "discount": 10.0,
                "discount2": 20.0,
                "discount3": 30.0,
                "uom_id": self.dozen_unit.id,
            }
        )

        # Launch and confirm Wizard
        lines_for_update = self.invoice_2._get_update_supplierinfo_lines()
        wizard = self.WizardUpdate.with_context(
            default_line_ids=lines_for_update, default_invoice_id=self.invoice_2.id
        ).create({})
        wizard.update_supplierinfo()

        # Check Correct Standard Price
        self.assertEqual(
            self.line_2_1.product_id.standard_price,
            42,  # (1000 * 0.9 * 0.8 * 0.7) / 12
            "Confirming wizard should have updated Product standard price",
        )

    def test_03_shared_cost(self):
        self.assertEqual(
            self.invoice_1.product_expense_total,
            7540,  # (1000 * 10 * 0.9 * 0.8 * 0.7) + 500 * 5,
            "Bad computation of the field 'Product Expenses Total'",
        )

        self.assertEqual(
            self.invoice_1.distributed_expense_total,
            1000,
            "Bad computation of the field 'Distributed Expenses Total'",
        )

        # Check that transport cost are ignored from the wizard
        lines_for_update = self.invoice_1._get_update_supplierinfo_lines()

        # Launch and confirm Wizard
        wizard = self.WizardUpdate.with_context(
            default_line_ids=lines_for_update, default_invoice_id=self.invoice_1.id
        ).create({})

        self.assertEqual(
            len(wizard.line_ids),
            2,
            "Update wizard should only two lines, ignoring Impact standard price",
        )

        self.assertEqual(
            {wizard.line_ids[0].product_id.id, wizard.line_ids[1].product_id.id},
            {self.line_1_1.product_id.id, self.line_1_2.product_id.id},
            "Update wizard should update all the expenses products.",
        )
        wizard.update_supplierinfo()

        # Check Correct Standard Price
        self.assertEqual(
            round(self.line_1_1.product_id.standard_price, 2),
            570.84,  # (5040 + 1000 * (5040 / 7540)) / 10
            "Landing cost should impact standard price of the purchased" " product",
        )

        # Check Correct Standard Price
        self.assertEqual(
            round(self.line_1_2.product_id.standard_price, 2),
            566.31,  # (2500 + 1000 * (2500 / 7540)) / 5
            "Landing cost should impact standard price of the purchased" " product",
        )
