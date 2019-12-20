# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    label_ids = fields.Many2many(
        comodel_name="product.label",
        relation="product_label_product_rel",
        column1="product_id",
        column2="label_id",
        string="Labels",
    )
