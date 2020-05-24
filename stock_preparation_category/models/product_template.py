# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    preparation_categ_id = fields.Many2one(
        comodel_name="stock.preparation.category",
        string="Preparation Category",
        related="product_variant_ids.preparation_categ_id",
        readonly=False,
    )
