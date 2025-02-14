# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import api, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.model_create_multi
    def create(self, vals_list):
        partners = super(
            HrEmployee,
            self.with_context(create_hr_employee=True),
        ).create(vals_list)
        partners._hide_address_home_partners()
        return partners

    def write(self, vals):
        res = super().write(vals)
        if vals.get("address_home_id"):
            self._hide_address_home_partners()
        return res

    def _hide_address_home_partners(self):
        partners = self.mapped("address_home_id").filtered(
            lambda x: not x.is_odoo_employee
        )
        if partners:
            partners.write({"is_odoo_employee": True})
