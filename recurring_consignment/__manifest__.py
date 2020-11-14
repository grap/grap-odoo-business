# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Recurring Consignment',
    'version': "12.0.1.0.15",
    'summary': 'Sale - Handle Recurring Consignment',
    'category': 'Sale',
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'account_product_fiscal_classification',
    ],
    'data': [
        'security/ir_module_category.xml',
        'security/res_groups.xml',
        'views/menu.xml',
        'wizards/view_invoice_commission_wizard.xml',
        'wizards/view_consignor_create_wizard.xml',
        # 'views/view_account_invoice.xml',
        'views/view_account_tax.xml',
        'views/view_account_product_fiscal_classification.xml',
        'views/view_product_template.xml',
        'views/view_res_partner.xml',
        'views/view_product_pricelist.xml',
        'report/report_account_invoice.xml',
    ],
    'demo': [
        'demo/res_groups.xml',
    ],
    'post_init_hook': 'create_consignor_sequence',
    'installable': True,
}
