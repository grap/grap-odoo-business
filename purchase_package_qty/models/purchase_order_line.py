# coding: utf-8
# Copyright (C) 2013 - Today: GRAP (http://www.grap.coop)
# @author Julien WESTE
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from math import ceil

from openerp import _, api, models
from openerp.exceptions import Warning as UserError


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    # Constraints section
    @api.constrains('product_id', 'product_qty')
    def _check_purchase_qty(self):
        for line in self.filtered(
                lambda x: x.product_id and
                x.order_id.state not in ('draft', 'sent')):
            change, new_qty, package_qty, uom_name =\
                self._get_package_qty_info(
                    line.product_id, line.order_id.partner_id,
                    line.product_qty)
            if change:
                raise UserError(_("Package Error!"), _(
                    "You have to buy a multiple of the package  qty or change"
                    " the package settings in the supplierinfo of the product"
                    " for the following line:"
                    " \n - Product: %s;"
                    " \n - Unit Price: %s;"
                    " \n - Purchase Quantity: %s;"
                    " \n - Package Quantity: %s" % (
                        line.product_id.name, line.price_unit,
                        line.product_qty, package_qty)))

    # Views section
    @api.multi
    def onchange_product_id(
            self, pricelist_id, product_id, qty, uom_id, partner_id,
            date_order=False, fiscal_position_id=False, date_planned=False,
            name=False, price_unit=False, state='draft'):
        product_obj = self.env['product.product']
        res = super(PurchaseOrderLine, self).onchange_product_id(
            pricelist_id, product_id, qty, uom_id, partner_id,
            date_order=date_order, fiscal_position_id=fiscal_position_id,
            date_planned=date_planned, name=name, price_unit=price_unit,
            state=state)
        product = product_obj.browse(product_id)
        partner = partner_obj.browse(partner_id)
        if product and partner:
            change, new_qty, package_qty, uom_name =\
                self._get_package_qty_info(product, partner, qty)
            if change:
                res['warning'] = {
                    'title': _('Warning!'),
                    'message': _(
                        "The selected supplier only sells"
                        "this product by %s %s") % (package_qty, uom_name)}
                res['value'].update({'product_qty': new_qty})
        return res


    # Custom Section
    @api.model
    def _get_package_qty_info(self, product, partner, quantity):
        change = False
        new_qty = 0
        for supplierinfo in product.seller_ids.filtered(
                lambda x: x.name.id == partner.id):
            package_qty = supplierinfo.package_qty
            indicative = supplierinfo.indicative_package
            if (not(indicative) and
                    int(qty / package_qty) != qty / package_qty):
                change = True
                new_qty = ceil(qty / package_qty) * package_qty
        return change, new_qty, package_qty, uom_name
