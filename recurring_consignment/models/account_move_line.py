# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    # Columns Section
    consignment_invoice_line_id = fields.Many2one(
        string="Consignment Commission Invoice Line",
        comodel_name="account.move.line",
        index=True,
        help="Account move Line that commissions"
        " the current line, if the related product"
        " is a product related to consignor.",
    )
    consignment_invoice_line_ids = fields.One2many(
        comodel_name="account.move.line",
        inverse_name="consignment_invoice_line_id",
    )
