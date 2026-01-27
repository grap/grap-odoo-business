# Copyright (C) 2026 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import http
from odoo.http import request

from odoo.addons.payment_mollie.controllers.main import MollieController


class SaleEshopMollieController(MollieController):

    """
    Redirect Mollie payment to sale_eshop website
    See README for more informations.
    """

    @http.route(
        "/payment/mollie/return",
        type="http",
        auth="public",
        methods=["GET", "POST"],
        csrf=False,
        save_session=False,
    )
    def mollie_return_from_checkout(self, **data):
        """
        We go through /payment/status in case some works is done there
        It's handle and override on post_processing.py
        We set some fields to check transaction status, confirm SO etc.
        """
        res = super().mollie_return_from_checkout(**data)

        sale_id = data.get("eshop_sale_id") or 0
        if sale_id == 0:
            return res
        else:
            company_id = data.get("company_id")
            transaction_id = data.get("transaction_id")
            base_status = "/payment/status?"
            param_status = (
                "eshop_sale_id="
                + str(sale_id)
                + "&company_id="
                + str(company_id)
                + "&transaction_id="
                + str(transaction_id)
            )
            return request.redirect(base_status + param_status)
