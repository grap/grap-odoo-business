# Copyright (C) 2022 - Today: GRAP (http://www.grap.coop)
# @author: Quentin Dupont (quentin.dupont@grap.coop)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "MRP BoM Product Allergen",
    "summary": "Handle Product allergens on MRP BoM and BoM Lines.",
    "version": "16.0.1.0.1",
    "category": "Manufacturing",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": [
        "mrp",
        # GRAP Business modules,
        "product_food",
    ],
    "demo": [
        "demo/product.xml",
        "demo/bom.xml",
    ],
    "data": [
        "views/view_mrp_bom.xml",
        "views/view_product_allergen.xml",
    ],
    "installable": True,
}
