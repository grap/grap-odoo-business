# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import datetime

from odoo.tests.common import TransactionCase


class TestModule(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ResCompany = cls.env["res.company"]
        cls.AccountConfigSettings = cls.env["account.config.settings"].with_user(
            cls.env.ref("base.user_demo")
        )
        cls.main_company = cls.env.ref("base.main_company")

    def test_configure_demo_user(self):
        # with Form(invoice) as
        config = self.AccountConfigSettings.create({})
        self.assertEqual(config.period_lock_date, self.main_company.period_lock_date)

        new_date = datetime.date(2000, 1, 1)
        config.write({"period_lock_date": new_date})
        config.execute()
        self.assertEqual(self.main_company.period_lock_date, new_date)
