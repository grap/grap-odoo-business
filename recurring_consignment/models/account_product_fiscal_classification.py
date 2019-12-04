# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError


class AccountProductFiscalClassification(models.Model):
    _inherit = 'account.product.fiscal.classification'

    # Columns Section
    consignor_partner_id = fields.Many2one(
        string='Consignor', comodel_name='res.partner',
        domain="[('is_consignor', '=', True)]")

    # Constrains Section
    @api.constrains('purchase_tax_ids', 'sale_tax_ids', 'consignor_partner_id')
    def _check_consignor_tax_ids(self):
        for fiscal_classification in self:
            if (fiscal_classification.consignor_partner_id and
                    len(fiscal_classification.purchase_tax_ids)):
                raise UserError(_(
                    "You can not set Supplier Taxes for Fiscal Classification"
                    "used for consignment"))
