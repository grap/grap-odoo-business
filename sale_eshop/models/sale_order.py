# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import _, api, fields, models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = ["sale.order", "eshop.mixin"]

    eshop_sale = fields.Boolean()
    eshop_note = fields.Char(help="Field set by eshop user during cart validation")

    recovery_name = fields.Char(
        compute="_compute_recovery_infos",
    )

    recovery_extra_cost = fields.Float(
        compute="_compute_recovery_infos",
    )

    # Inherit Section
    _eshop_fields = [
        "amount_total",
        "note",
        "name",
        "eshop_sale",
        "eshop_note",
        "amount_untaxed",
        "amount_tax",
        "recovery_moment_id",
        "recovery_name",
        "recovery_extra_cost",
    ]

    # Compute Section
    @api.depends("recovery_moment_id", "recovery_moment_id.place_id")
    def _compute_recovery_infos(self):
        for sale in self:
            _place = sale.recovery_moment_id.place_id
            sale.recovery_name = _place.name
            sale.recovery_extra_cost = (
                _place.shipping_product_id.list_price
                if _place.shipping_product_id
                else 0
            )

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
            order._action_cancel()
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
    def eshop_set_eshop_note(self, partner_id, eshop_note):
        order = self.eshop_get_current_sale_order(partner_id)
        if order:
            order.write({"eshop_note": eshop_note})
            return order.eshop_note

    @api.model
    def eshop_set_quantity(self, partner_id, product_id, quantity, method):
        SaleOrderLine = self.env["sale.order.line"]
        ResPartner = self.env["res.partner"]

        order = self.eshop_get_current_sale_order(partner_id)

        if not order:
            partner = ResPartner.browse(partner_id)
            if partner.property_product_pricelist:
                pricelist_id = partner.property_product_pricelist.id
            else:
                pricelist_id = self.env.company.eshop_pricelist_id.id
            order = self.create(
                {
                    "partner_id": partner_id,
                    "partner_invoice_id": partner_id,
                    "partner_shipping_id": partner_id,
                    "pricelist_id": pricelist_id,
                    "eshop_sale": True,
                }
            )

        # Search Line With Product.
        current_line = order.order_line.filtered(
            lambda x: x.product_id.id == product_id
        )

        # Add Qty if add method is used (in Catatog view)
        if current_line:
            current_line = current_line[0]
            if method == "add":
                quantity += current_line.product_uom_qty

        if quantity != 0:
            if not current_line:
                line_vals = {
                    "order_id": order.id,
                    "product_id": product_id,
                    "product_uom_qty": quantity,
                }
                if self.env.company.eshop_wallet_enabled:
                    line_vals["qty_to_invoice"] = quantity
                current_line = SaleOrderLine.create(line_vals)
            else:
                current_line.write(
                    {
                        "product_uom_qty": quantity,
                    }
                )
                if self.env.company.eshop_wallet_enabled:
                    current_line.write(
                        {
                            "qty_to_invoice": quantity,
                        }
                    )
            messages = current_line.eshop_apply_minimum_quantity()

            res = {
                "messages": messages,
                "quantity": current_line.product_uom_qty,
                "qty_to_invoice": current_line.qty_to_invoice,
                "changed": (quantity != current_line.product_uom_qty),
                "price_subtotal": current_line.price_subtotal,
                "price_total": current_line.price_total,
                "discount": current_line.discount,
            }
        else:
            # Delete cart line
            res = {
                "quantity": 0,
                "changed": False,
                "price_subtotal": 0,
                "price_total": 0,
                "discount": 0,
            }
            if current_line:
                if len(order.order_line) == 1:
                    order.unlink()
                    res["messages"] = [
                        _("The Shopping Cart has been successfully deleted.")
                    ]
                else:
                    current_line.unlink()
                    res["messages"] = [_("The line has been successfully deleted.")]

        res.update(self._eshop_sale_order_info(order))
        return res

    @api.model
    def eshop_select_recovery_moment(self, partner_id, recovery_moment_id):
        recovery_moment = self.env["sale.recovery.moment"].browse(recovery_moment_id)
        # Check if the moment is complete
        if recovery_moment.is_complete:
            return "recovery_moment_complete"
        else:
            order = self.eshop_get_current_sale_order(partner_id)
            order.write({"recovery_moment_id": recovery_moment_id})
        return True

    @api.model
    def eshop_confirm_sale_order(self, partner_id):
        order = self.eshop_get_current_sale_order(partner_id)
        # Remove .with_delay because we need sale to be confirm right now in order
        # to create invoice
        order.with_context(send_email=True).action_confirm()
        return True

    @api.model
    def eshop_invoice_with_wallet(self, order_id):
        order = self.browse(order_id)

        wallet_journal = self.env["account.journal"].search(
            [("type", "=", "bank"), ("is_customer_wallet_journal", "=", True)], limit=1
        )

        if not wallet_journal:
            raise UserError(_("Wallet journal can't be found. Check settings."))

        payment_method = self.env.ref("account.account_payment_method_manual_in")
        if not payment_method:
            raise UserError(_("Manuel payment method can't be found."))

        # savepoint to rollback if error ?
        with self.env.cr.savepoint():
            # 0. Force lines to be invoiced (even if invoice_policy is in delivered)
            for line in order.order_line:
                line.qty_to_invoice = line.product_uom_qty - line.qty_invoiced

            # 1. Create invoice
            invoice = order._create_invoices()
            invoice.action_post()

            # 2. Check if all went right
            if invoice.state != "posted":
                raise UserError(_("Invoice was not posted correctly."))

            # 3. Create payment with wallet journal
            payment = self.env["account.payment"].create(
                {
                    "payment_type": "inbound",
                    "partner_type": "customer",
                    "partner_id": invoice.partner_id.id,
                    "amount": invoice.amount_total,
                    "payment_method_id": payment_method.id,
                    "journal_id": wallet_journal.id,
                    "date": fields.Date.context_today(self),
                    "ref": "[eshop] " + invoice.name,
                }
            )
            payment.action_post()

            # 4. Reconcile payment and invoice
            lines_to_reconcile = (invoice.line_ids + payment.move_id.line_ids).filtered(
                lambda x: x.account_id
                == invoice.partner_id.property_account_receivable_id
                and not x.reconciled
            )

            lines_to_reconcile.reconcile()

        return True

    @api.model
    def eshop_invoice_online_payment(self, order_id, transaction_id):
        order = self.browse(order_id)
        transaction = self.env["payment.transaction"].browse(transaction_id)

        # savepoint to rollback if error ?
        with self.env.cr.savepoint():
            # 0. Force lines to be invoiced (even if invoice_policy is in delivered)
            for line in order.order_line:
                line.qty_to_invoice = line.product_uom_qty - line.qty_invoiced

            # 1. Create invoice
            invoice = order._create_invoices()
            invoice.action_post()

            # 2. Check if all went right
            if invoice.state != "posted":
                raise UserError(_("Invoice was not posted correctly."))

            # 3. Create payment through Mollie algorythm with transaction
            # This function post payment and reconcile with invoice
            payment_record = transaction.sudo()._create_payment()

        return invoice.id

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
