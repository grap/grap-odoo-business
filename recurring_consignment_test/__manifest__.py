# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Recurring Consignment - Test Module',
    'version': "12.0.1.0.2",
    'summary': 'Test module for Recurring_ Consignment Module',
    'category': 'Sale',
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'recurring_consignment',
        'l10n_generic_coa',
    ],
    'demo': [
        'demo/account_account.xml',
        'demo/res_partner.xml',
        'demo/account_tax.xml',
        'demo/account_product_fiscal_classification.xml',
        'demo/product_product.xml',
        'demo/account_tax_delayed.xml',
        'demo/account_invoice.xml',
        'demo/product_pricelist.xml',
    ],
    'installable': True,
}
