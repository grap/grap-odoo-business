# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Product Labels",
    "version": "12.0.1.0.0",
    "category": "Sales",
    "author": "GRAP",
    "website": "http://www.grap.coop",
    "license": "AGPL-3",
    "depends": [
        "product",
        "sale",
    ],
    "data": [
        "security/res_groups.xml",
        "security/ir_rule.xml",
        "security/ir.model.access.csv",
        "views/view_product_product.xml",
        "views/view_product_template.xml",
        "views/view_product_label.xml",
        "report/report_account_invoice.xml",
        "report/report_sale_order.xml",
    ],
    "demo": [
        "demo/res_groups.xml",
        "demo/product_label.xml",
        "demo/product_product.xml",
    ],
    "images": [
    ],
    "installable": True,
}
