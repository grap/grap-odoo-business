# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Account Invoice - Standard Price Update',
    'summary': 'In the supplier invoice, automatically update all products '
               'whose standard price on the line is different from '
               ' the product standard price',
    'version': "12.0.1.0.3",
    'category': 'Accounting & Finance',
    'author': 'GRAP',
    'license': 'AGPL-3',
    'depends': [
        'account_invoice_supplierinfo_update',
        'account_invoice_supplierinfo_update_triple_discount',
    ],
    'data': [
        'wizard/wizard_update_invoice_supplierinfo.xml',
        'views/view_account_invoice.xml',
        'views/view_product_template.xml',
    ],
    'demo': [
        'demo/account_account.xml',
        'demo/product_product.xml',
        'demo/account_invoice.xml',
    ],
    'images': [
        'static/description/wizard_form.png',
    ],
    'installable': True,
}
