# coding: utf-8
# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Stock - Preparation Categories',
    'version': '8.0.1.0.0',
    'summary': "Manage Preparation Categories for stock moves",
    'category': 'Stock',
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'stock',
        'web_widget_color',
    ],
    'data': [
        'security/ir_rule.xml',
        'security/ir_module_category.xml',
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/view_stock_preparation_category.xml',
        'views/view_product_product.xml',
        'views/view_stock_move.xml',
    ],
    'demo': [
        # 'demo/product_product.xml',
        'demo/stock_preparation_category.xml',
        'demo/res_groups.xml',
    ],
    'images': [
        'static/description/stock_preparation_category_tree.png',
    ],
    'installable': False,
}
