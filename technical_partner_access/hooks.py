# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import SUPERUSER_ID
from odoo.api import Environment


def post_init_hook(cr, pool):
    env = Environment(cr, SUPERUSER_ID, {})
    ResUsers = env["res.users"]
    ResCompany = env["res.company"]
    users = ResUsers.with_context(active_test=False).search([])
    users.mapped("partner_id").write({"is_odoo_user": True})
    companies = ResCompany.with_context(active_test=False).search([])
    companies.mapped("partner_id").write({"is_odoo_company": True})
