# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Employee - Direct Access to home information",
    "summary": "Prevent creation of many home partners at" " employee level.",
    "version": "16.0.1.0.3",
    "category": "base",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": ["hr"],
    "data": [
        "views/view_hr_employee.xml",
    ],
    "installable": True,
}
