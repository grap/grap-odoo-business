# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from datetime import datetime

from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError


class ProductProduct(models.Model):
    _name = "product.product"
    _inherit = ["product.product", "eshop.with.image.mixin"]

    # Inherit Section
    _eshop_invalidation_type = "single"

    _eshop_fields = [
        "name",
        "uom_id",
        "image_1920",
        "image_512",
        "list_price",
        "list_price_vat_excl",
        "eshop_category_id",
        "label_ids",
        "eshop_minimum_qty",
        "eshop_rounded_qty",
        "maker_description",
        "eshop_description",
        "country_id",
        "state_id",
        "department_id",
        "default_code",
        "eshop_taxes_description",
    ]

    _eshop_image_fields = ["image_1920", "image_512", "image_128"]

    _ESHOP_STATE_SELECTION = [
        ("available", "Available for Sale"),
        ("disabled", "Temporarily Disabled"),
        ("unavailable", "Unavailable for Sale"),
    ]

    eshop_category_id = fields.Many2one(
        comodel_name="eshop.category",
        string="eShop Category",
        domain=[("type", "=", "normal")],
    )

    eshop_start_date = fields.Date(string="Start Date of Sale")

    eshop_end_date = fields.Date(string="End Date of Sale")

    eshop_state = fields.Selection(
        string="eShop State",
        selection=_ESHOP_STATE_SELECTION,
        compute="_compute_eshop_state",
        search="_search_eshop_state",
    )

    eshop_minimum_qty = fields.Float(
        string="Minimum Quantity for eShop", required=True, default=0
    )

    eshop_rounded_qty = fields.Float(
        string="Rounded Quantity for eShop", required=True, default=0
    )

    eshop_description = fields.Text(type="Text", string="Eshop Description")

    eshop_taxes_description = fields.Char(
        compute="_compute_eshop_taxes_description",
        string="Eshop Taxes Description",
    )

    # Compute Section
    @api.depends("taxes_id.description")
    def _compute_eshop_taxes_description(self):
        for product in self:
            product.eshop_taxes_description = ", ".join(
                product.mapped("taxes_id.description")
            )

    @api.depends(
        "eshop_category_id",
        "sale_ok",
        "active",
        "eshop_start_date",
        "eshop_end_date",
    )
    def _compute_eshop_state(self):
        for product in self:
            if not (product.eshop_category_id and product.sale_ok and product.active):
                product.eshop_state = "unavailable"
            else:
                dateNow = fields.date.today()
                if product.eshop_start_date and product.eshop_end_date:
                    if (
                        product.eshop_start_date <= dateNow
                        and dateNow <= product.eshop_end_date
                    ):
                        product.eshop_state = "available"
                    else:
                        product.eshop_state = "disabled"
                elif product.eshop_start_date:
                    if product.eshop_start_date <= dateNow:
                        product.eshop_state = "available"
                    else:
                        product.eshop_state = "disabled"
                elif product.eshop_end_date:
                    if dateNow <= product.eshop_end_date:
                        product.eshop_state = "available"
                    else:
                        product.eshop_state = "disabled"
                else:
                    product.eshop_state = "available"

    # API eshop Section
    @api.model
    def get_current_eshop_product_list(self, partner_id=False):
        SaleOrder = self.env["sale.order"]
        order = SaleOrder.eshop_get_current_sale_order(partner_id)
        line_dict = {}
        if order:
            for line in order.order_line:
                line_dict[line.product_id.id] = {
                    "qty": line.product_uom_qty,
                    "discount": line.discount,
                }

        today = fields.Date.context_today(self)
        Product = self.env['product.product']
        products = Product.search([
            ('active', '=', True),
            ('product_tmpl_id.sale_ok', '=', True),
            ('product_tmpl_id.company_id', '=', self.env.company.id),
            '|', ('eshop_start_date', '=', False),
                 ('eshop_start_date', '<=', today),
            '|', ('eshop_end_date', '=', False),
                 ('eshop_end_date', '>=', today),
        ])

        res = []
        for product in products:
            tmpl = product.product_tmpl_id
            category = product.eshop_category_id
            tax_ids = tmpl.taxes_id.ids
            label_ids = product.label_ids.ids if hasattr(product, 'label_ids') else []
            data = {
                "id": product.id,
                "template_id": tmpl.id,
                "default_code": product.default_code or False,
                "name": tmpl.name,
                "list_price": tmpl.list_price,
                "list_price_vat_excl": product.list_price_vat_excl,
                "category_id": category.id,
                "category_sequence": category.sequence,
                "category_name": category.name,
                "category_complete_name": category.complete_name,
                "category_image_write_date": category.image_512 and category.write_date,
                "category_image_write_date_hash": category.image_512 and hash(category.write_date),
                "product_image_write_date": product.image_512 and product.write_date,
                "product_image_write_date_hash": product.image_512 and hash(product.write_date),
                "uom_id": tmpl.uom_id.id,
                "uom_eshop_description": tmpl.uom_id.eshop_description,
                "eshop_minimum_qty": product.eshop_minimum_qty,
                "tax_ids": sorted(tax_ids),
                "label_ids": sorted(label_ids),
                "qty": 0,
                "discount": 0,
            }
            if product.id in line_dict:
                data["qty"] = line_dict[product.id]["qty"]
                data["discount"] = line_dict[product.id]["discount"]

            res.append(data)

        res.sort(key=lambda x: (x["category_sequence"], x["category_name"], x["name"]))
        return res

    def _search_eshop_state(self, operator, value):
        dateNow = datetime.now().strftime("%Y-%m-%d")
        if operator not in ("=", "in"):
            raise UserError(_("The Operator %s is not implemented !" % (operator)))
        if operator == "=":
            lst = [value]
        else:
            lst = value
        sql_lst = []
        if "available" in lst and len(lst) == 1:
            sql_lst.append(
                """((
                        eshop_start_date is not null
                        AND eshop_end_date is not null)
                    AND (
                        eshop_start_date <= '%s'
                        AND '%s' <= eshop_end_date
                    )
                )"""
                % (dateNow, dateNow)
            )
            sql_lst.append(
                """((
                        eshop_start_date is null
                        AND eshop_end_date is not null)
                    AND ('%s' <= eshop_end_date)
                )"""
                % (dateNow)
            )
            sql_lst.append(
                """((
                        eshop_start_date is not null
                        AND eshop_end_date is null)
                    AND (
                        eshop_start_date <= '%s'
                    )
                )"""
                % (dateNow)
            )
            sql_lst.append(
                """(eshop_start_date is null
                    AND eshop_end_date is null)"""
            )
            for i in range(0, len(sql_lst)):
                sql_lst[i] = """(
                    eshop_category_id IS NOT NULL
                    AND id in (
                        SELECT pp.id
                        FROM product_product pp
                        INNER JOIN product_template pt
                            ON pp.product_tmpl_id = pt.id
                            AND pt.sale_ok is true)
                    AND active is true
                    AND (%s))""" % (sql_lst[i])
        else:
            raise UserError(_("This arg %s is not implemented !" % (value)))

        where = sql_lst[0]
        for item in sql_lst[1:]:
            where += " OR %s" % (item)
        sql_req = "SELECT id FROM product_product"
        sql_req += " WHERE %s;" % (where)
        self.env.cr.execute(sql_req)
        res = self.env.cr.fetchall()
        return [("id", "in", [x[0] for x in res])]

    # Overwrite section
    @api.model
    def _get_eshop_domain(self):
        return [("eshop_state", "=", "available")]
