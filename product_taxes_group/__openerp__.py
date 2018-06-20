# coding: utf-8
# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Product - Taxes Group - OBSOLETE',
    'summary': 'Simplify taxes management for products with Taxes Group',
    'version': '8.0.6.0.0',
    'category': 'product',
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'stock',
        'account_product_fiscal_classification',
        'recurring_consignment',
    ],
    'data': [
        'security/ir_model_access.yml'
    ],
    'installable': True,
}
