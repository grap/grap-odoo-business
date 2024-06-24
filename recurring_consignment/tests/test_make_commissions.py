# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from datetime import timedelta

from odoo import fields
from odoo.tests.common import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestMakeCommissions(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.CommissionWizard = cls.env["invoice.commission.wizard"]
        cls.IrActionsReport = cls.env["ir.actions.report"]
        cls.AccountMove = cls.env["account.move"]
        cls.consignor_1 = cls.env.ref("recurring_consignment.consignor_1")
        cls.customer_invoice_1 = cls.env.ref("recurring_consignment.customer_invoice_1")
        cls.customer_invoice_2 = cls.env.ref("recurring_consignment.customer_invoice_2")
        cls.commission_product_vat_20 = cls.env.ref(
            "recurring_consignment.commission_product_vat_20"
        )
        cls.vat_20_exclude = cls.env.ref("recurring_consignment.vat_20_exclude")
        cls.invoice_report = cls.env.ref("account.account_invoices")
        cls.env.user.company_id = cls.env.ref("recurring_consignment.company")

    def _make_commission(self, consignors):
        wizard = self.CommissionWizard.with_context(active_ids=consignors.ids).create(
            {}
        )

        # Set max date to the last day of the current month
        today = fields.date.today()
        if today.month < 12:
            wizard.max_date = fields.date(today.year, today.month + 1, 1) - timedelta(
                days=1
            )
        else:
            wizard.max_date = fields.date(today.year + 1, 1, 1) - timedelta(days=1)

        wizard._onchange_max_date()

        wizard.invoice_commission()

        return self.AccountMove.search(
            [
                ("partner_id", "=", self.consignor_1.id),
                ("is_consignment_invoice", "=", True),
            ]
        )

    # Test Section
    def test_30_commission_workflow(self):
        self.customer_invoice_1.action_post()
        self.customer_invoice_2.action_post()

        commission_invoices = self._make_commission(self.consignor_1)

        self.assertEqual(
            len(commission_invoices), 1, "It should generate one invoice commission"
        )

        commission_invoice = commission_invoices[0]

        self.assertEqual(commission_invoice.state, "draft")

        lines_20 = commission_invoice.invoice_line_ids.filtered(
            lambda x: x.product_id.id == self.commission_product_vat_20.id
        )
        # check invoice lines generated
        self.assertEqual(
            len(commission_invoice.invoice_line_ids),
            1,
            "One commission line should be generated",
        )
        self.assertEqual(
            len(lines_20), 1, "One 20% commission line should be generated"
        )

        # Check line details (Tax Excl)
        line_20 = lines_20[0]
        self.assertEqual(line_20.quantity, 1, "Incorrect Commission Quantity.")
        self.assertEqual(
            line_20.price_unit,
            2100 + 20,
            "Incorrect Commission Price Unit, awaiting"
            " (10,000 + 500) * 0.2"
            " + 100 * 0.2",
        )
        self.assertEqual(
            line_20.tax_ids.ids,
            [self.vat_20_exclude.id],
            "Incorrect Commission Tax.",
        )

        self.IrActionsReport._render_qweb_pdf(
            "account.account_invoices", commission_invoices.ids
        )

        commission_invoice.action_post()
        self.assertEqual(commission_invoice.payment_state, "paid")

    def test_31_commission_refund(self):
        # confirm sale of (+50) unit
        self.customer_invoice_2.action_post()

        # Copy, change quantity (+90) and confirm
        copy_invoice = self.customer_invoice_2.copy()
        copy_invoice.invoice_line_ids[0].quantity = 90
        copy_invoice.action_post()

        # Make a refund change quantity (-20) and confirm.
        refund_invoice = self.customer_invoice_2._reverse_moves()
        refund_invoice.invoice_line_ids[0].quantity = 20
        refund_invoice.action_post()

        commission_invoices = self._make_commission(self.consignor_1)

        res = commission_invoices.get_commission_information_product_detail()[0]
        self.assertEqual(
            res["quantity"],
            50 + 90 - 20,
            "Error with refunded sale invoices : Bad quantity of product.",
        )

        self.assertEqual(
            res["total_vat_excl"],
            10 * (50 + 90 - 20),
            "Error with refunded sale invoices : Bad price subtotal vat excl.",
        )
