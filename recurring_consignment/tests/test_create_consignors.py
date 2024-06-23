# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestCreateConsignors(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ResPartner = cls.env["res.partner"]
        cls.ConsignorCreateWizard = cls.env["consignor.create.wizard"]
        cls.AccountProductFiscalClassification = cls.env[
            "account.product.fiscal.classification"
        ]
        cls.env.user.company_id = cls.env.ref("recurring_consignment.company")

    def _create_consignor(self, extra_vals):
        vals = {
            "consignor_name": "My Consignor",
            "account_suffix": "MYC1",
            "commission_rate": 20.0,
            "is_vat_subject": False,
            "has_vat_000": False,
            "has_vat_021": False,
            "has_vat_055": False,
            "has_vat_100": False,
            "has_vat_200": False,
        }
        vals.update(extra_vals)
        wizard = self.ConsignorCreateWizard.create(vals)
        res = wizard.create_consignor()
        return self.ResPartner.browse(res["res_id"])

    def test_20_consignor_with_vat_creation_wizard(self):
        # Create consignor VAT Subject
        partner = self._create_consignor(
            {
                "is_vat_subject": True,
                "has_vat_055": True,
                "has_vat_200": True,
            }
        )

        # Check Results
        self.assertTrue(partner.is_consignor)
        self.assertEqual(partner.consignment_commission, 20)
        classifications = self.AccountProductFiscalClassification.search(
            [("consignor_partner_id", "=", partner.id)]
        )
        self.assertEqual(len(classifications), 2)

    def test_21_consignor_without_vat_creation_wizard_bad(self):
        # Create consignor not VAT Subject with bad configuration
        with self.assertRaises(ValidationError):
            self._create_consignor({})

    def test_22_consignor_without_vat_creation_wizard_good(self):
        # Create consignor not VAT Subject with correct configuration
        partner = self._create_consignor({"has_vat_000": True})

        # Check Results
        classifications = self.AccountProductFiscalClassification.search(
            [("consignor_partner_id", "=", partner.id)]
        )
        self.assertEqual(classifications[0].sale_tax_ids[0].amount, 0.0)
