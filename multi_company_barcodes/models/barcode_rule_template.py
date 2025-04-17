# Copyright (C) 2020-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class BarcodeRuleTemplate(models.Model):
    _name = "barcode.rule.template"
    _inherit = "barcode.rule"

    barcode_nomenclature_id = fields.Many2one(
        comodel_name="barcode.nomenclature.template"
    )

    @api.multi
    def _prepare_rule(self):
        self.ensure_one()
        return {x: self[x] for x in ["name", "sequence", "type", "encoding", "pattern"]}
