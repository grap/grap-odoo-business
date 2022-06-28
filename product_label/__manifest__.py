# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Product Labels",
    "version": "12.0.1.1.5",
    "category": "Product",
    "author": "GRAP",
    "maintainers": ["legalsylvain", "quentinDupont"],
    "developpment_status": "Production/Stable",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": [
        "product",
    ],
    "data": [
        "security/res_groups.xml",
        "security/ir_rule.xml",
        "security/ir.model.access.csv",
        "views/view_product_product.xml",
        "views/view_product_template.xml",
        "views/view_product_label.xml",
    ],
    "demo": [
        "demo/res_groups.xml",
        "demo/product_label.xml",
        "demo/product_product.xml",
    ],
    "images": [
        "./static/description/product_label_kanban.png"
        "./static/description/product_label_form.png"
        "./static/description/product_template_form.png"
    ],
    "installable": True,
}
