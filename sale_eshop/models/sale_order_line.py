# coding: utf-8
# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


import math

from openerp import _, api, models


class SaleOrderLine(models.Model):
    _name = 'sale.order.line'
    _inherit = ['sale.order.line', 'eshop.mixin']

    # Inherit Section
    _eshop_fields = [
        'product_id', 'product_uom', "price_unit", "tax_id",
        "discount", "product_uom_qty", "price_subtotal_gross",
        "price_subtotal",
    ]

    # API Section
    @api.model
    def eshop_custom_load_data(self, order_id):
        domain = [
            ('order_id', '=', order_id),
        ]
        items = self.eshop_load_data(domain)
        for item in items:
            tax_ids = item["tax_id"]
            product_uom_id = item["product_uom"]
            item.pop("tax_id")
            item.pop("product_uom")
            item["tax_ids"] = tax_ids
            item["product_uom_id"] = product_uom_id
        return items

    # Overload Section
    @api.multi
    def product_id_change(
            self, pricelist, product_id, qty=0,
            uom=False, qty_uos=0, uos=False, name='', partner_id=False,
            lang=False, update_tax=True, date_order=False, packaging=False,
            fiscal_position=False, flag=False):
        """
        Manage minimum / rounded quantity.
        return 'info' value instead of 'warning' value to avoid blocking
        message for end users.
        """
        is_eshop = self.env.user.has_group('sale_eshop.res_groups_is_eshop')
        infos = []
        computed_discount = False
        product = self.env['product.product'].browse(product_id)
        if qty and is_eshop and product_id:
            computed_discount = True
            discount = 0
            if product.eshop_minimum_qty:
                rounded_qty = self._eshop_round_value(product, qty)
                if qty < product.eshop_minimum_qty:
                    infos.append(_(
                        "'%.3f' is not a valid quantity for %s, the "
                        " minimum quantity is %'%.3f'. The quantity has"
                        " been automatically increased in your shopping"
                        " cart.") % (
                        qty, product.name, product.eshop_minimum_qty))
                    qty = product.eshop_minimum_qty
                else:
                    if qty != rounded_qty:
                        # The quantity has been rounded
                        infos.append(_(
                            "'%.3f' is not a valid quantity for %s, the"
                            " quantity has been rounded to '%.3f'.") % (
                            qty, product.name, rounded_qty))
                        qty = rounded_qty

        res = super(SaleOrderLine, self).product_id_change(
            pricelist, product_id, qty=qty, uom=uom,
            qty_uos=qty_uos, uos=uos, name=name, partner_id=partner_id,
            lang=lang, update_tax=update_tax, date_order=date_order,
            packaging=packaging, fiscal_position=fiscal_position,
            flag=flag)
        res['infos'] = infos
        res['value']['product_uom_qty'] =\
            res['value'].get('product_uom_qty', qty)
        if computed_discount:
            res['value']['discount'] = discount
        return res

    # Custom Section
    @api.model
    def _eshop_round_value(self, product, qty):
        rounded_qty = product.eshop_rounded_qty
        digit = len(str(float(rounded_qty) - int(rounded_qty)).split('.')[1])
        division = float(qty) / rounded_qty
        if division % 1 == 0:
            return qty
        else:
            return round(math.ceil(division) * rounded_qty, digit)
