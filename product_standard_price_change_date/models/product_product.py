# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT (quentin.dupont@grap.coop)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    standard_price_change_date = fields.Date(
        help="Date of last standard price change. "
        "Automatically sets to the date of the day you changed the standard price",
    )

    @api.onchange("standard_price")
    def _onchange_standard_price_change_date(self):
        for product in self:
            product.standard_price_change_date = fields.Date.today()

    # Overload Section
    @api.model_create_multi
    def create(self, vals_list):
        products = super().create(vals_list)
        for product in products.filtered(lambda x: x.standard_price):
            product.standard_price_change_date = fields.Date.today()
        return products

    def write(self, vals):
        if "standard_price" in vals:
            vals["standard_price_change_date"] = fields.Date.today()
        return super().write(vals)
