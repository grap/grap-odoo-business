# coding: utf-8
# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Sale - Food Information for Products',
    'version': '8.0.3.0.0',
    'category': 'Sales',
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'product',
        'l10n_fr_department',
    ],
    'data': [
        'security/ir_rule.xml',
        'security/ir_module_category.xml',
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/view_certifier_organization.xml',
        'views/view_product_label.xml',
        'views/view_product_product.xml',
        'views/view_res_company.xml',
        'views/action.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/res_groups.xml',
        'demo/product_label.xml',
        'demo/product_product.xml',
    ],
    'css': [
        'static/src/css/css.css',
    ],
    'external_dependencies': {
        'python': ['cairosvg'],
    },
    'installable': True,
}
