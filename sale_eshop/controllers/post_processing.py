# Copyright (C) 2026 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import http
from odoo.http import request

from odoo.addons.payment.controllers.post_processing import PaymentPostProcessing


class SaleEshopPaymentPostProcessing(PaymentPostProcessing):

    """
    Inherit Odoo Payment Controller to redirect Mollie payment to sale_eshop website
    See README for more informations.
    """

    @http.route(
        "/payment/status", type="http", auth="public", website=True, sitemap=False
    )
    def display_status(self, **kwargs):
        """We go through /payment/status in case some works is done there
        Its handle and override on post_processing.py
        """
        res = super().display_status()
        if (
            "eshop_sale_id" in kwargs
            and "company_id" in kwargs
            and "transaction_id" in kwargs
        ):
            company_id = int(kwargs.get("company_id"))
            base_url = (
                request.env["res.company"].browse(company_id).eshop_url.rstrip("/")
                + "/"
            )
            if base_url:
                sale_id = kwargs.get("eshop_sale_id")  # needed to confirm it
                transaction_id = kwargs.get("transaction_id")  # needed to get status
                base_status = "payment_validation_online/status/"
                param_status = str(sale_id) + "/" + str(transaction_id)
                # Return to non-local url because we go to website → local=False
                return request.redirect(
                    base_url + base_status + param_status, local=False
                )

        return res
