# Copyright (C) 2018-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    product_expense_total = fields.Float(
        string="Product Expenses Total",
        compute="_compute_expense_total",
        digits="Product Price",
        store=True,
    )

    distributed_expense_total = fields.Float(
        string="Distributed Expenses Total",
        compute="_compute_expense_total",
        digits="Product Price",
        store=True,
    )

    @api.depends(
        "invoice_line_ids.product_id.is_impact_standard_price",
        "invoice_line_ids.price_subtotal",
    )
    def _compute_expense_total(self):
        for invoice in self.filtered(lambda x: x.move_type == "in_invoice"):
            invoice.update(
                {
                    "product_expense_total": sum(
                        invoice.invoice_line_ids.filtered(
                            lambda x: not x.product_id
                            or not x.product_id.is_impact_standard_price
                        ).mapped("price_subtotal")
                    ),
                    "distributed_expense_total": sum(
                        invoice.invoice_line_ids.filtered(
                            lambda x: x.product_id
                            and x.product_id.is_impact_standard_price
                        ).mapped("price_subtotal")
                    ),
                }
            )

    def _get_update_supplierinfo_lines(self):
        ProductProduct = self.env["product.product"]
        res = super()._get_update_supplierinfo_lines()
        new_res = []
        for line in res:
            # Remove products that represent distributed cost
            product = ProductProduct.browse(line[2]["product_id"])
            if not product.is_impact_standard_price:
                new_res.append(line)
        return new_res
