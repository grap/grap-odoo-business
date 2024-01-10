# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author: Quentin DUPONT (https://twitter.com/pondupont)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Product print category food report",
    "version": "12.0.2.0.0",
    "summary": "Food report like pricetags",
    "category": "Product",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": [
        "product_print_category",
        "product_food",
        "product_label",
        "product_origin",
        "l10n_fr_department_product_origin",
    ],
    "data": [
        "security/ir_rule.xml",
        "security/ir.model.access.csv",
        "report/qweb_pricetag_bulk_long.xml",
        "report/qweb_pricetag_bulk_square.xml",
        "report/qweb_pricetag_counter.xml",
        "report/qweb_pricetag_normal.xml",
        "report/qweb_pricetag_normal_small.xml",
        "report/qweb_pricetag_normal_large.xml",
        "report/qweb_pricetag_square.xml",
        "report/qweb_pricetag_square_small.xml",
        "report/qweb_pricetag_square_large.xml",
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
