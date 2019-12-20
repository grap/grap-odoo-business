# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, tools


class ProductLabel(models.Model):
    _name = "product.label"
    _description = "Product Labels"

    # Columns Section
    code = fields.Char(string="Code", required=True)

    name = fields.Char(string="Name", required=True)

    active = fields.Boolean(string="Active", default=True)

    company_id = fields.Many2one(comodel_name="res.company", string="Company")

    website = fields.Char(string="Website")

    note = fields.Text(string="Note")

    display_on_invoice = fields.Boolean(
        string="Display on Invoices",
        help="By checking this field, the label will be printed on"
        " all the invoices.",
    )

    product_ids = fields.Many2many(
        comodel_name="product.product",
        relation="product_label_product_rel",
        column1="label_id",
        column2="product_id",
        string="Products",
    )

    product_qty = fields.Integer(
        string="Product Quantity", compute="_compute_product_qty")

    image = fields.Binary(string="Image", attachment=True)

    image_medium = fields.Binary(string="Medium-sized image", attachment=True)

    image_small = fields.Binary(string="Small-sized image", attachment=True)

    @api.multi
    @api.depends("product_ids")
    def _compute_product_qty(self):
        for label in self:
            label.product_qty = len(label.product_ids)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            tools.image_resize_images(vals, sizes={'image': (1024, None)})
        return super().create(vals_list)

    @api.multi
    def write(self, vals):
        tools.image_resize_images(vals, sizes={'image': (1024, None)})
        return super().write(vals)
