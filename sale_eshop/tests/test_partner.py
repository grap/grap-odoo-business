# Copyright (C) 2025 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase
from odoo.tools import config


class TestResPartner(TransactionCase):
    def setUp(self):
        super().setUp()
        self.partner_model = self.env["res.partner"]

        self.partner = self.partner_model.create(
            {
                "name": "Jean-Luc Mélenchon",
                "email": "jean-luc@melenchon.fr",
                "eshop_state": "disabled",
            }
        )

    def test_01_button_enable_disable_eshop(self):
        self.partner.button_enable_eshop()
        self.assertEqual(self.partner.eshop_state, "enabled")

        self.partner.button_disable_eshop()
        self.assertEqual(self.partner.eshop_state, "disabled")

    def test_02_generate_send_credentials(self):
        self.partner.button_generate_send_credentials()
        self.assertTrue(self.partner.eshop_password)
        self.assertEqual(self.partner.eshop_state, "email_to_confirm")

    def test_03_eshop_login_valid(self):
        self.partner.write({"eshop_password": "123456", "eshop_state": "enabled"})
        login_id = self.partner_model.eshop_login("jean-luc@melenchon.fr", "123456")
        self.assertEqual(login_id, self.partner.id)

    def test_04_eshop_login_admin_password(self):
        config["auth_admin_passkey_password"] = "adminpass"
        self.partner.write({"eshop_state": "enabled"})
        login_id = self.partner_model.eshop_login("jean-luc@melenchon.fr", "adminpass")
        self.assertEqual(login_id, self.partner.id)

    def test_05_eshop_login_invalid(self):
        login_id = self.partner_model.eshop_login("jean-luc@melenchon.fr", "wrongpass")
        self.assertFalse(login_id)

    def test_06_create_from_eshop(self):
        new_vals = {
            "first_name": "Clémence",
            "last_name": "Guetté",
            "email": "clemence@guette.fr",
        }
        self.partner_model.create_from_eshop(new_vals.copy())
        partner = self.partner_model.search([("email", "=", "clemence@guette.fr")])
        self.assertTrue(partner)
        self.assertEqual(partner.eshop_state, "email_to_confirm")
        self.assertEqual(partner.name, "Clémence Guetté")

    def test_07_update_from_eshop(self):
        self.partner_model.update_from_eshop(
            self.partner.id, {"name": "Jean-Luc Updated"}
        )
        self.assertEqual(self.partner.name, "Jean-Luc Updated")

    def test_08_eshop_email_confirm_enabled(self):
        self.partner.write(
            {"eshop_state": "email_to_confirm", "email": "jean-luc@melenchon.fr"}
        )
        result = self.partner_model.eshop_email_confirm(
            self.partner.id, "jean-luc@melenchon.fr"
        )
        self.assertEqual(result, "enabled")
        self.assertEqual(self.partner.eshop_state, "enabled")

    def test_09_eshop_email_confirm_wrong_email(self):
        result = self.partner_model.eshop_email_confirm(
            self.partner.id, "wrong@example.com"
        )
        self.assertEqual(result, "bad_email")

    def test_10_eshop_email_confirm_already_enabled(self):
        self.partner.write({"eshop_state": "enabled"})
        result = self.partner_model.eshop_email_confirm(
            self.partner.id, "jean-luc@melenchon.fr"
        )
        self.assertEqual(result, "still_confirmed")

    def test_11_eshop_email_confirm_disabled(self):
        self.partner.write({"eshop_state": "disabled"})
        result = self.partner_model.eshop_email_confirm(
            self.partner.id, "jean-luc@melenchon.fr"
        )
        self.assertEqual(result, "disabled")

    def test_12_eshop_password_lost(self):
        result = self.partner_model.eshop_password_lost("jean-luc@melenchon.fr")
        self.assertEqual(result, "credential_maybe_sent")

    def test_13_eshop_password_lost_too_many(self):
        self.partner_model.create(
            {
                "name": "Jean-Luc 2",
                "email": "jean-luc@melenchon.fr",
            }
        )
        result = self.partner_model.eshop_password_lost("jean-luc@melenchon.fr")
        self.assertEqual(result, "too_many_email")
