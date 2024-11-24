# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    label_ids = fields.Many2many(
        comodel_name="product.label",
        compute="_compute_label_ids",
        inverse="_inverse_label_ids",
        string="Labels",
        readonly=False,
    )

    @api.depends("product_variant_ids", "product_variant_ids.label_ids")
    def _compute_label_ids(self):
        for p in self:
            if len(p.product_variant_ids) == 1:
                p.label_ids = p.product_variant_ids.label_ids
            else:
                p.label_ids = False

    def _inverse_label_ids(self):
        for p in self:
            if len(p.product_variant_ids) == 1:
                p.product_variant_ids.label_ids = p.label_ids

    def _get_related_fields_variant_template(self):
        res = super()._get_related_fields_variant_template()
        res.append("label_ids")
        return res
