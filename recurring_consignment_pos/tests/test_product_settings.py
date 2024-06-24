# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.exceptions import ValidationError
from odoo.tests.common import tagged

from odoo.addons.recurring_consignment.tests.test_product_settings import (
    TestProductSettings,
)

from .test_abstract import TestAbstract


@tagged("post_install", "-at_install")
class TestProductSettingsPointOfSale(TestAbstract, TestProductSettings):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product_D = cls.env.ref(
            "recurring_consignment.consigned_product_consignor_1_vat_20_D"
        )

    def test_51_change_consignor_no_pos_order(self):
        """Test if it's possible to change a consignor for a product
        that has not been saled in a pos order"""
        self.product_E.product_tmpl_id.write(
            {
                "consignor_partner_id": self.consignor_2.id,
                "fiscal_classification_id": self.fiscal_classification_0_consignor_2.id,
            }
        )

    def test_52_change_consignor_openened_session(self):
        """Test if it's impossible to change a consignor for a product
        if a session is opened"""
        self._make_pos_order(product=self.product_D, close_session=False)
        with self.assertRaises(ValidationError):
            new_vals = {
                "consignor_partner_id": self.consignor_2.id,
                "fiscal_classification_id": self.fiscal_classification_0_consignor_2.id,
            }
            self.product_E.product_tmpl_id.write(new_vals)

    def test_53_change_consignor_closed_session(self):
        """Test if it's possible to change a consignor for a product
        if a session is closed and the product has not been sold"""
        self._make_pos_order(product=self.product_D, close_session=True)
        new_vals = {
            "consignor_partner_id": self.consignor_2.id,
            "fiscal_classification_id": self.fiscal_classification_0_consignor_2.id,
        }
        self.product_E.product_tmpl_id.write(new_vals)

    def test_54_change_consignor_with_pos_order(self):
        """Test if it's impossible to change a consignor for a product
        that has been saled in a pos order"""
        self._make_pos_order(product=self.product_E, close_session=True)
        with self.assertRaises(ValidationError):
            new_vals = {
                "consignor_partner_id": self.consignor_2.id,
                "fiscal_classification_id": self.fiscal_classification_0_consignor_2.id,
            }
            self.product_E.product_tmpl_id.write(new_vals)
