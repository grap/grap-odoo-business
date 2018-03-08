# coding: utf-8
# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Account Invoice - Standard Price Update',
    'summary': 'In the supplier invoice, automatically update all products '
               'whose standard price on the line is different from '
               ' the product standard price',
    'version': '8.0.1.0.0',
    'category': 'Accounting & Finance',
    'author': 'GRAP',
    'license': 'AGPL-3',
    'depends': [
        'account_invoice_supplierinfo_update',
        'account_invoice_supplierinfo_update_triple_discount',
    ],
    'installable': True,
    'data': [
        'wizard/wizard_update_invoice_supplierinfo.xml',
    ],
    'images': [
        'static/description/wizard_form.png',
    ],
}
