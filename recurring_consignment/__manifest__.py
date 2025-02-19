# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Recurring Consignment",
    "version": "16.0.2.1.1",
    "summary": "Sale - Handle Recurring Consignments",
    "category": "Sale",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": ["account_product_fiscal_classification"],
    "data": [
        "security/ir_module_category.xml",
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "views/menu.xml",
        "wizards/view_invoice_commission_wizard.xml",
        "wizards/view_consignor_create_wizard.xml",
        "views/view_account_move.xml",
        "views/view_account_tax.xml",
        "views/view_account_product_fiscal_classification.xml",
        "views/view_product_template.xml",
        "views/view_res_config_settings.xml",
        "views/view_res_partner.xml",
        "views/view_product_pricelist.xml",
        "report/report_account_invoice.xml",
    ],
    "demo": [
        "demo/res_company.xml",
        "demo/account_account.xml",
        "demo/account_journal.xml",
        "demo/res_partner.xml",
        "demo/account_tax.xml",
        "demo/account_product_fiscal_classification.xml",
        "demo/product_product.xml",
        "demo/product_pricelist.xml",
        "demo/account_move.xml",
        "demo/ir_property.xml",
    ],
    "post_init_hook": "create_consignor_sequence",
    "installable": True,
}
