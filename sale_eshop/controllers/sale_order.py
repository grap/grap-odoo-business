# Copyright (C) 2026 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import http
from odoo.http import request


class SaleOrder(http.Controller):
    @http.route(
        "/api/sale_generate_payment_link/", type="json", auth="public", readonly=True
    )
    def generate_payment_link(self, **kwargs):
        sale_id = kwargs.get("sale_id")
        if not sale_id:
            return {"error": "sale_id missing"}

        sale = request.env["sale.order"].sudo().search([("id", "=", sale_id)])

        if not sale.exists():
            return {"error": "sale not found"}

        ctx = {
            "active_model": "sale.order",
            "active_id": sale.id,
        }

        wizard_vals = {
            "res_model": "sale.order",
            "res_id": sale.id,
            "amount": sale.amount_total,
            "currency_id": sale.currency_id.id,
            "partner_id": sale.partner_id.id,
            "description": sale.name,
        }

        wizard = (
            request.env["payment.link.wizard"]
            .with_context(ctx)
            .sudo()
            .create(wizard_vals)
        )

        return {"payment_url": wizard.link}
