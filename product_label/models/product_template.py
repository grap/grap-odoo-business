# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    label_ids = fields.Many2many(
        string="Labels",
        comodel_name="product.label",
        compute=lambda x: x._compute_template_field_from_variant_field("label_ids"),
        inverse=lambda x: x._set_product_variant_field("label_ids"),
        readonly=False,
    )

    def _get_related_fields_variant_template(self):
        res = super()._get_related_fields_variant_template()
        res.append("label_ids")
        return res
