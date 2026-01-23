# Copyright 2021 - Today Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestModule(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.HrEmployee = cls.env["hr.employee"]
        cls.ResPartner = cls.env["res.partner"]
        cls.employee = cls.HrEmployee.create(
            {
                "name": "Employee Name",
                "address_home_email": "hr_direct@address_home.com",
            }
        )

    def test_computation(self):
        self.employee.address_home_email = "hr_direct@address_home.com2"
        self.assertEqual(
            self.employee.address_home_id.email, "hr_direct@address_home.com2"
        )
        self.employee.address_home_id.email = "hr_direct@address_home.com3"
        self.assertEqual(
            self.employee.address_home_email, "hr_direct@address_home.com3"
        )

    def test_copy(self):
        new_employee = self.employee.copy()
        self.assertTrue(new_employee.address_home_id)
        self.assertNotEqual(new_employee.address_home_id, self.employee.address_home_id)
