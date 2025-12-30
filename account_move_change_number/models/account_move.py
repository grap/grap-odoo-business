# Copyright (C) 2013 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from datetime import datetime

from odoo import _, models


class AccountMove(models.Model):
    _inherit = "account.move"

    def rename_account_move_change_number(self):
        for move in self:
            old_name = move.name
            old_narration = move.narration or ""

            move.button_cancel()
            # need to reset name to trigger new name
            move.name = "/"
            move.action_post()

            # Add description of the change
            move.narration = old_narration + _(
                "\nAccount move renamed. Old name : %(oldname)s."
                " New name : %(newname)s. Rename date : %(renamedate)s."
                " Author : %(author)s.",
                oldname=old_name,
                newname=move.name,
                renamedate=datetime.today().strftime("%d/%m/%Y"),
                author=self.env.user.name,
            )
        return True
