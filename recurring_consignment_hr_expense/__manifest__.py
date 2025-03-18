# Copyright (C) 2025-Today GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Account Product - Fiscal Classification - Recurring consignment",
    "summary": "Glue module between Recurring consignment and fiscal classification",
    "version": "16.0.1.1.0",
    "category": "Accounting",
    "author": "GRAP,Odoo Community Association (OCA)",
    "maintainers": ["legalsylvain"],
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": [
        "recurring_consignment",
        "account_product_fiscal_classification_hr_expense",
    ],
    "excludes": ["product_tax_multicompany_default"],
    "data": ["views/view_product_product.xml"],
    "installable": True,
    "auto_install": True,
}
