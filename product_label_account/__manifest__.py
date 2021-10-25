# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Product Labels (Invoice Glue Module)",
    "version": "12.0.1.1.3",
    "category": "Account",
    "author": "GRAP",
    "maintainers": ["legalsylvain", "quentinDupont"],
    "developpment_status": "Production/Stable",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": [
        "product_label",
        "account",
    ],
    "data": [
        "report/report_account_invoice.xml",
    ],
    "images": ["./static/description/report_account_invoice.png"],
    "installable": True,
    "auto_install": True,
}
