# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import api, models


class ResCompany(models.Model):
    _inherit = "res.company"

    @api.model_create_multi
    def create(self, vals_list):
        res = super(ResCompany, self.with_context(action_from_res_company=True)).create(
            vals_list
        )
        return res.with_context(action_from_res_company=False)

    def write(self, vals):
        return super(ResCompany, self.with_context(action_from_res_company=True)).write(
            vals
        )

    def unlink(self):
        return super(
            ResCompany, self.with_context(action_from_res_company=True)
        ).unlink()
