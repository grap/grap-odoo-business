# Copyright (C) 2026 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models
from odoo.http import request


class AccountMove(models.Model):
    _name = "account.move"
    _inherit = ["account.move", "eshop.mixin"]

    def eshop_invoice_payment_link(self):
        self.ensure_one()
        ctx = {
            "active_model": "account.move",
            "active_id": self.id,
        }

        wizard_vals = {
            "res_model": "account.move",
            "res_id": self.id,
            "amount": self.amount_total,
            "currency_id": self.currency_id.id,
            "partner_id": self.partner_id.id,
            "description": self.name,
        }
        # wizard = self.env['payment.link.wizard'].with_context(ctx).create(wizard_vals)
        wizard = self.env["payment.link.wizard"].with_context(ctx).new(wizard_vals)
        import pdb

        pdb.set_trace()
        req = request.env["account.move"]
        # # wizard._compute_link()
        # from werkzeug import urls

        # access_token = self.env['payment.link.wizard'].sudo()._get_access_token(
        #     partner_id=self.partner_id.id,
        #     amount=self.amount_total,
        #     currency_id=self.currency_id.id,
        # )

        # # wizard = self.env['payment.link.wizard'].browse(wizard.id)

        # payment_url = wizard.link
        return payment_url
