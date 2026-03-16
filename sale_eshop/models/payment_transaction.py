# Copyright (C) 2026 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class PaymentTransaction(models.Model):
    # _inherit = "payment.transaction"
    _name = "payment.transaction"
    _inherit = ["payment.transaction", "eshop.mixin"]

    # Inherit Section
    _eshop_fields = ["state"]

    """
	Override Mollie's code to add a param in URL that will be catch later
    See README.md for more informations
	"""

    def _mollie_prepare_payment_payload(self, api_type):
        payment_data, params = super()._mollie_prepare_payment_payload(api_type)

        if api_type == "order" and self.sale_order_ids:
            order = self.sale_order_ids[0]
            if order.eshop_sale:
                base_url = payment_data.get("redirectUrl")
                transaction_id = payment_data.get("metadata")["transaction_id"]
                payment_data["redirectUrl"] = (
                    base_url
                    + "&eshop_sale_id="
                    + str(order.id)
                    + "&company_id="
                    + str(order.company_id.id)
                    + "&transaction_id="
                    + str(transaction_id)
                )

        return payment_data, params
