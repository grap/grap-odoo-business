# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Recurring Consignment for Purchase",
    "version": "12.0.1.1.1",
    "summary": "Glue module for Recurring Consignment and Purchase modules",
    "category": "Sale",
    "author": "GRAP",
    "website": "http://www.grap.coop",
    "license": "AGPL-3",
    "depends": [
        "recurring_consignment",
        "purchase",
        "stock",
    ],
    "data": ["views/view_purchase_order.xml"],
    "installable": True,
    "auto_install": True,
}
