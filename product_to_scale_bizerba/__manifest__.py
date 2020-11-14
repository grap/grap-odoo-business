# Copyright (C) 2016-Today GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Product - Send to Bizerba Scales (Retail Connect)',
    'summary': 'Synchronize Odoo database with Retail Connect Bizerba System',
    'version': "12.0.1.0.2",
    'category': 'Product',
    'author': 'GRAP, La Louve',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'product',
    ],
    'data': [
        'security/ir_module_category.xml',
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'data/ir_config_parameter.xml',
        'data/ir_cron.xml',
        'views/menu.xml',
        'views/view_product_product.xml',
        'views/view_uom_uom.xml',
        'views/view_product_scale_system.xml',
        'views/view_product_scale_group.xml',
        'views/view_product_scale_log.xml',
    ],
    'demo': [
        'demo/res_groups.xml',
        'demo/uom_uom.xml',
        'demo/product_scale_system.xml',
        'demo/product_scale_system_product_line.xml',
        'demo/product_scale_group.xml',
        'demo/product_product.xml',
        'demo/decimal_precision.xml',
    ],
    'installable': True,
}
