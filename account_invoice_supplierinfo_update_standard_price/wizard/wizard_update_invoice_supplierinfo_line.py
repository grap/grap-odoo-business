# coding: utf-8
# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models
import openerp.addons.decimal_precision as dp


class WizardUpdateInvoiceSupplierinfoLine(models.TransientModel):
    _inherit = 'wizard.update.invoice.supplierinfo.line'

    current_standard_price = fields.Float(
        string='Current Standard Price', readonly=True,
        digits=dp.get_precision('Product Price'))

    new_standard_price = fields.Float(
        string='New Standard Price',
        digits=dp.get_precision('Product Price'))
