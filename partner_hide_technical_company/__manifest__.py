# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Partner - Hide Companies Partners",
    "summary": "Hide partners created when creating companies.",
    "version": "16.0.1.1.0",
    "category": "base",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business",
    "license": "AGPL-3",
    "depends": ["partner_hide_technical_abstract"],
    "post_init_hook": "post_init_hook",
    "installable": True,
}
