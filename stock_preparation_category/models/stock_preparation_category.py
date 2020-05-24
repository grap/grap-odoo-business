# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class StockPreparationCategory(models.Model):
    _name = "stock.preparation.category"
    _description = "Preparation Categories"
    _order = "sequence, name"

    # Column Section
    name = fields.Char(string="Name", required=True)

    sequence = fields.Integer(string="Sequence", required=True)

    code = fields.Char(
        string="Code", required=True,
        help="This field will be used on the picking reports")

    color = fields.Char(string="Color", required=True, default="#FFFFFF")

    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        default=lambda x: x._default_company_id(),
    )

    active = fields.Boolean(string="Active", default=True)

    product_ids = fields.One2many(
        comodel_name="product.product",
        inverse_name="preparation_categ_id",
        string="Products",
    )

    product_qty = fields.Integer(
        compute="_compute_product_qty",
        string="Product Quantity"
    )

    # Default Section
    @api.model
    def _default_company_id(self):
        return self.env.user.company_id.id

    # Compute Section
    @api.depends("product_ids.preparation_categ_id")
    def _compute_product_qty(self):
        for category in self:
            category.product_qty = len(category.product_ids)
