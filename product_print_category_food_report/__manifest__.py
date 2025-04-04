# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author: Quentin DUPONT (https://twitter.com/pondupont)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Product print category food report",
    "version": "16.0.1.0.0",
    "summary": "Food report like pricetags",
    "category": "Product",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": [
        # OCA
        "product_print_category",
        "product_net_weight",
        "product_uom_measure_type",
        # GRAP
        "product_maker",
        "product_label",
        "product_origin",
        "product_food",
        "product_food_certification",
        "l10n_fr_department_product_origin",
    ],
    "data": [
        "security/ir_rule.xml",
        "security/ir.model.access.csv",
        "report/qweb_components.xml",
        "report/qweb_template_pricetag_template_A.xml",
        "report/qweb_template_pricetag_template_B.xml",
        "report/qweb_template_pricetag_template_C.xml",
        "report/qweb_template_pricetag_01.xml",
        "report/qweb_template_pricetag_02.xml",
        "report/qweb_template_pricetag_10.xml",
        "report/qweb_template_pricetag_11.xml",
        "report/qweb_template_pricetag_12.xml",
        "report/qweb_template_pricetag_20.xml",
        "report/qweb_template_pricetag_30.xml",
        "report/qweb_template_pricetag_31.xml",
        "report/qweb_template_pricetag_32.xml",
        "report/qweb_template_pricetag_33.xml",
        "report/qweb_template_pricetag_40.xml",
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
    "assets": {
        "web.report_assets_common": [
            'product_print_category_food_report/static/src/scss/**',
            # Uncomment the following line to debug
            # 'product_print_category_food_report/static/src/scss-debug/**',
        ],
    },
    "installable": True,
}
