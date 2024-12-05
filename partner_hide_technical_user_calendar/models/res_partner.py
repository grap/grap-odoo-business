# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def _compute_meeting(self):
        return super(
            ResPartner, self.with_context(show_odoo_user=True)
        )._compute_meeting()
