# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, models
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def _check_consignor_changes(self):
        PurchaseOrderLine = self.env["purchase.order.line"]
        res = super()._check_consignor_changes()
        order_lines = PurchaseOrderLine.search(
            [("product_id", "in", self.mapped("product_variant_ids").ids)]
        )
        if len(order_lines):
            raise UserError(
                _(
                    "You can not change the value of the field"
                    " 'Consignor' because the product is associated"
                    " to one or more Purchase Order Lines. You should"
                    " disable the product and create a new one."
                )
            )
        return res
