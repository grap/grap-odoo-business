# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "GRAP - Custom Qweb Reports",
    "version": "12.0.1.0.0",
    "category": "GRAP - Custom",
    "author": "GRAP",
    "website": "http://www.grap.coop",
    "license": "AGPL-3",
    "depends": [
        "product_print_category",
    ],
    "data": [
        "security/ir_rule.xml",
        "security/ir.model.access.csv",
        "report/qweb_template_product_product.xml",
        "views/action.xml",
        "views/menu.xml",
        "views/view_res_company.xml",
        "views/view_product_pricetag_type.xml",
        "views/view_product_product.xml",
        "views/view_uom_uom.xml",
        "data/product_print_category.xml",
    ],
    "demo": [
        "demo/res_groups.xml",
        "demo/uom_uom.xml",
        "demo/product_pricetag_type.xml",
        "demo/product_product.xml",
        "demo/product_print_category.xml",
    ],
    "installable": True,
}
