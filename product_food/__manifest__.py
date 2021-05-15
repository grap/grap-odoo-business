# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Products - Food Informations",
    "version": "12.0.1.1.1",
    "category": "Sales",
    "author": "GRAP",
    "website": "http://www.grap.coop",
    "license": "AGPL-3",
    "depends": ["product_label", "product_origin"],
    "data": [
        "security/res_groups.xml",
        "security/ir_rule.xml",
        "security/ir.model.access.csv",
        "views/view_certifier_organization.xml",
        "views/view_product_label.xml",
        "views/view_product_allergen.xml",
        "views/view_product_category.xml",
        "views/view_product_product.xml",
        "views/view_product_template.xml",
        "views/view_res_company.xml",
    ],
    "demo": [
        "demo/res_groups.xml",
        "demo/certifier_organization.xml",
        "demo/product_label.xml",
        "demo/product_allergen.xml",
        "demo/product_category.xml",
        "demo/product_product.xml",
    ],
    "images": [
        "static/description/certifier_organization_form.png",
        "static/description/product_allergen_form.png",
    ],
    "installable": True,
}
