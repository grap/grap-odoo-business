# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, models
from odoo.exceptions import Warning as UserError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Constrains Section
    @api.constrains('is_consignment_commission', 'available_in_pos')
    def _check_is_consignment_commission_pos(self):
        if self.filtered(
                lambda x: x.is_consignment_commission and x.available_in_pos):
            raise UserError(_(
                "A Consignment Commission can not be available in PoS"))

    @api.multi
    def _check_consignor_changes(self, vals):
        super()._check_consignor_changes(vals)
        PosOrderLine = self.env['pos.order.line']
        if vals.get('consignor_partner_id', False):
            for template in self:
                product_ids = template.product_variant_ids.ids
                if template.consignor_partner_id.id !=\
                        vals.get('consignor_partner_id', False):
                    order_lines = PosOrderLine.search([
                        ('product_id', 'in', product_ids)])
                    if len(order_lines):
                        raise UserError(_(
                            "You can not change the value of the field"
                            " 'Consignor' because the product is associated"
                            " to one or more PoS Order Lines. You should"
                            " disable the product and create a new one."))
