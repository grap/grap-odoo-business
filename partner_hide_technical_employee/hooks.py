# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import SUPERUSER_ID
from odoo.api import Environment


def post_init_hook(cr, pool):
    env = Environment(cr, SUPERUSER_ID, {})
    HrEmployee = env["hr.employee"]
    employees = HrEmployee.with_context(active_test=False).search([])
    employees.mapped("work_contact_id").write({"is_odoo_employee": True})
    employees.mapped("address_home_id").write({"is_odoo_employee": True})
