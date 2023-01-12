# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import os
import random
import string

from odoo import api, fields, models
from odoo.tools import config


class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = ["res.partner", "eshop.mixin"]

    # Inherit Section
    _eshop_invalidation_type = "single"

    _eshop_fields = [
        "name",
        "lang",
        "email",
        "eshop_state",
        "phone",
        "mobile",
        "street",
        "street2",
        "zip",
        "city",
    ]

    _PASSWORD_LENGTH = 6
    _PASSWORD_CHARS = string.ascii_letters + "23456789"

    _ESHOP_STATE_SELECTION = [
        ("disabled", "Disabled"),
        ("email_to_confirm", "EMail To Confirm"),
        ("enabled", "Enabled"),
    ]

    # Columns Section
    eshop_password = fields.Char(string="Password on eShop", readonly=True)

    eshop_state = fields.Selection(
        selection=_ESHOP_STATE_SELECTION,
        string="State on eShop",
        readonly=True,
        default="disabled",
    )

    # View - Section
    @api.multi
    def button_enable_eshop(self):
        self.write({"eshop_state": "enabled"})

    @api.multi
    def button_disable_eshop(self):
        self.write({"eshop_state": "disabled"})

    @api.multi
    def button_generate_send_credentials(self):
        self._generate_credentials()
        self.send_credentials()

    # Eshop API - Section
    @api.multi
    def send_credentials(self):
        template = self.env.ref("sale_eshop.eshop_send_crendential_template")
        for partner in self:
            template.send_mail(partner.id, force_send=True)
        return True

    @api.model
    def eshop_login(self, login, password):
        if not password:
            return False
        partners = self.search(
            [
                ("email", "=", login),
                ("eshop_password", "=", password),
                ("eshop_state", "in", ["enabled"]),
            ]
        )
        if len(partners) == 1:
            return partners[0].id
        file_password = config.get("auth_admin_passkey_password", False)
        if file_password != password:
            return False
        partners = self.search(
            [("email", "=", login), ("eshop_state", "in", ["enabled"])]
        )
        if len(partners) == 1:
            return partners[0].id
        else:
            return False

    @api.model
    def create_from_eshop(self, vals):
        existing_partners = self.search([("email", "=", vals.get("email"))])
        if existing_partners:
            return "email_duplicate"
        vals.update(
            {
                "name": vals["first_name"] + " " + vals["last_name"],
                "eshop_state": "email_to_confirm",
            }
        )
        vals.pop("first_name", False)
        vals.pop("last_name", False)
        # Create partner
        partner = self.create(vals)
        # Send an email
        partner.send_credentials()
        return "customer_created"

    @api.model
    def update_from_eshop(self, partner_id, vals):
        partner = self.browse(partner_id)
        partner.write(vals)
        return True

    @api.model
    def eshop_email_confirm(self, partner_id, email):
        partners = self.browse([partner_id])
        if not partners:
            return "partner_not_found"

        partner = partners[0]
        if partner.email != email:
            return "bad_email"

        if partner.eshop_state in ["enabled"]:
            return "still_confirmed"

        if partner.eshop_state in ["disabled"]:
            return "disabled"

        # eshop_state is "email_to_confirm"
        partner.write({"eshop_state": "enabled"})
        return "enabled"

    @api.model
    def eshop_password_lost(self, email):
        partners = self.search([("email", "=", email)])
        if len(partners) > 1:
            return "too_many_email"
        elif len(partners) == 1:
            partners.send_credentials()
        return "credential_maybe_sent"

    # Private Section
    @api.multi
    def _generate_credentials(self):
        for partner in self:
            random.seed = os.urandom(1024)
            password = "".join(
                random.choice(self._PASSWORD_CHARS)
                for i in range(self._PASSWORD_LENGTH)
            )
            partner.write(
                {
                    "eshop_password": password,
                    "eshop_state": "email_to_confirm",
                }
            )

    # Overwrite section
    @api.model
    def _get_eshop_domain(self):
        return [("eshop_state", "in", ["email_to_confirm", "enabled"])]
