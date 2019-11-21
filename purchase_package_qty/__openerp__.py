# coding: utf-8
# Copyright (C) 2013 - Today: GRAP (http://www.grap.coop)
# @author Julien WESTE
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Purchase - Package Quantity',
    'version': '8.0.2.0.0',
    'category': 'Purchase',
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'purchase',
    ],
    'data': [
        'views/view_product_supplierinfo.xml',
    ],
    'demo': [
        'demo/product_template.xml',
        'demo/purchase_order.xml',
    ],
    'installable': False,
}
