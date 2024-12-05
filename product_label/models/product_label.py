# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductLabel(models.Model):
    _name = "product.label"
    _inherit = ["image.mixin"]
    _description = "Product Labels"

    # Columns Section
    code = fields.Char(required=True)

    name = fields.Char(required=True)

    active = fields.Boolean(default=True)

    company_id = fields.Many2one(comodel_name="res.company", string="Company")

    website = fields.Char()

    note = fields.Text()

    display_on_report = fields.Boolean(
        string="Display on Reports",
        help="By checking this field, the label will be printed on"
        " all the official documents.",
    )

    product_ids = fields.Many2many(
        comodel_name="product.product",
        relation="product_label_product_rel",
        column1="label_id",
        column2="product_id",
        string="Products",
    )

    product_qty = fields.Integer(
        string="Product Quantity", compute="_compute_product_qty"
    )

    @api.depends("product_ids")
    def _compute_product_qty(self):
        for label in self:
            label.product_qty = len(label.product_ids)
