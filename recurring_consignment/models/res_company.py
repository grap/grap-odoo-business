# Copyright (C) 2020 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ResCompany(models.Model):
    _inherit = "res.company"

    commission_product_id = fields.Many2one(
        comodel_name="product.product",
        domain="[('detailed_type', '=', 'service')]",
        help="Used for the Recurring Consignment features."
        " Define the product that will be used to generate"
        " consignment invoices to consignors.",
    )

    commission_deduction_journal_id = fields.Many2one(
        comodel_name="account.journal",
        domain="[('type', '=', 'general')]",
        help="Miscellaneous Journal, used to generate an entry"
        " that deducts the commission from the amount to be paid out.",
    )

    recurring_consignment_account_prefix = fields.Char(
        help="Code used as prefix to generate account code of the consignors."
    )

    @api.model_create_multi
    def create(self, vals_list):
        companies = super().create(vals_list)
        companies._create_consignor_sequence()
        return companies

    def _create_consignor_sequence(self):
        ResPartner = self.env["res.partner"]
        Irsequence = self.env["ir.sequence"]
        for company in self:
            _logger.info(
                "Creating consignor sequence for company '%s'" % (company.name)
            )
            current_consignor_qty = len(
                ResPartner.with_context(active_test=False).search(
                    [
                        ("company_id", "=", company.id),
                        ("is_consignor", "=", True),
                    ]
                )
            )
            Irsequence.create(
                company._prepare_consignor_sequence(current_consignor_qty)
            )

    def _prepare_consignor_sequence(self, current_consignor_qty):
        self.ensure_one()
        return {
            "name": "Consignor sequence",
            "code": "consignor.create.wizard",
            "implementation": "no_gap",
            "company_id": self.id,
            "prefix": "Prod",
            "padding": 3,
            "number_next_actual": current_consignor_qty + 1,
        }
