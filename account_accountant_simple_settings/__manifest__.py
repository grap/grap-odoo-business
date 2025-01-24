# Copyright (C) 2020 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Accountant - Simple Settings",
    "summary": "Allow accountants to make some simple accounting configuration"
    " without having administration rights.",
    "version": "16.0.1.0.1",
    "category": "Accounting",
    "author": "GRAP",
    "maintainers": ["legalsylvain"],
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": ["account", "base_setup"],
    "data": [
        "security/ir.model.access.csv",
        "views/view_account_config_settings.xml",
    ],
}
