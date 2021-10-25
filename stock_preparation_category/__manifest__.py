# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Stock - Preparation Categories",
    "version": "12.0.1.1.1",
    "summary": "Manage Preparation Categories for stock moves",
    "category": "Stock",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": ["stock"],
    "data": [
        "security/ir_rule.xml",
        "security/ir_module_category.xml",
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "views/view_product_product.xml",
        "views/view_product_template.xml",
        "views/view_stock_preparation_category.xml",
        "views/view_stock_move.xml",
        "views/view_stock_picking.xml",
        "reports/report_stock_picking.xml",
    ],
    "demo": [
        "demo/stock_preparation_category.xml",
        "demo/product_product.xml",
        "demo/stock_picking.xml",
        "demo/res_groups.xml",
    ],
    "images": [
        "static/description/stock_preparation_category_tree.png",
        "static/description/product_template_form.png",
    ],
    "installable": True,
}
