# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.exceptions import UserError
from odoo.tests.common import TransactionCase


class TestModule(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ResPartner = cls.env["res.partner"]
        cls.ResCompany = cls.env["res.company"]
        cls.demo_user = cls.env.ref("base.user_demo")
        cls.main_company = cls.env.ref("base.main_company")
        cls.company_name = "Users technical_partner_access - res.company"

    def test_01_company_part(self):
        company = self.ResCompany.create({"name": self.company_name})
        # Check access without context (by search)
        result = self.ResPartner.search([("name", "=", self.company_name)])
        self.assertEqual(
            len(result),
            0,
            "Search company partner should not return result without context",
        )
        # Check access without context (by name_search)
        result = self.ResPartner.name_search(self.company_name)
        self.assertEqual(
            len(result),
            0,
            "Name Search company partner should not return result without context",
        )

        # Check access with context (by search)
        result = self.ResPartner.with_context(show_odoo_company=True).search(
            [("name", "=", self.company_name)]
        )
        self.assertEqual(
            len(result), 1, "Search company partner should return result with context"
        )
        # Check access with context (by name_search)
        result = self.ResPartner.with_context(show_odoo_company=True).name_search(
            self.company_name
        )
        self.assertEqual(
            len(result),
            1,
            "Name Search company partner should return result with context",
        )

        # Without Correct access right, should fail
        with self.assertRaises(UserError):
            company.partner_id.with_user(self.demo_user).write({"name": "Test"})

        # With Correct access right, should success
        company.partner_id.write({"name": "Test"})
