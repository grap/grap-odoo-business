# Copyright (C) 2017 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestModule(TransactionCase):

    def setUp(self):
        super(TestModule, self).setUp()
        self.ProductCategory = self.env['product.category']
        self.IrProperty = self.env['ir.property']
        self.mother_category = self.env.ref(
            'product_category_recursive_property.mother_category')
        self.child_category = self.env.ref(
            'product_category_recursive_property.child_category')
        self.expense_account = self.env.ref(
            'product_category_recursive_property.account_expense')
        self.income_account = self.env.ref(
            'product_category_recursive_property.account_income')

    # Test Section
    def test_01_all_default(self):
        """[Functional Test] Tests changing expense / income account
        on product categories"""

        default_account_expense_id =\
            self.mother_category.property_account_expense_categ_id.id
        default_account_income_id =\
            self.mother_category.property_account_income_categ_id.id

        # Set expense categ to mother category
        self.mother_category.write({
            'property_account_expense_categ_id': self.expense_account.id})
        self.assertEquals(
            self.child_category.property_account_expense_categ_id.id,
            self.expense_account.id,
            "Set an expense account to a mother category must set an"
            " expense account to their childs !")

        # Set income categ to mother category
        self.mother_category.write({
            'property_account_income_categ_id': self.income_account.id})
        self.assertEquals(
            self.child_category.property_account_income_categ_id.id,
            self.income_account.id,
            "Set an income account to a mother category must set an"
            " income account to their childs !")

        # Check if other categories are not affected
        categories = self.ProductCategory.search([
            ('id', 'not in', [
                self.mother_category.id, self.child_category.id])])
        for category in categories:
            self.assertEquals(
                category.property_account_expense_categ_id.id,
                default_account_expense_id,
                "Set an expense categ to a category must not affect non child"
                " categories !")
            self.assertEquals(
                category.property_account_income_categ_id.id,
                default_account_income_id,
                "Set an income categ to a category must not affect non child"
                " categories !")
