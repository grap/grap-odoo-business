# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT (quentin.dupont@grap.coop)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Product Labels MRP",
    "summary": "Adds labels in MRP BoMs",
    "version": "16.0.1.0.0",
    "category": "Product",
    "author": "GRAP",
    "maintainers": ["quentinDupont"],
    "developpment_status": "Production/Stable",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": [
        "mrp",
        "product",
        # OCA
        "product_label",
    ],
    "data": [
        "views/view_mrp_bom.xml",
    ],
    "installable": True,
    "auto-install": True,
}
