# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author: Quentin DUPONT (https://twitter.com/pondupont)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Product print category food report",
    "version": "12.0.3.0.0",
    "summary": "Food report like pricetags",
    "category": "Product",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": [
        # OCA
        "product_print_category",
        "product_net_weight",
        # GRAP
        "product_label",
        "product_origin",
        "product_food",
        "product_food_certification",
        "l10n_fr_department_product_origin",
    ],
    "data": [
        "security/ir_rule.xml",
        "security/ir.model.access.csv",
        "report/qweb_reports.xml",
        "report/qweb_components.xml",
        "report/qweb_template_pricetag_template_A.xml",
        "report/qweb_template_pricetag_template_B.xml",
        "report/qweb_template_pricetag_01.xml",
        "report/qweb_template_pricetag_02.xml",
        "report/qweb_template_pricetag_10.xml",
        "report/qweb_template_pricetag_11.xml",
        "report/qweb_template_pricetag_12.xml",
        # "report/qweb_pricetag_bulk_long.xml",
        # "report/qweb_pricetag_bulk_square.xml",
        # "report/qweb_pricetag_counter.xml",
        # "report/qweb_pricetag_normal_large.xml",
        # "report/qweb_pricetag_square_large.xml",
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
    ],
    "installable": True,
}
