# Copyright (C) 2013 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Product Category - Recursive property',
    'version': "12.0.1.0.1",
    'summary': "Propagate recursively properties for product category",
    'category': 'Product',
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'stock_account',
    ],
    'demo': [
        'demo/account_account.xml',
        'demo/product_category.xml',
    ],
    'installable': True,
}
