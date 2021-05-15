# Copyright 2021 - Today Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestModule(TransactionCase):
    def setUp(self):
        super().setUp()
        self.ProductProduct = self.env["product.product"]
        self.ProductTemplate = self.env["product.template"]
        self.alimentary_category = self.env.ref("product_food.alimentary_category")
        self.main_category = self.env.ref("product.product_category_all")
        self.uom_unit = self.env.ref("uom.product_uom_unit")

    def test_product_product(self):
        product = self.ProductProduct.create(
            {
                "name": "Product",
                "uom_id": self.uom_unit.id,
                "uom_po_id": self.uom_unit.id,
                "categ_id": self.alimentary_category.id,
            }
        )
        self.assertEqual(product.is_alimentary, True)

        # Affect product to a non-alimentary category and run onchange
        product.categ_id = self.main_category.id
        product.onchange_categ_id_is_alimentary()
        self.assertEqual(product.is_alimentary, False)

        # Set non-alimentary category as a alimentary category and propagate settings
        # to all the child product
        self.main_category.is_alimentary = True
        self.main_category.button_apply_is_alimentary_settings()
        self.assertEqual(product.is_alimentary, True)
