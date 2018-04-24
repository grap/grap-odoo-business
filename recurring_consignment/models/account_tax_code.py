# coding: utf-8
# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError


class AccountTaxCode(models.Model):
    _inherit = 'account.tax.code'

    # Columns Section
    consignment_product_id = fields.Many2one(
        string='Consignment Product', comodel_name='product.product',
        domain="[('is_consignment_commission', '=', True)]",
        help="Set a 'Sales commission' product for consignment sales.\n"
        "If not set, transaction will not be commissioned. (this case is"
        " usefull to avoid to commission taxes transaction, because in"
        " most cases, commissions are computed on without taxes amount).")

    @api.constrains('consignment_product_id')
    def _check_consignment_product_id(self):
        for tax_code in self.filtered(lambda x: x.consignment_product_id):
            if not tax_code.consignment_product_id.is_consignment_commission:
                raise UserError(_(
                    "Set only consignement commission product in the"
                    " according field"))
