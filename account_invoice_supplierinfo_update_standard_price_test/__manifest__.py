# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Account Invoice - Standard Price Update (Test Module)",
    "summary": "Test module for the module"
    " account_invoice_supplierinfo_update_standard_price",
    "version": "12.0.1.0.3",
    "category": "Accounting & Finance",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": [
        "l10n_generic_coa",
        "account_invoice_supplierinfo_update_standard_price",
    ],
    "demo": [
        "demo/account_account.xml",
        "demo/product_product.xml",
        "demo/account_invoice.xml",
    ],
    "installable": True,
    "auto_install": True,
}
