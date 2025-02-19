# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import Command
from odoo.tests.common import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestAbstract(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.PosOrder = cls.env["pos.order"]
        cls.env.user = cls.env.ref("base.user_admin")
        cls.env.user.company_id = cls.env.ref("recurring_consignment.company")
        cls.env.company = cls.env.ref("recurring_consignment.company")
        cls.config = cls.env.ref("recurring_consignment_pos.pos_config")
        cls.payment_method_cash = cls.env.ref(
            "recurring_consignment_pos.payment_method_cash"
        )

        cls.product_E = cls.env.ref(
            "recurring_consignment_pos.consigned_product_consignor_1_vat_20_E"
        )
        # cls.payment_method_cash = cls.env["pos.payment.method"].create(
        #     {
        #         "name": "Cash",
        #         "journal_id": cls.env.ref(
        #             "recurring_consignment.account_journal_cash"
        #         ).id,
        #         "company_id": cls.env.company.id,
        #     }
        # )
        # cls.config.payment_method_ids = cls.payment_method_cash.ids

    def _make_pos_order(self, product=False, close_session=False):
        self.config.open_ui()
        self.pos_session = self.config.current_session_id

        line_vals = {
            "id": 1,
            "qty": 1,
            "price_unit": 1,
            "price_subtotal": 1,
            "price_subtotal_incl": 1.20,
            "discount": 0,
            "product_id": product.id,
            "tax_ids": [[6, False, product.taxes_id.ids]],
            "full_product_name": product.name,
        }
        statement_vals = {
            "name": "2024-06-26 23:28:47",
            "payment_method_id": self.payment_method_cash.id,
            "amount": 1.20,
        }

        order_data = {
            "id": "00003-001-0001",
            "data": {
                "sequence_number": 1,
                "name": "Order 00099-099-0099",
                "pos_session_id": self.pos_session.id,
                "creation_date": "2024-06-26T23:28:47.947Z",
                "access_token": "a89e1005-6f4c-4aa6-9b0f-9bc27a5379ff",
                "user_id": self.env.user.id,
                "pricelist_id": 1,
                "fiscal_position_id": False,
                "partner_id": False,
                "amount_paid": 1.20,
                "amount_total": 1.20,
                "amount_tax": 0.20,
                "amount_return": 0,
                "lines": [Command.create(line_vals)],
                "statement_ids": [Command.create(statement_vals)],
            },
            "to_invoice": False,
        }

        orders = self.PosOrder.create_from_ui([order_data])

        self.assertEqual(len(orders), 1)

        if close_session:
            self.pos_session.close_session_from_ui()

        return self.pos_session, orders
