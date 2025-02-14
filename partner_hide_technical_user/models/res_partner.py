# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_odoo_user = fields.Boolean(
        string="Is an Odoo User",
        readonly=True,
        default=False,
        index=True,
    )

    # Overload Section
    @api.model
    def _get_hidden_elements(self):
        res = super()._get_hidden_elements()
        res += [
            {"name": "user", "model": "res.users", "partner_fields": ["partner_id"]}
        ]
        return res

    # Custom section
    @api.model
    def _check_technical_partner_derogation(self, model_name, items):
        result = super()._check_technical_partner_derogation(model_name, items)
        if not result and model_name == "res.users":
            return items.ids == self.env.user.ids and self.env.context.get(
                "write_user_mode", False
            )
        return result
