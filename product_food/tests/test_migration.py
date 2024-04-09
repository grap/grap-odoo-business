# Copyright 2021 - Today Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase

from ..models.tools import get_allergen_data


class TestMigration(TransactionCase):
    def setUp(self):
        super().setUp()
        self.all_allergens = self.env["product.allergen"].search([])

    def test_allergen(self):
        self._assert_result("Sésame.", ["SES"])

        self._assert_result(
            """Cacahuètes.
            Peur contenir des traces fruits à coques et de sésame.""",
            ["ARA"],
            ["FAC", "SES"],
        )
        self._assert_result(
            """Présence et/ou traces possibles de
            fruits à coques, arachide, gluten, sésame et soja.""",
            [],
            ["FAC", "ARA", "GLU", "SES", "SOJA"],
        )

    def _assert_result(self, text, code_list, trace_code_list=False):
        (
            allergen_text,
            allergens,
            residual,
            trace_allergens,
            trace_residual,
        ) = get_allergen_data(self.env, text, self.all_allergens)
        if not trace_code_list:
            trace_code_list = []
        self.assertEqual(sorted(allergens.mapped("code")), sorted(code_list))
        self.assertEqual(
            sorted(trace_allergens.mapped("code")), sorted(trace_code_list)
        )
