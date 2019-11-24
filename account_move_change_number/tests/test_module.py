# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestModule(TransactionCase):

    def setUp(self):
        super().setUp()
        self.invoice = self.env.ref('account_move_change_number.demo_invoice_1')
        self.move = self.invoice.move_id

    def test_01_rename_move(self):
        # Get sequence
        sequence = self.move.journal_id.sequence_id

        next_name = ("%s%s") % (
            self.move.name[:-sequence.padding],
            str(sequence.number_next_actual + 1).zfill(sequence.padding))

        self.move.rename_account_move_change_number()

        self.assertEqual(
            self.move.name, next_name,
            "Rename of Account Move failed.")

        self.assertEqual(
            self.invoice.number, next_name,
            "Rename of Account Invoice failed.")
