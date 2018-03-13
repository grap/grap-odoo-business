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
        'security/ir_module_category.yml',
        'security/res_groups.yml',
        'security/ir_model_access.yml',
        'view/view.xml',
        'view/view_res_company.xml',
        'view/action.xml',
        'view/menu.xml',
    ],
    'demo': [
        'demo/res_groups.xml',
        'demo/product_label.xml',
        'demo/product_pricetag_type.xml',
        'demo/function.xml',
    ],
    'css': [
        'static/src/css/css.css',
    ],
    'external_dependencies': {
        'python': ['cairosvg'],
    },
    'installable': True,
}
