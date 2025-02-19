# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Recurring Consignment - Point of Sale",
    "version": "16.0.1.0.0",
    "summary": "Glue module for Recurring Consignment and PoS modules",
    "category": "Sale",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": [
        # Odoo
        "point_of_sale",
        # GRAP
        "recurring_consignment",
    ],
    "data": ["views/view_account_move.xml"],
    "demo": [
        "demo/product_product.xml",
        "demo/account_journal.xml",
        "demo/pos_payment_method.xml",
        "demo/pos_config.xml",
    ],
    "installable": True,
    "auto_install": True,
}
