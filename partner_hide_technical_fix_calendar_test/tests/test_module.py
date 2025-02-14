# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestModule(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.employee = cls.env.ref("hr.employee_hne")

    def test_no_error_employee(self):
        self.employee.work_contact_id._compute_meeting()

    def test_no_error_company(self):
        self.env.company.partner_id._compute_meeting()

    def test_no_error_user(self):
        self.env.user.partner_id._compute_meeting()
