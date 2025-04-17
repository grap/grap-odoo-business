# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestModule(TransactionCase):
    """Tests for 'Product - Simple Pricelist' Module"""

    def setUp(self):
        super().setUp()
        self.ResCompany = self.env["res.company"]
        self.BarcodeNomenclature = self.env["barcode.nomenclature"]

    # Test Section
    def test_01_creat_company(self):
        company = self.ResCompany.create(
            {"name": "Demo Company (Multi Company Barcodes)"}
        )
        self.env.user.company_id = company.id
        nomenclatures = self.BarcodeNomenclature.search(
            [("company_id", "=", company.id)]
        )

        self.assertEqual(
            len(nomenclatures),
            1,
            "Create a new company should create a new nomenclature.",
        )

        rules = nomenclatures.rule_ids
        self.assertEqual(
            len(rules),
            1,
            "Create a new nomenclature based on template should create rules",
        )
