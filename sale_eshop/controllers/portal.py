# Copyright (C) 2026 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo.addons.payment.controllers.portal import PaymentPortal


class SaleEshopPaymentPortal(PaymentPortal):

    """
    Inherit Odoo PaymentPortal to handle sale_eshop payment in custom template
    """

    def _get_payment_page_template_xmlid(self, **kwargs):
        if kwargs.get("sale_eshop") == "True":
            return "sale_eshop.payment_page_eshop_template"
        return super()._get_payment_page_template_xmlid(**kwargs)
