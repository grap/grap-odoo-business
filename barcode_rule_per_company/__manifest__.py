# Copyright (C) 2014-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Barcodes Rule Per Company",
    "version": "16.0.1.0.0",
    "category": "Multi Company",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": ["barcodes"],
    "data": [
        "security/ir_rule.xml",
        "views/view_barcode_nomenclature.xml",
        "views/view_barcode_rule.xml",
    ],
    "installable": True,
}
