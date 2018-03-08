# coding: utf-8
# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models


class WizardUpdateInvoiceSupplierinfo(models.TransientModel):
    _inherit = 'wizard.update.invoice.supplierinfo'

    @api.multi
    def update_supplierinfo(self):
        self.ensure_one()
        res = super(
            WizardUpdateInvoiceSupplierinfo, self).update_supplierinfo()

        for line in self.line_ids.filtered(lambda x: x.product_id):
            line.product_id.standard_price = line.new_standard_price
        return res
