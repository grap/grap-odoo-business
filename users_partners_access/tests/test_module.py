# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase
from odoo.exceptions import Warning as UserError


class TestModule(TransactionCase):

    def setUp(self):
        super().setUp()
        self.ResUsers = self.env['res.users']
        self.demo_user = self.env.ref('base.user_demo')
        self.demo_partner = self.env.ref('base.partner_demo')

    def test_01_create_user(self):
        user = self.ResUsers.create({
            'customer': True,
            'supplier': True,
            'name': 'Users Partners Access Test',
            'login': 'login@users_partners_access.com',
        })
        self.assertEqual(
            user.partner_id.customer, False,
            "User's partner should be customer.")
        self.assertEqual(
            user.partner_id.supplier, False,
            "User's partner should not be supplier.")

    def test_02_check_access_right(self):
        # Without Correct access right, should fail
        with self.assertRaises(UserError):
            self.demo_partner.sudo(self.demo_user).write({
                'name': 'Test',
            })

        # With Correct access right, should success
        self.demo_partner.write({
            'name': 'Test',
        })
