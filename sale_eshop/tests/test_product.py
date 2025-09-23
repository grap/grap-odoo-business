# Copyright (C) 2025 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from datetime import date, timedelta

from odoo.exceptions import UserError
from odoo.tests.common import TransactionCase


class TestProduct(TransactionCase):
    def setUp(self):
        super().setUp()
        self.Product = self.env["product.product"]
        self.Category = self.env["eshop.category"]
        self.UoM = self.env.ref("uom.product_uom_unit")
        self.ProductTmpl = self.env["product.template"].create(
            {
                "name": "Test Template",
                "sale_ok": True,
                "uom_id": self.UoM.id,
                "type": "consu",
                "list_price": 10.0,
            }
        )
        self.category = self.Category.create(
            {
                "name": "Category A",
                "type": "normal",
            }
        )

    def test_01_compute_eshop_state_available(self):
        product = self.Product.create(
            {
                "product_tmpl_id": self.ProductTmpl.id,
                "eshop_category_id": self.category.id,
                "sale_ok": True,
                "active": True,
            }
        )
        self.assertEqual(product.eshop_state, "available")

    def test_02_compute_eshop_state_disabled_by_date(self):
        product = self.Product.create(
            {
                "product_tmpl_id": self.ProductTmpl.id,
                "eshop_category_id": self.category.id,
                "eshop_start_date": date.today() + timedelta(days=2),
                "eshop_end_date": date.today() + timedelta(days=10),
                "sale_ok": True,
                "active": True,
            }
        )
        self.assertEqual(product.eshop_state, "disabled")

    def test_03_compute_eshop_state_unavailable(self):
        product = self.Product.create(
            {
                "product_tmpl_id": self.ProductTmpl.id,
                "sale_ok": True,
                "active": True,
            }
        )
        self.assertEqual(product.eshop_state, "unavailable")

    def test_04_search_eshop_state_available(self):
        product = self.Product.create(
            {
                "product_tmpl_id": self.ProductTmpl.id,
                "eshop_category_id": self.category.id,
                "sale_ok": True,
                "active": True,
            }
        )
        domain = self.Product._search_eshop_state("=", "available")
        self.assertIn(product.id, domain[0][2])

    def test_05_search_eshop_state_unavailable(self):
        product = self.Product.create(
            {
                "product_tmpl_id": self.ProductTmpl.id,
                "sale_ok": True,
                "active": True,
            }
        )
        domain = self.Product._search_eshop_state("=", "unavailable")
        self.assertIn(product.id, domain[0][2])

    def test_06_search_eshop_state_invalid_operator(self):
        with self.assertRaises(UserError):
            self.Product._search_eshop_state(">", "available")

    def test_07_search_eshop_state_invalid_value(self):
        with self.assertRaises(UserError):
            self.Product._search_eshop_state("=", "fake_state")

    def test_08_load_products(self):
        result = self.Product.get_current_eshop_product_list()
        self.assertNotEqual(
            len(result), 0, "Loading products should return a non empty list"
        )
