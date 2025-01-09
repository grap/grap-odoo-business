# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Products - Food Informations",
    "version": "16.0.1.0.0",
    "category": "Sales",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": [
        # OCA
        "product_usability",
        "product_compute_template_field_from_variant_helper",
        # GRAP
        "product_label",
    ],
    "data": [
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "views/view_product_label.xml",
        "views/view_product_allergen.xml",
        "views/view_product_category.xml",
        "views/view_product_product.xml",
        "views/view_product_template.xml",
    ],
    "demo": [
        "demo/product_label.xml",
        "demo/product_allergen.xml",
        "demo/product_category.xml",
        "demo/product_product.xml",
    ],
    "installable": True,
}
