# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


import math

from odoo import _, api, models


class SaleOrderLine(models.Model):
    _name = "sale.order.line"
    _inherit = ["sale.order.line", "eshop.mixin"]

    # Inherit Section
    _eshop_fields = [
        "product_id",
        "product_uom",
        "price_unit",
        "tax_id",
        "discount",
        "product_uom_qty",
        "price_subtotal",
        "price_total",
    ]

    # API Section
    @api.model
    def eshop_custom_load_data(self, order_id):
        domain = [
            ("order_id", "=", order_id),
        ]
        items = self.eshop_load_data(domain)
        for item in items:
            tax_ids = item["tax_id"]
            product_uom_id = item["product_uom"]
            item.pop("tax_id")
            item.pop("product_uom")
            item["tax_ids"] = tax_ids
            item["product_uom_id"] = product_uom_id
        return items

    @api.multi
    def eshop_apply_minimum_quantity(self):
        messages = []
        self.ensure_one()
        if self.product_id.eshop_minimum_qty:

            if self.product_uom_qty < self.product_id.eshop_minimum_qty:
                # The quantity will be augmented to the threshold
                messages.append(
                    _(
                        "'%.3f' is not a valid quantity for %s, the "
                        " minimum quantity is '%.3f'. The quantity has"
                        " been automatically increased in your shopping"
                        " cart."
                    )
                    % (
                        self.product_uom_qty,
                        self.product_id.name,
                        self.product_id.eshop_minimum_qty,
                    )
                )
                self.product_uom_qty = self.product_id.eshop_minimum_qty
            else:
                rounded_qty = self._eshop_round_value(
                    self.product_id, self.product_uom_qty
                )
                if self.product_uom_qty != rounded_qty:
                    # The quantity will be rounded
                    messages.append(
                        _(
                            "'%.3f' is not a valid quantity for %s, the"
                            " quantity has been rounded to '%.3f'."
                        )
                        % (
                            self.product_uom_qty,
                            self.product_id.name,
                            rounded_qty,
                        )
                    )
                    self.product_uom_qty = rounded_qty

        return messages

    # Custom Section
    @api.model
    def _eshop_round_value(self, product, qty):
        rounded_qty = product.eshop_rounded_qty
        digit = len(str(float(rounded_qty) - int(rounded_qty)).split(".")[1])
        division = float(qty) / rounded_qty
        if division % 1 == 0:
            return qty
        else:
            return round(math.ceil(division) * rounded_qty, digit)
