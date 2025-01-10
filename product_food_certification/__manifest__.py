# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Products - Food Certification Informations",
    "version": "16.0.1.0.0",
    "category": "Sales",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": [
        "product_food",
    ],
    "data": [
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "views/view_certifier_organization.xml",
        "views/view_product_product.xml",
        "views/view_product_template.xml",
        "views/view_res_company.xml",
        "views/view_product_label.xml",
    ],
    "demo": [
        "demo/certifier_organization.xml",
        "demo/product_label.xml",
        "demo/res_company.xml",
    ],
    "installable": True,
}
