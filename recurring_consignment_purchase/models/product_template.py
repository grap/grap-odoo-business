# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, models
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.multi
    def _check_consignor_changes(self, vals):
        super()._check_consignor_changes(vals)
        PurchaseOrderLine = self.env['purchase.order.line']
        if vals.get('consignor_partner_id', False):
            for template in self:
                product_ids = template.product_variant_ids.ids
                if template.consignor_partner_id.id !=\
                        vals.get('consignor_partner_id', False):
                    order_lines = PurchaseOrderLine.search([
                        ('product_id', 'in', product_ids)])
                    if len(order_lines):
                        raise UserError(_(
                            "You can not change the value of the field"
                            " 'Consignor' because the product is associated"
                            " to one or more Purchase Order Lines. You should"
                            " disable the product and create a new one."))
