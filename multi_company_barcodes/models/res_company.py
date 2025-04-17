# Copyright (C) 2020-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    nomenclature_id = fields.Many2one(default=False)

    @api.model
    def create(self, vals):
        company = super().create(vals)
        if not company.nomenclature_id:
            template = self.env["barcode.nomenclature.template"].search([], limit=1)
            if template:
                company.nomenclature_id = (
                    self.env["barcode.nomenclature"]
                    .sudo()
                    .create(template._prepare_nomenclature(company))
                    .id
                )
        return company
