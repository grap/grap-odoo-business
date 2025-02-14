# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_odoo_company = fields.Boolean(
        string="Is an Odoo Company",
        readonly=True,
        default=False,
        index=True,
    )

    # Overload Section
    @api.model
    def _get_hidden_elements(self):
        res = super()._get_hidden_elements()
        res += [
            {
                "name": "company",
                "model": "res.company",
                "partner_fields": ["partner_id"],
            }
        ]
        return res

    @api.model_create_multi
    def create(self, vals_list):
        if self.env.context.get("is_odoo_company"):
            for vals in vals_list:
                vals["is_odoo_company"] = True
        return super().create(vals_list)
