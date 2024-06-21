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
        cls.ResUsers = cls.env["res.users"]
        cls.demo_user = cls.env.ref("base.user_demo")
        cls.demo_partner = cls.env.ref("base.partner_demo")
        cls.main_company = cls.env.ref("base.main_company")
        cls.user_name = "technical_partner_access - res.users"

    def test_01_user_part(self):
        user = self.ResUsers.create(
            {
                "name": self.user_name,
                "login": "login@users_partners_access.com",
                "company_id": self.main_company.id,
            }
        )
        # check that partner has no company
        self.assertEqual(
            user.partner_id.company_id.id,
            False,
            "User's partner should not have company.",
        )

        # Check access without context (by search)
        result = self.ResPartner.search([("name", "=", self.user_name)])
        self.assertEqual(
            len(result),
            0,
            "Search user partner should not return result without context",
        )

        # Check access without context (by name_search)
        result = self.ResPartner.name_search(self.user_name)
        self.assertEqual(
            len(result),
            0,
            "Name Search user partner should not return result without context",
        )

        # Check access with context (by search)
        result = self.ResPartner.with_context(show_odoo_user=True).search(
            [("name", "=", self.user_name)]
        )
        self.assertEqual(
            len(result), 1, "Search user partner should return result with context"
        )

        # Check access with context (by name_search)
        result = self.ResPartner.with_context(show_odoo_user=True).name_search(
            self.user_name
        )
        self.assertEqual(
            len(result), 1, "Name Search user partner should return result with context"
        )

        # Without Correct access right, should fail
        with self.assertRaises(UserError):
            self.demo_partner.with_user(self.demo_user).write({"name": "Test"})

        # With Correct access right, should success
        self.demo_partner.write({"name": "Test"})
