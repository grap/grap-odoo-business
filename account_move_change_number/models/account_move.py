# Copyright (C) 2013 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from datetime import datetime

from odoo import _, api, models


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.multi
    def rename_account_move_change_number(self):
        for move in self:
            old_name = move.name
            old_narration = move.narration or ""

            # unpost acount move
            move.button_cancel()

            # set name to "/"
            move.name = "/"

            # Get related invoice
            invoices = self.env["account.invoice"].search(
                [('move_id', "=", move.id)]
            )
            if invoices:
                invoice = invoices[0]
                invoice.move_name = "/"
            else:
                invoice = False

            # post account move
            move.post(invoice=invoice)
            new_name = move.name

            # Add description of the change
            date = datetime.today().strftime("%d/%m/%Y")
            author_name = self.env.user.name
            move.narration = old_narration + _(
                "\nAccount move renamed. Old name : %s."
                " New name : %s. Rename date : %s. Author : %s."
            ) % (old_name, new_name, date, author_name)
        return True
