# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import _, api, fields, models


class ConsignorCreateWizard(models.TransientModel):
    _name = "consignor.create.wizard"
    _description = "Consignor Creation Wizard"

    # Setting Section
    @api.multi
    def _get_account_prefix(self):
        self.ensure_one()
        # For the time being, we have no other cases
        return "467"

    @api.multi
    def _get_tax_included(self):
        self.ensure_one()
        # for the time being, we have no B2B company
        # with consignors
        return True

    # Columns Section
    name = fields.Char(string="Consignor Name")

    account_suffix = fields.Char(string="Account Suffix")

    rate = fields.Float(string="Commission Rate")

    is_vat_subject = fields.Boolean(string="Subject to VAT", default=True)

    product_ids = fields.Many2many(
        comodel_name="product.product",
        string="Available Taxes",
        domain="[('is_consignment_commission', '=', True)]",
        default=lambda x: x._default_product_ids(),
    )

    # Default values Section
    def _default_product_ids(self):
        ProductProduct = self.env["product.product"]
        products = ProductProduct.search([("is_consignment_commission", "=", True)])
        return products.ids

    # Action Section
    @api.multi
    def create_consignor(self):
        self.ensure_one()
        ResPartner = self.env["res.partner"]
        AccountAccount = self.env["account.account"]
        AccountTax = self.env["account.tax"]
        FiscalClassification = self.env["account.product.fiscal.classification"]

        # Create Objects
        sequence = self.env["ir.sequence"].next_by_code("consignor.create.wizard")
        account = AccountAccount.create(self._prepare_account())
        partner = ResPartner.create(self._prepare_partner(sequence, account))
        for product in self.product_ids:
            tax = AccountTax.create(
                self._prepare_tax(sequence, account, partner, product)
            )
            FiscalClassification.create(
                self._prepare_fiscal_classification(sequence, partner, tax)
            )

        # Return view with the new consignor
        action = self.env.ref("base.action_partner_form").read()[0]
        form_view = [(self.env.ref("base.view_partner_form").id, "form")]
        action["views"] = form_view + [
            (state, view) for state, view in action.get("views", []) if view != "form"
        ]
        action["res_id"] = partner.id

        return action

    @api.multi
    def _prepare_account(self):
        self.ensure_one()
        return {
            "name": self.name,
            "company_id": self.env.user.company_id.id,
            "code": "{prefix}{suffix}".format(
                prefix=self._get_account_prefix(), suffix=self.account_suffix
            ),
            "reconcile": False,
            "user_type_id": self.env.ref("account.data_account_type_other_income").id,
        }

    @api.multi
    def _prepare_tax(self, sequence, account, partner, commission_product):
        self.ensure_one()
        amount = commission_product.taxes_id[0].amount
        return {
            "name": "{sequence} - {amount:.1f} -{vat_subject}{name}".format(
                sequence=sequence,
                amount=amount,
                vat_subject=self.is_vat_subject and " " or _(" NOT SUBJECT TO VAT - "),
                name=self.name,
            ),
            "company_id": self.env.user.company_id.id,
            "description": self.is_vat_subject
            and "{amount:.1f}%".format(amount=amount)
            or "0%",
            "amount": self.is_vat_subject and amount or 0.0,
            "amount_type": "percent",
            "price_include": self._get_tax_included(),
            "account_id": account.id,
            "refund_account_id": account.id,
            "consignor_partner_id": partner.id,
            "consignment_product_id": commission_product.id,
        }

    def _prepare_fiscal_classification(self, sequence, partner, tax):
        return {
            "name": _("{sequence} - VAT {amount:2.1f}% -{vat_subject}{name}").format(
                sequence=sequence,
                amount=tax.consignment_product_id.taxes_id[0].amount,
                vat_subject=self.is_vat_subject and " " or _(" NOT SUBJECT TO VAT - "),
                name=self.name,
            ),
            "sale_tax_ids": [(4, tax.id)],
            "consignor_partner_id": partner.id,
        }

    @api.multi
    def _prepare_partner(self, sequence, account):
        self.ensure_one()
        return {
            "name": "{sequence} - {name}".format(
                sequence=sequence,
                name=self.name,
            ),
            "consignment_account_id": account.id,
            "property_account_receivable_id": account.id,
            "property_account_payable_id": account.id,
            "consignment_commission": self.rate,
            "is_consignor": True,
            "customer": False,
            "supplier": True,
        }
