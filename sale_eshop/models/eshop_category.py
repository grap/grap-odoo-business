# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models, tools
from odoo.exceptions import Warning as UserError


class EshopCategory(models.Model):
    _name = "eshop.category"
    _inherit = ["eshop.with.image.mixin", "image.mixin"]
    _rec_name = "complete_name"
    _order = "sequence, complete_name"
    _description = "Eshop category"

    # Inherit Section
    _eshop_invalidation_type = "single"

    _eshop_fields = [
        "name",
        "available_product_qty",
        "child_qty",
        "image_512",
        "type",
        "parent_id",
        "product_ids",
        "complete_name",
    ]

    _eshop_image_fields = ["image_1920", "image_512", "image_128"]

    _TYPE_SELECTION = [
        ("view", "View"),
        ("normal", "Normal"),
    ]

    # Columns Section
    name = fields.Char(string="Name", required=True, index=True)

    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        index=True,
        required=True,
        default=lambda s: s._default_company_id(),
    )

    sequence = fields.Integer(string="Sequence", required=True, default=1)

    complete_name = fields.Char(
        string="Complete Name",
        store=True,
        recursive=True,
        compute="_compute_complete_name",
    )

    image_1920 = fields.Image(string="Image", max_width=1920, max_height=1920, store=True)

    image_512 = fields.Image(string="Medium-sized image", max_width=512, max_height=512, store=True)

    image_128 = fields.Image(string="Small-sized image", max_width=128, max_height=128, store=True)

    parent_id = fields.Many2one(
        comodel_name="eshop.category",
        string="Parent Category",
        index=True,
        domain="[('type', '=', 'view')]",
    )

    child_ids = fields.One2many(
        comodel_name="eshop.category",
        inverse_name="parent_id",
        string="Child Categories",
        readonly=True,
    )

    type = fields.Selection(
        selection=_TYPE_SELECTION,
        string="Category Type",
        required=True,
        default="normal",
        help="A category of the view type is a virtual category that"
        " can be used as the parent of another category to create a"
        " hierarchical structure.",
    )

    product_ids = fields.One2many(
        comodel_name="product.product",
        inverse_name="eshop_category_id",
        string="Products",
        readonly=True,
    )

    child_qty = fields.Integer(string="Childs Quantity", compute="_compute_multi_child")

    product_qty = fields.Integer(
        string="Products Quantity", compute="_compute_multi_child"
    )

    available_product_ids = fields.One2many(
        string="Available Products",
        compute="_compute_multi_child",
        comodel_name="product.product",
    )

    available_product_qty = fields.Integer(
        string="Available Products Quantity",
        compute="_compute_multi_child",
        comodel_name="product.product",
    )

    # Default Section
    @api.model
    def _default_company_id(self):
        return self.env.company.id

    # Constraints Section
    @api.constrains("type", "product_ids", "child_ids")
    def _check_type(self):
        for category in self:
            if category.type == "view" and category.product_qty > 0:
                raise UserError(_("A 'view' Category can not belongs products"))
            elif category.type == "normal" and len(category.child_ids) > 0:
                raise UserError(
                    _("A 'normal' Category can not belongs childs categories")
                )

    # Compute Section
    @api.depends("name", "parent_id.complete_name")
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = _("%s / %s") % (
                    category.parent_id.complete_name,
                    category.name,
                )
            else:
                category.complete_name = category.name

    @api.depends("product_ids", "child_ids")
    def _compute_multi_child(self):
        for category in self:
            available_products = category.product_ids.filtered(
                lambda x: x.eshop_state == "available"
            )
            category.product_qty = len(category.product_ids)
            category.available_product_ids = available_products
            category.available_product_qty = len(available_products)
            category.child_qty = len(category.child_ids)

    # Name Function
    @api.model
    def name_search(self, name, args=None, operator="ilike", limit=100):
        recs = self.search([("complete_name", operator, name)] + args, limit=limit)
        return recs.name_get()

    @api.depends("complete_name")
    def name_get(self):
        res = []
        for category in self:
            res.append((category.id, category.complete_name))
        return res
