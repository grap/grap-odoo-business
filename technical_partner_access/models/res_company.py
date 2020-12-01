# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import api, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    # Overload Section
    @api.model
    def create(self, vals):
        return super(
            ResCompany, self.with_context(is_odoo_company=True)
        ).create(vals)
