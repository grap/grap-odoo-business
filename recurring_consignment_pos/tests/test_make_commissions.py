# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import tagged

from odoo.addons.recurring_consignment.tests.test_make_commissions import (
    TestMakeCommissions,
)

from .test_abstract import TestAbstract


@tagged("post_install", "-at_install")
class TestMakeCommissionPointOfSale(TestAbstract, TestMakeCommissions):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_50_commission_workflow_point_of_sale(self):
        self._make_pos_order(product=self.product_E, close_session=True)
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

        # Check line #2 details (Tax Excl)
        line_20 = lines_20[0]
        self.assertEqual(line_20.quantity, 1, "Incorrect Commission Quantity.")
        self.assertEqual(
            line_20.price_unit, 0.2, "Incorrect Commission Price Unit, awaiting 1 * 0.2"
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
