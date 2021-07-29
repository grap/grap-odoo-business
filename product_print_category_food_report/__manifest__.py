# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author: Quentin DUPONT (https://twitter.com/pondupont)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Product print category food report",
    "version": "12.0.1.1.1",
    "summary": "Food report like pricetags",
    "category": "Product",
    "author": "GRAP",
    "website": "http://www.grap.coop",
    "license": "AGPL-3",
    "depends": [
        "product_print_category",
        "product_food",
        "product_label",
        "product_notation",
        "product_origin",
        "product_origin_l10n_fr_department",
    ],
    "data": [
        "security/ir_rule.xml",
        "security/ir.model.access.csv",
        "report/qweb_pricetag_bulk_long.xml",
        "report/qweb_pricetag_bulk_square.xml",
        "report/qweb_pricetag_counter.xml",
        "report/qweb_pricetag_normal.xml",
        "report/qweb_pricetag_square.xml",
        "views/view_res_company.xml",
        "views/view_res_country_group.xml",
        "views/view_product_pricetag_type.xml",
        "views/view_product_product.xml",
        "views/view_uom_uom.xml",
        "data/product_print_category.xml",
        "data/res_country_group.xml",
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
