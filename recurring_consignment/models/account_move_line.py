# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    # Columns Section
    consignment_invoice_id = fields.Many2one(
        string="Consignment Commission Invoice", comodel_name="account.invoice"
    )

    consignment_commission = fields.Float(string="Consignment Commission Rate")

    @api.constrains("consignment_invoice_id")
    def _check_consignment_invoice_id(self):
        for line in self.filtered(lambda x: x.consignment_invoice_id):
            if line.account_id != line.consignment_invoice_id.account_id:
                raise UserError(
                    _(
                        "You try to create a commission invoice for the account %s,"
                        " with lines with account %s."
                    )
                    % (
                        line.account_id.display_name,
                        line.consignment_invoice_id.account_id.display_name,
                    )
                )
