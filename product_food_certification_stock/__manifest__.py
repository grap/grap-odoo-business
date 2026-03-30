# Copyright (C) 2025 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Product - Food Certification Informations - Stock",
    "version": "16.0.1.0.2",
    "category": "Sales",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": [
        # Odoo
        "stock",
        # GRAP
        "product_food_certification",
    ],
    "data": [
        "reports/report_stock_picking.xml",
    ],
    "demo": [
        "demo/product_product.xml",
    ],
    "installable": True,
    "auto_install": True,
}
