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
        cls.HrEmployee = cls.env["hr.employee"]
        cls.demo_user = cls.env.ref("base.user_demo")
        cls.demo_partner = cls.env.ref("base.partner_demo")
        cls.employee_name = "technical_partner_access"
        cls.employee = cls.HrEmployee.create(
            {
                "name": "technical_partner_access - work_contact_id",
                # To create the work_contact_id
                "work_email": "TEST@TEST.com",
            }
        )
        cls.employee_partner = cls.employee.work_contact_id
        cls.employee.address_home_id = cls.ResPartner.create(
            {
                "name": "technical_partner_access - address_home_id",
            }
        )

    def test_01_search_partner(self):
        # Check access without context (by search)
        result = self.ResPartner.search([("name", "ilike", self.employee_name)])
        self.assertEqual(
            len(result),
            0,
            "'search' employee partner should not return result without context",
        )

        # Check access without context (by name_search)
        result = self.ResPartner.name_search(self.employee_name)
        self.assertEqual(
            len(result),
            0,
            "'name_search' employee partner should not return result without context",
        )

        # Check access with context (by search)
        result = self.ResPartner.with_context(show_odoo_employee=True).search(
            [("name", "ilike", self.employee_name)]
        )
        self.assertEqual(
            len(result),
            2,
            "'search' employee partners should return result with context",
        )

        # Check access with context (by name_search)
        result = self.ResPartner.with_context(show_odoo_employee=True).name_search(
            self.employee_name
        )
        self.assertEqual(
            len(result),
            2,
            "'name_search' employee partners should return result with context",
        )

    def test_02_write_on_partner_without_right(self):
        # Without Correct access right, write should fail
        self.demo_user.write(
            {
                "groups_id": [
                    Command.unlink(self.env.ref("hr.group_hr_manager").id),
                    Command.unlink(self.env.ref("hr.group_hr_user").id),
                ]
            }
        )
        with self.assertRaises(UserError):
            self.employee_partner.with_user(self.demo_user).write({"name": "Test"})

    def test_03_write_on_partner_with_right(self):
        # With Correct access right, should success
        self.employee_partner.write({"name": "Test"})
