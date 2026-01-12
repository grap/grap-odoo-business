# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Quentin Dupont (quentin.dupont@grap.coop)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "MRP Product Price Quick Menus",
    "summary": "Adds menus to help manage price between BoMs and Products.",
    "version": "16.0.1.2.0",
    "category": "GRAP - Business",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": [
        # OCA
        "mrp_product_characterisation",
        "mrp_bom_product_price_margin",
        "product_margin_classification",
        # GRAP
        "product_standard_price_change_date",
    ],
    "data": [
        "views/view_mrp_bom.xml",
        "views/view_product_product.xml",
        "views/menu.xml",
    ],
    "installable": True,
}
