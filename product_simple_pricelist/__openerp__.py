# coding: utf-8
# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Product - Simple Pricelist',
    'summary': 'Provides Wizard to manage easily Pricelist By Products',
    'version': '8.0.2.0.0',
    'category': 'Product',
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'product',
    ],
    'data': [
        'security/ir_rule.xml',
        'security/ir.model.access.xml',
        'views/view_product_simple_pricelist_item_update_wizard.xml',
        'views/view_product_simple_pricelist_item.xml',
        'views/view_product_pricelist.xml',
    ],
    'installable': True,
}
