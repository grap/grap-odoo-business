# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models


class HrEmployeeBase(models.AbstractModel):
    _inherit = "hr.employee.base"

    def _inverse_work_contact_details(self):
        return super(
            HrEmployeeBase,
            self.with_context(create_employee=True),
        )._inverse_work_contact_details()
