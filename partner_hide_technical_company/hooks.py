# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import SUPERUSER_ID
from odoo.api import Environment


def post_init_hook(cr, pool):
    env = Environment(cr, SUPERUSER_ID, {})
    ResCompany = env["res.company"]
    companies = ResCompany.with_context(active_test=False).search([])
    companies.mapped("partner_id").with_context(action_from_res_company=True).write(
        {"is_odoo_company": True}
    )
