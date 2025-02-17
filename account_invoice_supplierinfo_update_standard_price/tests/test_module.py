# Copyright 2018 - Today: GRAP (http://www.grap.coop)
# Copyright Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo.tests import Form, tagged

from odoo.addons.account_invoice_supplierinfo_update_triple_discount.tests import (
    test_module,
)


@tagged("post_install", "-at_install")
class TestModuleStandardPrice(test_module.TestModuleTripleDiscount):
    @classmethod
    def setUpClass(cls, chart_template_ref=None):
        super().setUpClass(chart_template_ref=chart_template_ref)

        cls.product_d = cls.env["product.product"].create(
            {
                "name": "product_d",
                "uom_id": cls.env.ref("uom.product_uom_unit").id,
                "uom_po_id": cls.env.ref("uom.product_uom_unit").id,
                "lst_price": 10.0,
                "standard_price": 0.0,
                "property_account_income_id": cls.copy_account(
                    cls.company_data["default_account_revenue"]
                ).id,
                "property_account_expense_id": cls.copy_account(
                    cls.company_data["default_account_expense"]
                ).id,
                "taxes_id": [],
                "supplier_taxes_id": [],
                "is_impact_standard_price": True,
            }
        )

    def _add_impact_standard_price_line(self):
        with Form(self.invoice) as invoice_form:
            with invoice_form.invoice_line_ids.new() as line_form:
                line_form.product_id = self.product_d
                line_form.quantity = 15
                line_form.price_unit = 1
                line_form.tax_ids.clear()
        invoice_form.save()

        self.line_d = self.invoice.invoice_line_ids.filtered(
            lambda x: x.product_id == self.product_d
        )

    # configuration
    # line_a (4000 $)
    # - quantity: 10 // price_unit: 400 // uom_id: uom_unit

    # line_b (5.6 $)
    # - quantity: 1 // price_unit: 10 // uom_id: uom_dozen
    # - discount1: 10.0 // discount2: 20.0 // discount3: 30.0

    # line_without_product (35 $)
    # - quantity: 1 // price_unit: 35

    # line_d (15 $)
    # - quantity: 15 // price_unit: 1

    # PRODUCT TOTAL: 4000 + 5.6 + 35 = 4040.60

    def test_invoice_new_field_computation(self):
        self.assertAlmostEqual(self.invoice.product_expense_total, 4000 + 5.6 + 35)
        self.assertAlmostEqual(self.invoice.distributed_expense_total, 0)
        self._add_impact_standard_price_line()
        self.assertAlmostEqual(self.invoice.distributed_expense_total, 15)

    def test_supplierinfo_update_standard_price_without_distributed(self):
        vals_wizard = self.invoice.check_supplierinfo().get("context", {})

        line_ids = vals_wizard.get("default_line_ids", {})

        self.assertEqual(len(line_ids), 2)
        self.assertAlmostEqual(line_ids[0][2]["new_standard_price"], 4000.0 / 10)
        self.assertAlmostEqual(line_ids[1][2]["new_standard_price"], 5.6)

        # Create and launch update process
        wizard = self.WizardUpdateSupplierinfo.create(
            {"line_ids": line_ids, "invoice_id": self.invoice.id}
        )

        wizard.update_supplierinfo()

        self.assertAlmostEqual(self.product_a.standard_price, 4000.0 / 10)
        self.assertAlmostEqual(self.product_b.standard_price, 5.6)

    def test_supplierinfo_update_standard_price_with_distributed(self):
        self._add_impact_standard_price_line()

        vals_wizard = self.invoice.check_supplierinfo().get("context", {})

        line_ids = vals_wizard.get("default_line_ids", {})

        self.assertEqual(len(line_ids), 2)
        self.assertAlmostEqual(
            line_ids[0][2]["new_standard_price"],
            self.invoice.currency_id.round((4000.0 + 15 * 4000 / 4040.60) / 10),
        )
        self.assertAlmostEqual(
            line_ids[1][2]["new_standard_price"],
            self.invoice.currency_id.round(5.6 + 15 * 5.6 / 4040.60),
        )
