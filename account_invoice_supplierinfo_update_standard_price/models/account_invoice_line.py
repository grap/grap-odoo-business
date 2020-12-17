# Copyright (C) 2018-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, models
from odoo.tools.float_utils import float_compare
from odoo.exceptions import Warning as UserError


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    @api.multi
    def _get_standard_price(self):
        self.ensure_one()
        if not self.product_id:
            return 0
        else:
            if self.invoice_id.product_expense_total != 0:
                line_shared_cost =\
                    self.invoice_id.distributed_expense_total * (
                        self.price_subtotal /
                        self.invoice_id.product_expense_total)
            else:
                raise UserError(_(
                    "We can't check prices"
                    " for a invoice whose total is null"))
            if self.quantity:
                line_shared_cost_per_unit = line_shared_cost / self.quantity
            else:
                line_shared_cost_per_unit = 0
            uom = self.uom_id or self.product_id.uom_id
            return self.invoice_id.currency_id.round(
                uom._compute_price(
                    line_shared_cost_per_unit + (
                        self.price_unit *
                        (1 - self.discount / 100) *
                        (1 - self.discount2 / 100) *
                        (1 - self.discount3 / 100)
                    ),
                    self.product_id.uom_id
                ))

    @api.multi
    def _is_correct_price(self, supplierinfo):
        self.ensure_one()
        DecimalPrecision = self.env['decimal.precision']
        res = super()._is_correct_price(supplierinfo)
        if not self.product_id:
            return res
        else:
            return res and not float_compare(
                self.product_id.standard_price,
                self._get_standard_price(),
                precision_digits=DecimalPrecision.precision_get('Product Price'))

    @api.multi
    def _prepare_supplier_wizard_line(self, supplierinfo):
        res = super()._prepare_supplier_wizard_line(supplierinfo)
        if self.product_id:
            res.update({
                'current_standard_price': self.product_id.standard_price,
                'new_standard_price': self._get_standard_price(),
            })
        return res
