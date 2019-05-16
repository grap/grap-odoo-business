# coding: utf-8
# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Product - Update Standard Price',
    'summary': 'Possibility to update standard price of a product, based'
               ' on supplier infos, discount, etc...',
    'version': '8.0.1.0.0',
    'category': 'Purchase',
    'author': 'GRAP',
    'license': 'AGPL-3',
    'depends': [
        'product_supplierinfo_triple_discount',
    ],
    'data': [
        'views/view_product_template.xml',
        'views/view_product_supplierinfo.xml',
    ],
    'demo': [
        'demo/res_groups.xml',
        'demo/pricelist_partnerinfo.xml',
    ],
    'images': [
    ],
    'installable': True,
}
