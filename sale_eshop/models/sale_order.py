# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import _, api, models

from odoo.addons.queue_job.job import job


class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = ["sale.order", "eshop.mixin"]

    # Inherit Section
    _eshop_fields = [
        "amount_total",
        "note",
        "amount_untaxed",
        "amount_tax",
    ]

    # API Section
    @api.model
    def eshop_custom_load_data(self, partner_id):
        domain = [
            ("partner_id", "=", partner_id),
            ("user_id", "=", self.env.user.id),
            ("state", "=", "draft"),
        ]
        return self.eshop_load_data(domain)

    @api.model
    def eshop_get_current_sale_order(self, partner_id):
        order_ids = self.search(
            [
                ("partner_id", "=", partner_id),
                ("user_id", "=", self.env.user.id),
                ("state", "=", "draft"),
            ]
        )
        return order_ids and order_ids[0] or False

    @api.model
    def eshop_delete_current_sale_order(self, partner_id):
        order = self.eshop_get_current_sale_order(partner_id)
        if order:
            order.unlink()
        return True

    @api.model
    def eshop_delete_sale_order_line(self, partner_id, line_id):
        order = self.eshop_get_current_sale_order(partner_id)
        if order:
            line = order.order_line.filtered(lambda x: x.id == line_id)
            if line:
                if len(order.order_line) == 1:
                    order.unlink()
                    return "order_deleted"
                else:
                    line.unlink()
                    return "line_deleted"
        return True

    @api.model
    def eshop_set_note(self, partner_id, note):
        order = self.eshop_get_current_sale_order(partner_id)
        if order:
            order.write({"note": note})
            return order.note

    @api.model
    def eshop_set_quantity(self, partner_id, product_id, quantity, method):
        """@method : 'set' / 'add'"""
        SaleOrderLine = self.env["sale.order.line"]
        ResPartner = self.env["res.partner"]

        order = self.eshop_get_current_sale_order(partner_id)

        if not order:
            # Create Sale Order
            partner = ResPartner.browse(partner_id)
            if partner.property_product_pricelist:
                pricelist_id = partner.property_product_pricelist.id
            else:
                pricelist_id = self.env.user.company_id.eshop_pricelist_id.id
            order = self.create(
                {
                    "partner_id": partner_id,
                    "partner_invoice_id": partner_id,
                    "partner_shipping_id": partner_id,
                    "pricelist_id": pricelist_id,
                }
            )

        # Search Line
        current_line = False
        for line in order.order_line:
            if line.product_id.id == product_id:
                current_line = line
                if method == "add":
                    quantity += line.product_uom_qty
                break

        if quantity != 0:
            if not current_line:
                new_line = SaleOrderLine.new()
                new_line.product_id = product_id
                new_line.order_id = order.id
                new_line.product_uom_qty = quantity
                new_line.product_id_change()
                new_line_vals = SaleOrderLine._convert_to_write(
                    new_line._cache)
                current_line = SaleOrderLine.create(new_line_vals)
            else:
                current_line.product_uom_qty = quantity
                current_line.product_id_change()
            messages = current_line.eshop_apply_minimum_quantity()

            res = {
                "messages": messages,
                "quantity": current_line.product_uom_qty,
                "changed": (quantity != current_line.product_uom_qty),
                "price_subtotal": current_line.price_subtotal,
                "price_total": current_line.price_total,
                "discount": current_line.discount,
            }
        else:
            res = {
                "quantity": 0,
                "changed": False,
                "price_subtotal": 0,
                "price_total": 0,
                "discount": 0,
            }
            if current_line:
                if len(order.order_line) == 1:
                    # We unlink the whole order
                    order.unlink()
                    res["messages"] = [
                        _("The Shopping Cart has been successfully deleted.")
                    ]
                else:
                    # We unlink the line
                    current_line.unlink()
                    res["messages"] = [
                        _("The line has been successfully deleted")
                    ]

        res.update(self._eshop_sale_order_info(order))
        return res

    @api.model
    def eshop_select_recovery_moment(self, partner_id, recovery_moment_id):
        recovery_moment = self.env["sale.recovery.moment"].browse(
            recovery_moment_id
        )
        # Check if the moment is complete
        if recovery_moment.is_complete:
            return "recovery_moment_complete"
        else:
            order = self.eshop_get_current_sale_order(partner_id)
            order.write(
                {"recovery_moment_id": recovery_moment_id}
            )
            self.with_delay()._eshop_confirm_sale_order(order.id)
        return True

    @api.model
    @job(default_channel='root.sale_eshop_confirm_order')
    def _eshop_confirm_sale_order(self, order_id):
        order = self.browse(order_id)
        order.with_context(send_email=True).action_confirm()

    # Custom Section
    def _eshop_sale_order_info(self, order):
        if order:
            return {
                "amount_untaxed": order.amount_untaxed,
                "amount_tax": order.amount_tax,
                "amount_total": order.amount_total,
                "order_id": order.id,
            }
        else:
            return {
                "amount_untaxed": 0,
                "amount_tax": 0,
                "amount_total": 0,
                "order_id": False,
            }
