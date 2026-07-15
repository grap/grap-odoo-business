# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def _compute_meeting(self):
        element_names = [element["name"] for element in self._get_hidden_elements()]
        contextual_env = self
        if "user" in element_names:
            contextual_env = contextual_env.with_context(show_odoo_user=True)
        if "company" in element_names:
            contextual_env = contextual_env.with_context(show_odoo_company=True)
        if "employee" in element_names:
            contextual_env = contextual_env.with_context(show_odoo_employee=True)
        return super(ResPartner, contextual_env)._compute_meeting()
