# coding: utf-8
# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestModule(TransactionCase):

    def setUp(self):
        super().setUp()
        self.ScaleLog = self.env["product.scale.log"]
        self.salad_product = self.env.ref("product_to_scale_bizerba.salad")
        self.apple_product = self.env.ref("product_to_scale_bizerba.apple")
        self.vegetable_scale_group = self.env.ref(
            "product_to_scale_bizerba.demo_scale_group_vegetables")
        self.initial_log_ids = self.ScaleLog.search([]).ids

    def test_01_generate_create_log(self):
        self.salad_product.scale_group_id = self.vegetable_scale_group.id
        new_logs = self.ScaleLog.search([
            ('id', 'not in', self.initial_log_ids)
        ])
        self.assertEqual(
            len(new_logs), 1,
            "set a scale group to a product should generate a new log"
        )
        new_log = new_logs[0]
        self.assertEqual(
            new_log.action, "create",
            "The log should be a 'creation' log.")

    def test_02_generate_delete_log(self):
        self.apple_product.scale_group_id = False
        new_logs = self.ScaleLog.search([
            ('id', 'not in', self.initial_log_ids)
        ])
        self.assertEqual(
            len(new_logs), 1,
            "Remove a scale group to a product should generate a new log"
        )
        new_log = new_logs[0]
        self.assertEqual(
            new_log.action, "unlink",
            "The log should be a 'deletion' log.")
