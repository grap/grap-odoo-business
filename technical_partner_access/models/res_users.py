# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import api, models


class ResUsers(models.Model):
    _inherit = "res.users"

    # Overload Section
    @api.model
    def create(self, vals):
        vals.update({"is_odoo_user": True})
        user = super().create(vals)
        user.partner_id.write(
            {
                "company_id": False,
            }
        )
        return user
