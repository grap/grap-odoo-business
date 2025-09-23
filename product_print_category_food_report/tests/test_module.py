# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestModule(TransactionCase):
    def setUp(self):
        super().setUp()
        self.ProductPrintWizard = self.env["product.print.wizard"]
        self.categories = self.env["product.print.category"].search([])
        self.report = self.env.ref("product_print_category.pricetag")
        self.products = self.env["product.product"].search(
            [("name", "ilike", "%Pricetag%")]
        )

    def test_render_qweb_pricetag(self):
        for category in self.categories:
            self.products.write({"print_category_id": category.id})

            wizard = self.ProductPrintWizard.with_context(
                active_model="product.print.category",
                active_ids=[category.id],
            ).create({})
            wizard.print_report()
            self.env.ref("product_print_category.pricetag")._render_qweb_pdf(
                "product_print_category.report_pricetag",
                wizard.line_ids.ids,
            )
