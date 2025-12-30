# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestModule(TransactionCase):
    def setUp(self):
        super().setUp()
        self.move = self.env.ref("account_move_change_number.demo_move_1")

    # Check that new name is actual_name + 1 at the end
    def test_01_rename_move(self):
        self.move.action_post()
        self.assertEqual(self.move.state, "posted", "Initial Move name is not posted.")

        sequence = self.move.journal_id.sequence_id
        next_name = ("%s%s") % (
            self.move.name[: -sequence.padding],
            str(sequence.number_next_actual + 1).zfill(sequence.padding),
        )

        self.move.rename_account_move_change_number()
        self.assertEqual(self.move.name, next_name, "Rename of Account Move failed.")