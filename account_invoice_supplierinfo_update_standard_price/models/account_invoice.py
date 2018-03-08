# -*- coding: utf-8 -*-
# Copyright (C) 2018-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models, api
import openerp.addons.decimal_precision as dp


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    product_expense_total = fields.Float(
        string='Product Expenses Total',
        compute='_compute_expense_total',
        digits=dp.get_precision('Product Price'),
        multi='expense_total', store=True)

    distributed_expense_total = fields.Float(
        string='Distributed Expenses Total',
        compute='_compute_expense_total',
        digits=dp.get_precision('Product Price'),
        multi='expense_total', store=True)

    @api.multi
    @api.depends(
        'invoice_line.product_id.is_impact_standard_price',
        'invoice_line.price_subtotal')
    def _compute_expense_total(self):
        for invoice in self.filtered(lambda x: x.type == 'in_invoice'):
            invoice.update({
                'product_expense_total': sum(
                    invoice.invoice_line.
                        filtered(lambda x:
                            not x.product_id or
                            not x.product_id.is_impact_standard_price).
                        mapped('price_subtotal')),
                'distributed_expense_total': sum(
                    invoice.invoice_line.
                        filtered(lambda x:
                            x.product_id and
                            x.product_id.is_impact_standard_price).
                        mapped('price_subtotal')),
            })
