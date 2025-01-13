# Copyright (C) 2022 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT (quentin.dupont@grap.coop)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class MrpBom(models.Model):
    _inherit = "mrp.bom"

    bom_allergen_ids = fields.Many2many(
        string="Allergens",
        comodel_name="product.allergen",
        help="Includes allergens of the product and its components",
        compute="_compute_bom_allergen_ids",
        store=True,
    )

    @api.depends(
        "product_tmpl_id", "product_tmpl_id.allergen_ids", "bom_line_ids.allergen_ids"
    )
    def _compute_bom_allergen_ids(self):
        for bom in self:
            # list(set()) removes duplication
            bom.bom_allergen_ids = [
                (
                    6,
                    0,
                    list(
                        set(
                            bom.product_tmpl_id.allergen_ids.ids
                            + [
                                x.id
                                for bom_line in bom.bom_line_ids
                                for x in bom_line.product_id.allergen_ids
                            ]
                        )
                    ),
                )
            ]
