# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from dateutil.relativedelta import relativedelta

from odoo.fields import Datetime
from odoo.tests.common import TransactionCase


class TestShippingCost(TransactionCase):
    def setUp(self):
        super().setUp()
        self.moment_group = self.env.ref("sale_recovery_moment.recovery_moment_group_1")
        self.moment = self.env.ref("sale_recovery_moment.recovery_moment_1")

    def _check_state(self, item, state):
        self.assertEqual(item.state, state)

        res = item.search([("state", "=", state)])
        self.assertIn(item.id, res.ids)

    def _change_date_and_check(self, item):
        item.write(
            {
                "min_sale_date": Datetime.now() + relativedelta(days=2),
                "max_sale_date": Datetime.now() + relativedelta(days=3),
                "min_recovery_date": Datetime.now() + relativedelta(days=4),
                "max_recovery_date": Datetime.now() + relativedelta(days=5),
            }
        )
        self._check_state(item, "futur")

        item.write({"min_sale_date": Datetime.now() + relativedelta(days=-5)})
        self._check_state(item, "pending_sale")

        item.write({"max_sale_date": Datetime.now() + relativedelta(days=-4)})
        self._check_state(item, "finished_sale")

        item.write({"min_recovery_date": Datetime.now() + relativedelta(days=-3)})
        self._check_state(item, "pending_recovery")

        item.write({"max_recovery_date": Datetime.now() + relativedelta(days=-2)})
        self._check_state(item, "finished_recovery")

    def test_01_change_date_moment(self):
        self._change_date_and_check(self.moment)

    def test_02_change_date_moment_group(self):
        self._change_date_and_check(self.moment_group)
