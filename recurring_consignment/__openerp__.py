# coding: utf-8
# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Recurring Consignment',
    'version': '8.0.2.0.0',
    'summary': 'Sale - Handle Recurring Consignment',
    'category': 'Sale',
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'account_product_fiscal_classification',
        'purchase',
        'account_voucher',
        'point_of_sale',
        'sale',
        'report_webkit',
    ],
    'data': [
        'security/ir_module_category.xml',
        'security/res_groups.xml',
        'report/qweb_template_account_invoice_consignment.xml',
        'report/ir_actions_report_xml.xml',
        'views/action_popup.xml',
        'views/view_account_invoice.xml',
        'views/view_account_tax.xml',
        'views/view_account_tax_code.xml',
        'views/view_account_product_fiscal_classification.xml',
        'views/view_product_product.xml',
        'views/view_product_template.xml',
        'views/view_invoice_commission_wizard.xml',
        'views/view_res_partner.xml',
        'views/view_product_pricelist.xml',
        'views/action.xml',
        'views/menu.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/res_groups.xml',
        'demo/account_account.xml',
        'demo/res_partner.xml',
        'demo/account_tax_code.xml',
        'demo/account_tax.xml',
        'demo/account_product_fiscal_classification.xml',
        'demo/product_product.xml',
        'demo/account_invoice.xml',
        'demo/product_pricelist.xml',
        'demo/sale_order.xml',

    ],
    'installable': True,
}
