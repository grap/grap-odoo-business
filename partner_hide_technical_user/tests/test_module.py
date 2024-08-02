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
        cls.user_name = "technical_partner_access - res.users"
        cls.user = cls.ResUsers.create(
            {
                "name": cls.user_name,
                "login": "login@users_partners_access.com",
                "company_id": cls.env.ref("base.main_company").id,
            }
        )

    def test_01_search_partner(self):
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

    def test_02_write_on_partner_without_right(self):
        # Without Correct access right, write should fail
        with self.assertRaises(UserError):
            self.demo_partner.with_user(self.demo_user).write({"name": "Test"})

        # A user should have the possibility to write to his
        # related partner
        self.demo_user.with_user(self.demo_user).write({"tz": "Europe/Paris"})

    def test_03_write_on_partner_with_right(self):
        # With Correct access right, should success
        self.demo_partner.write({"name": "Test"})
