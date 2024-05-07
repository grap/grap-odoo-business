# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestProductSettings(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.consigned_product_vat_5_A = cls.env.ref(
            "recurring_consignment.consigned_product_consignor_1_vat_5_A"
        )
        cls.consigned_product_vat_5_B = cls.env.ref(
            "recurring_consignment.consigned_product_consignor_1_vat_5_B"
        )
        cls.consignor_2 = cls.env.ref("recurring_consignment.consignor_2")
        cls.fiscal_classification_0_consignor_2 = cls.env.ref(
            "recurring_consignment.fiscal_classification_0_consignor_2"
        )

    def test_01_change_standard_price(self):
        """Test the prevention to set a not null standard price
        Product."""
        with self.assertRaises(ValidationError):
            self.consigned_product_vat_5_B.write({"standard_price": 5.0})
        self.consigned_product_vat_5_B.write({"standard_price": 0.0})

    def test_02_change_consignor_possible_uninvoiced(self):
        """Test if it's possible to change a consignor for a uninvoiced product"""
        self.consigned_product_vat_5_B.product_tmpl_id.write(
            {
                "consignor_partner_id": self.consignor_2.id,
                "fiscal_classification_id": self.fiscal_classification_0_consignor_2.id,
            }
        )

    def test_03_change_consignor_impossible_invoiced(self):
        """Test if it's impossible to change a consignor for an invoiced product."""
        with self.assertRaises(ValidationError):
            new_vals = {
                "consignor_partner_id": self.consignor_2.id,
                "fiscal_classification_id": self.fiscal_classification_0_consignor_2.id,
            }
            self.consigned_product_vat_5_A.product_tmpl_id.write(new_vals)
