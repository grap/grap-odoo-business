# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import api, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.model_create_multi
    def create(self, vals_list):
        return super(
            HrEmployee,
            self.with_context(show_odoo_employee=True, create_hr_employee=True),
        ).create(vals_list)
