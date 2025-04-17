# Copyright (C) 2014-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Multi Company - Barcodes Module",
    "version": "12.0.1.1.2",
    "category": "Multi Company",
    "summary": "Handle Multi company for Barcodes Module",
    "author": "GRAP",
    "website": "https://github.com/grap/odoo-addons-multi-company",
    "license": "AGPL-3",
    "depends": [
        "barcodes",
        # GRAP
        "multi_company_base",
    ],
    "data": [
        "security/ir_rule.xml",
        "security/ir.model.access.csv",
        "views/view_barcode_nomenclature.xml",
        "views/view_barcode_rule.xml",
        "views/view_barcode_nomenclature_template.xml",
        "views/view_barcode_rule_template.xml",
    ],
    "demo": [
        "demo/barcode_nomenclature_template.xml",
        "demo/barcode_rule_template.xml",
    ],
    "installable": True,
}
