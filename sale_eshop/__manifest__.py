# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Sale - eShop",
    "version": "16.0.1.3.0",
    "summary": "Allow connection to Odoo eShop Project",
    "category": "Sale",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": [
        "sale_management",
        "social_media",
        # OCA
        "l10n_fr_department",
        "product_standard_margin",
        "queue_job",
        "product_compute_template_field_from_variant_helper",
        # GRAP
        "product_label",
        "product_maker",
        "sale_recovery_moment",
        "l10n_fr_department_product_origin",
        "base_company_legal_info",
        # CoopITeasy
        "customer_wallet",
        # Mollie https://github.com/mollie/mollie-odoo
        "payment_mollie_official",
    ],
    "external_dependencies": {"python": ["phonenumbers"]},
    "data": [
        "security/ir_rule.xml",
        "security/ir_module_category.xml",
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "data/queue_job_channel.xml",
        "data/queue_job_function.xml",
        "data/email_header.xml",
        "data/email_footer.xml",
        "data/email_create_account.xml",
        "data/email_lost_password.xml",
        "views/menu.xml",
        "views/view_eshop_category.xml",
        "views/view_eshop_fake_account.xml",
        "views/view_payment_portal_templates.xml",
        "views/view_product.xml",
        "views/view_uom_uom.xml",
        "views/view_res_company.xml",
        "views/view_res_partner.xml",
        "views/view_sale_order.xml",
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
    "assets": {
        # "web.assets_common": [
        #     "sale_eshop/static/src/scss/online_payment_portal.scss",
        # ],
        "web.assets_frontend": [
            "sale_eshop/static/src/scss/online_payment_portal.scss",
        ],
    },
    "installable": True,
}
