# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo.tests.common import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestPricelist(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = cls.env.ref("recurring_consignment.company")
        cls.ProductProduct = cls.env["product.product"]

        cls.sale_pricelist_10 = cls.env.ref("recurring_consignment.sale_pricelist_10")
        cls.sale_pricelist_50 = cls.env.ref("recurring_consignment.sale_pricelist_50")

        cls.consigned_product_vat_5_A = cls.env.ref(
            "recurring_consignment.consigned_product_consignor_1_vat_5_A"
        )
        cls.product_category = cls.env.ref("product.product_category_all")
        cls.consignor_1 = cls.env.ref("recurring_consignment.consignor_1")
        cls.fiscal_classification_5_consignor_1 = cls.env.ref(
            "recurring_consignment.fiscal_classification_5_consignor_1"
        )

    # Private Section
    def _test_pricelist(self, product, alternative):
        if alternative:
            self.assertEqual(
                self.sale_pricelist_50._get_product_price(product, 1),
                product.list_price * 0.9,
                "Alternative Pricelist should be applyed if it is set",
            )
        else:
            self.assertEqual(
                self.sale_pricelist_50._get_product_price(product, 1),
                product.list_price * 0.5,
                "Default pricelist should be applyed if pricelist"
                " if no alternative pricelist is set.",
            )

    def test_10_pricelist_existing_product_alternative(self):
        """Test if alternative pricelist mechanism works fine for existing
        products"""
        self._test_pricelist(self.consigned_product_vat_5_A, True)

    def test_11_pricelist_existing_product_normal(self):
        """Test if normal pricelist mechanism works fine for existing
        products"""
        self.sale_pricelist_50.consignment_pricelist_id = False
        self._test_pricelist(self.consigned_product_vat_5_A, False)

    def test_12_pricelist_create_product_alternative(self):
        """Test if alternative pricelist mechanism works fine for created products"""
        self.sale_pricelist_50.consignment_pricelist_id = self.sale_pricelist_10
        product = self.ProductProduct.create(
            {
                "name": "New Product",
                "company_id": self.company.id,
                "categ_id": self.product_category.id,
                "list_price": 100,
                "consignor_partner_id": self.consignor_1.id,
                "fiscal_classification_id": self.fiscal_classification_5_consignor_1.id,
            }
        )
        self._test_pricelist(product, True)

    def test_13_pricelist_create_product_normal(self):
        """Test if normal pricelist mechanism works fine for created products"""
        self.sale_pricelist_50.consignment_pricelist_id = False
        product = self.ProductProduct.create(
            {
                "name": "New Product",
                "company_id": self.company.id,
                "categ_id": self.product_category.id,
                "list_price": 100,
                "consignor_partner_id": self.consignor_1.id,
                "fiscal_classification_id": self.fiscal_classification_5_consignor_1.id,
            }
        )
        self._test_pricelist(product, False)
