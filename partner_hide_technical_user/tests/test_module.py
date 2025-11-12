# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import Command
from odoo.exceptions import UserError
from odoo.tests.common import TransactionCase


class TestModule(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ResPartner = cls.env["res.partner"]
        cls.ResUsers = cls.env["res.users"]
        cls.demo_user = cls.env.ref("base.user_demo")
        cls.internal_user_name = "technical_partner_access - Internal User Name"
        cls.portal_user_name = "technical_partner_access - Portal User Name"
        cls.internal_group = cls.env.ref("base.group_user")
        cls.portal_group = cls.env.ref("base.group_portal")
        cls.new_internal_user = cls.ResUsers.create(
            {
                "name": cls.internal_user_name,
                "login": "internal@partner_hide_technical_user.com",
                "company_id": cls.env.ref("base.main_company").id,
                "groups_id": [Command.link(cls.internal_group.id)],
            }
        )
        cls.new_portal_user = cls.ResUsers.create(
            {
                "name": cls.portal_user_name,
                "login": "portal@partner_hide_technical_user.com",
                "company_id": cls.env.ref("base.main_company").id,
                "groups_id": [Command.link(cls.portal_group.id)],
            }
        )

    def test_00_check_is_odoo_user_computation(self):
        self.assertTrue(self.new_internal_user.partner_id.is_odoo_user)
        self.assertFalse(self.new_portal_user.partner_id.is_odoo_user)

    def test_01_search_internal_partner(self):
        # Check access without context (by search)
        result = self.ResPartner.search([("name", "=", self.internal_user_name)])
        self.assertEqual(
            len(result),
            0,
            "Search internal user partner should not return result without context",
        )

        # Check access without context (by name_search)
        result = self.ResPartner.name_search(self.internal_user_name)
        self.assertEqual(
            len(result),
            0,
            "Name Search internal user partner should not return result"
            " without context",
        )

        # Check access with context (by search)
        result = self.ResPartner.with_context(show_odoo_user=True).search(
            [("name", "=", self.internal_user_name)]
        )
        self.assertEqual(
            len(result),
            1,
            "Search internal user partner should return result with context",
        )

        # Check access with context (by name_search)
        result = self.ResPartner.with_context(show_odoo_user=True).name_search(
            self.internal_user_name
        )
        self.assertEqual(
            len(result),
            1,
            "Name Search internal user partner should return result with context",
        )

    def test_02_search_portal_partner(self):
        # Check access without context (by search)
        result = self.ResPartner.search([("name", "=", self.portal_user_name)])
        self.assertEqual(
            len(result),
            1,
            "Search portal user partner should return result without context",
        )

        # Check access without context (by name_search)
        result = self.ResPartner.name_search(self.portal_user_name)
        self.assertEqual(
            len(result),
            1,
            "Name Search portal user partner should return result without context",
        )

        # Check access with context (by search)
        result = self.ResPartner.with_context(show_odoo_user=True).search(
            [("name", "=", self.portal_user_name)]
        )
        self.assertEqual(
            len(result),
            1,
            "Search portal user partner should return result with context",
        )

        # Check access with context (by name_search)
        result = self.ResPartner.with_context(show_odoo_user=True).name_search(
            self.portal_user_name
        )
        self.assertEqual(
            len(result),
            1,
            "Name Search portal user partner should return result with context",
        )

    def test_04_write_on_partner_without_right(self):
        # Without Correct access right, write should fail on partner
        with self.assertRaises(UserError):
            self.new_internal_user.partner_id.with_user(self.demo_user).with_context(
                write_user_mode=True
            ).write({"name": "Test"})
        with self.assertRaises(UserError):
            self.new_internal_user.with_user(self.demo_user).with_context(
                write_user_mode=True
            ).write({"name": "Test"})

        # A user should have the possibility to write to his
        # related partner
        self.demo_user.partner_id.with_user(self.demo_user).with_context(
            write_user_mode=True
        ).write({"tz": "Europe/Paris"})

        # A user should have the possibility to write on its user
        self.demo_user.with_user(self.demo_user).with_context(
            write_user_mode=True
        ).write({"name": "New User Name"})

    def _test_05_write_on_partner_with_right(self):
        # With Correct access right, should success
        self.new_internal_user.partner_id.write({"name": "Test"})
        self.new_internal_user.write({"name": "Test"})
