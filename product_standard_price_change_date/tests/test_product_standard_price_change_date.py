# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT (quentin.dupont@grap.coop)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields
from odoo.tests.common import TransactionCase


class TestProductStandardPriceChangeDate(TransactionCase):
    def setUp(self):
        super().setUp()
        self.random_product = self.env["product.product"].create(
            {
                "name": "Product 1",
                "type": "product",
            }
        )
        self.assertFalse(self.random_product.standard_price_change_date)

    def test_01_product_standard_price_change_date(self):
        self.random_product.standard_price = 10
        self.random_product._onchange_standard_price_change_date()
        self.assertEqual(
            self.random_product.standard_price_change_date, fields.Date.today()
        )
