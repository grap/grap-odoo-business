# Copyright (C) 2020-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models


class BarcodeNomenclatureTemplate(models.Model):
    _name = "barcode.nomenclature.template"
    _inherit = "barcode.nomenclature"

    rule_ids = fields.One2many(comodel_name="barcode.rule.template")

    company_id = fields.Many2one(default=False)

    @api.multi
    def _prepare_nomenclature(self, company):
        self.ensure_one()
        vals = {
            "name": _("Nomenclature of {}").format(company.name),
            "company_id": company.id,
            "upc_ean_conv": self.upc_ean_conv,
            "rule_ids": [],
        }
        for rule_template in self.rule_ids:
            vals["rule_ids"].append((0, 0, rule_template._prepare_rule()))
        return vals
