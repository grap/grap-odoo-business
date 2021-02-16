# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.exceptions import Warning as UserError
from odoo.tests.common import TransactionCase


class TestModule(TransactionCase):

    def setUp(self):
        super().setUp()
        self.ResPartner = self.env['res.partner']
        self.ResUsers = self.env['res.users']
        self.ResCompany = self.env['res.company']
        self.demo_user = self.env.ref('base.user_demo')
        self.demo_partner = self.env.ref('base.partner_demo')
        self.main_company = self.env.ref("base.main_company")
        self.user_name = 'technical_partner_access - res.users'
        self.company_name = 'Users technical_partner_access - res.company'

    def test_01_user_part(self):
        user = self.ResUsers.create({
            'name': self.user_name,
            'login': 'login@users_partners_access.com',
            'company_id': self.main_company.id,
        })
        # check that partner has no company
        self.assertEqual(
            user.partner_id.company_id.id, False,
            "User's partner should not have company.")

        # Check access without context
        result = self.ResPartner.search([('name', '=', self.user_name)])
        self.assertEqual(
            len(result), 0,
            "Search user partner should not return result without context")

        # Check access with context
        result = self.ResPartner.with_context(show_odoo_user=True).search(
            [('name', '=', self.user_name)])
        self.assertEqual(
            len(result), 1,
            "Search user partner should return result with context")

        # Without Correct access right, should fail
        with self.assertRaises(UserError):
            self.demo_partner.sudo(self.demo_user).write({
                'name': 'Test',
            })

        # With Correct access right, should success
        self.demo_partner.write({
            'name': 'Test',
        })

    def test_02_company_part(self):
        company = self.ResCompany.create({
            'name': self.company_name,
        })
        # Check access without context
        result = self.ResPartner.search([('name', '=', self.company_name)])
        self.assertEqual(
            len(result), 0,
            "Search company partner should not return result without context")

        # Check access with context
        result = self.ResPartner.with_context(show_odoo_company=True).search(
            [('name', '=', self.company_name)])
        self.assertEqual(
            len(result), 1,
            "Search company partner should return result with context")

        # Without Correct access right, should fail
        with self.assertRaises(UserError):
            company.partner_id.sudo(self.demo_user).write({
                'name': 'Test',
            })

        # With Correct access right, should success
        company.partner_id.write({
            'name': 'Test',
        })
