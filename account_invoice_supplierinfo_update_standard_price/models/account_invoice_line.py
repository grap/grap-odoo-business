# coding: utf-8
# Copyright (C) 2018-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import _, api, models
from openerp.tools.float_utils import float_compare
from openerp.exceptions import Warning as UserError


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    @api.multi
    def _get_standard_price(self):
        self.ensure_one()
        if not self.product_id:
            return 0
        else:
            factor = 1
            if self.uos_id and self.uos_id.id != self.product_id.uom_id.id:
                # Making conversion
                factor =\
                    self.uos_id.factor_inv\
                    / self.product_id.uom_id.factor_inv
            if self.invoice_id.product_expense_total != 0:
                line_shared_cost =\
                    self.invoice_id.distributed_expense_total * (
                        self.price_subtotal /
                        self.invoice_id.product_expense_total)
            else:
                raise UserError(_(
                    "We can't check prices"
                    " for a invoice whose total is null"))
            return (
                line_shared_cost / self.quantity + (
                    self.price_unit *
                    (1 - self.discount / 100) *
                    (1 - self.discount2 / 100) *
                    (1 - self.discount3 / 100))
                ) / factor

    @api.multi
    def _is_correct_partner_info(self, partnerinfo):
        self.ensure_one()
        precision_obj = self.env['decimal.precision']
        res = super(AccountInvoiceLine, self)._is_correct_partner_info(
            partnerinfo)
        if not self.product_id:
            return res
        else:
            return res and not float_compare(
                self.product_id.standard_price,
                self._get_standard_price(),
                precision_digits=precision_obj.precision_get('Product Price'))

    @api.multi
    def _prepare_supplier_wizard_line(self, supplierinfo, partnerinfo):
        res = super(AccountInvoiceLine, self)._prepare_supplier_wizard_line(
            supplierinfo, partnerinfo)
        if self.product_id:
            res.update({
                'current_standard_price': self.product_id.standard_price,
                'new_standard_price': self._get_standard_price(),
            })
        return res
