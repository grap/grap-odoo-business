# Copyright (C) 2026 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import http
from odoo.http import request


class AccountMove(http.Controller):
    @http.route(
        "/api/generate_payment_link/", type="json", auth="public", readonly=True
    )
    def generate_payment_link(self, **kwargs):
        invoice_id = kwargs.get("invoice_id")
        if not invoice_id:
            return {"error": "invoice_id missing"}

        invoice = request.env["account.move"].sudo().search([("id", "=", invoice_id)])

        if not invoice.exists():
            return {"error": "invoice not found"}

        ctx = {
            "active_model": "account.move",
            "active_id": invoice.id,
        }

        wizard_vals = {
            "res_model": "account.move",
            "res_id": invoice.id,
            "amount": invoice.amount_total,
            "currency_id": invoice.currency_id.id,
            "partner_id": invoice.partner_id.id,
            "description": invoice.name,
        }

        wizard = (
            request.env["payment.link.wizard"]
            .with_context(ctx)
            .sudo()
            .create(wizard_vals)
        )

        return {"payment_url": wizard.link}
