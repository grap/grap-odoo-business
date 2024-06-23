# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ConsignorCreateWizard(models.TransientModel):
    _name = "consignor.create.wizard"
    _description = "Consignor Creation Wizard"

    # Setting Section
    def _default_account_prefix(self):
        return self.env.company.recurring_consignment_account_prefix

    # Columns Section
    consignor_name = fields.Char(required=True)

    account_prefix = fields.Char(
        readonly=True, required=True, default=lambda x: x._default_account_prefix()
    )

    account_suffix = fields.Char(required=True)

    account_code = fields.Char(compute="_compute_account_code")

    commission_rate = fields.Float()

    is_vat_subject = fields.Boolean(string="Subject to VAT", default=True)

    has_vat_000 = fields.Boolean(string="VAT 00,0%")

    has_vat_021 = fields.Boolean(string="VAT 02,1%")

    has_vat_055 = fields.Boolean(string="VAT 05,5%")

    has_vat_100 = fields.Boolean(string="VAT 10,0%")

    has_vat_200 = fields.Boolean(string="VAT 20,0%")

    @api.depends("account_prefix", "account_suffix")
    def _compute_account_code(self):
        for wizard in self:
            wizard.account_code = (
                f"{wizard.account_prefix or ''}{wizard.account_suffix or ''}"
            )

    @api.onchange("is_vat_subject")
    def onchange_is_vat_subject(self):
        if not self.is_vat_subject:
            self.has_vat_000 = True
            self.has_vat_021 = False
            self.has_vat_055 = False
            self.has_vat_100 = False
            self.has_vat_200 = False

    @api.constrains(
        "is_vat_subject",
        "has_vat_000",
        "has_vat_021",
        "has_vat_055",
        "has_vat_100",
        "has_vat_200",
    )
    def check_vat_configuration(self):
        if self.is_vat_subject:
            if not any(
                [self.has_vat_021, self.has_vat_055, self.has_vat_100, self.has_vat_200]
            ):
                raise ValidationError(
                    _(
                        "If the consignor is VAT subject,"
                        " you should select at least a not null VAT."
                    )
                )
        else:
            if any(
                [self.has_vat_021, self.has_vat_055, self.has_vat_100, self.has_vat_200]
            ):
                raise ValidationError(
                    _(
                        "If the consignor is not VAT subject,"
                        " you should not select not null VAT."
                    )
                )
            if not self.has_vat_000:
                raise ValidationError(
                    _(
                        "If the consignor is not VAT subject,"
                        " you should select the null VAT."
                    )
                )

    # Action Section
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

        vat_amounts = []
        if self.has_vat_000:
            vat_amounts.append(0.0)
        if self.has_vat_021:
            vat_amounts.append(2.1)
        if self.has_vat_055:
            vat_amounts.append(5.5)
        if self.has_vat_100:
            vat_amounts.append(10.0)
        if self.has_vat_200:
            vat_amounts.append(20.0)
        for vat_amount in vat_amounts:
            tax = AccountTax.create(
                self._prepare_tax(sequence, account, partner, vat_amount)
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

    def _prepare_account(self):
        self.ensure_one()
        return {
            "name": self.consignor_name,
            "company_id": self.env.company.id,
            "code": self.account_code,
            "reconcile": True,
            "account_type": "income_other",
        }

    def _prepare_tax(self, sequence, account, partner, amount):
        self.ensure_one()
        return self._prepare_tax_model(
            sequence,
            account,
            partner,
            amount,
            self.is_vat_subject,
            self.consignor_name,
            self.env.company,
        )

    @api.model
    def _prepare_tax_model(
        self, sequence, account, partner, amount, is_vat_subject, partner_name, company
    ):
        return {
            "name": "{sequence} - {amount:.1f} -{vat_subject}{name}".format(
                sequence=sequence,
                amount=amount,
                vat_subject=is_vat_subject and " " or _(" NOT SUBJECT TO VAT - "),
                name=partner_name,
            ),
            "company_id": company.id,
            "description": is_vat_subject and f"{amount:.1f}%" or "0%",
            "amount": is_vat_subject and amount or 0.0,
            "amount_type": "percent",
            # for the time being, we have no B2B company with consignors
            "price_include": True,
            "invoice_repartition_line_ids": [
                (0, 0, {"repartition_type": "base"}),
                (0, 0, {"repartition_type": "tax", "account_id": account.id}),
            ],
            "refund_repartition_line_ids": [
                (0, 0, {"repartition_type": "base"}),
                (0, 0, {"repartition_type": "tax", "account_id": account.id}),
            ],
            "consignor_partner_id": partner.id,
        }

    def _prepare_fiscal_classification(self, sequence, partner, tax):
        self.ensure_one()
        return self._prepare_fiscal_classification_model(
            sequence,
            partner,
            tax,
            self.is_vat_subject,
            self.consignor_name,
            self.env.company,
        )

    def _prepare_fiscal_classification_model(
        self, sequence, partner, tax, is_vat_subject, partner_name, company
    ):
        return {
            "name": _("{sequence} - VAT {amount:2.1f}% -{vat_subject}{name}").format(
                sequence=sequence,
                amount=tax.amount,
                vat_subject=is_vat_subject and " " or _(" NOT SUBJECT TO VAT - "),
                name=partner_name,
            ),
            "sale_tax_ids": [(4, tax.id)],
            "consignor_partner_id": partner.id,
            "company_id": company.id,
        }

    def _prepare_partner(self, sequence, account):
        self.ensure_one()
        return {
            "name": f"{sequence} - {self.consignor_name}",
            "is_company": True,
            "consignment_account_id": account.id,
            "consignment_commission": self.commission_rate,
            "is_consignor": True,
        }
