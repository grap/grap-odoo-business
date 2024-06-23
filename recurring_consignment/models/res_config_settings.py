# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    commission_product_id = fields.Many2one(
        comodel_name="product.product",
        related="company_id.commission_product_id",
        readonly=False,
        help="Product that will be used to generate"
        " consignment invoices to consignors.",
    )

    commission_deduction_journal_id = fields.Many2one(
        comodel_name="account.journal",
        related="company_id.commission_deduction_journal_id",
        readonly=False,
        help="Miscellaneous Journal, used to generate an entry"
        " that deducts the commission from the amount to be paid out.",
    )

    recurring_consignment_account_prefix = fields.Char(
        related="company_id.recurring_consignment_account_prefix",
        readonly=False,
        help="Code used as prefix to generate account code of the consignors.",
    )
