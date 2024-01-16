# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Sale - eShop",
    "version": "12.0.2.0.0",
    "summary": "Allow connection to Odoo eShop Project",
    "category": "Sale",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": [
        "sale",
        "social_media",
        # OCA
        "l10n_fr_department",
        "product_standard_margin",
        "queue_job",
        # GRAP
        "product_label",
        "sale_recovery_moment",
        "l10n_fr_department_product_origin",
    ],
    "data": [
        "security/ir_rule.xml",
        "security/ir_module_category.xml",
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "data/queue_job_channel.xml",
        "data/queue_job_function.xml",
        "data/email_template.xml",
        "views/menu.xml",
        "views/view_eshop_category.xml",
        "views/view_eshop_fake_account.xml",
        "views/view_product_product.xml",
        "views/view_uom_uom.xml",
        "views/view_res_company.xml",
        "views/view_res_partner.xml",
        "views/view_wizard_res_company_eshop_setting.xml",
    ],
    "demo": [
        "demo/ir_config_parameter.xml",
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
