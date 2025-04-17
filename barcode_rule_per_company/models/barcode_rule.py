# Copyright (C) 2020-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class Barcoderule(models.Model):
    _inherit = "barcode.rule"

    company_id = fields.Many2one(
        comodel_name="res.company", default=lambda x: x._default_company_id()
    )

    def _default_company_id(self):
        if self.env.context.get("created_by_ui"):
            return self.env.company
