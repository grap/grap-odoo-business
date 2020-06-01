# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Sale - eShop",
    "version": "12.0.1.0.1",
    "summary": "Allow connection to Odoo eShop Project",
    "category": "Sale",
    "author": "GRAP",
    "license": "AGPL-3",
    "depends": [
        "sale",
        "product_label",
        "l10n_fr_department",
        "sale_recovery_moment",
        "product_origin_l10n_fr_department",
        "product_standard_margin",
        "queue_job",
    ],
    "data": [
        "security/ir_rule.xml",
        "security/ir_module_category.xml",
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "data/email_template.xml",
        "views/menu.xml",
        "views/view_eshop_category.xml",
        "views/view_product_product.xml",
        "views/view_uom_uom.xml",
        "views/view_res_company.xml",
        "views/view_res_partner.xml",
        "views/view_wizard_res_company_eshop_setting.xml",
    ],
    "demo": [
        "demo/res_company.xml",
        "demo/eshop_category.xml",
        "demo/account_tax.xml",
        "demo/product_product.xml",
        "demo/uom_uom.xml",
        "demo/res_users.xml",
        "demo/res_groups.xml",
        "demo/res_partner.xml",
    ],
    "installable": True,
}
