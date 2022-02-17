# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Sale - Recovery Moments",
    "version": "12.0.1.1.2",
    "summary": "Manage Recovery Moments and Places for Sale Order",
    "category": "Sale",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": [
        "sale_stock",
    ],
    "data": [
        "security/ir_rule.xml",
        "security/ir_module_category.xml",
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "data/ir_sequence.xml",
        "views/view_sale_order.xml",
        "views/view_stock_picking.xml",
        "wizards/view_sale_recovery_moment_wizard_duplicate.xml",
        "wizards/view_sale_recovery_moment_group_wizard_duplicate.xml",
        "views/view_sale_recovery_moment.xml",
        "views/view_sale_recovery_moment_group.xml",
        "views/view_sale_recovery_place.xml",
    ],
    "demo": [
        "demo/product_product.xml",
        "demo/sale_recovery_place.xml",
        "demo/sale_recovery_moment_group.xml",
        "demo/sale_recovery_moment.xml",
        "demo/sale_order.xml",
        "demo/res_groups.xml",
    ],
    "images": [
        "static/description/sale_recovery_place_tree.png",
        "static/description/sale_recovery_moment_group_form.png",
        "static/description/sale_recovery_moment_calendar.png",
    ],
    "installable": True,
}
