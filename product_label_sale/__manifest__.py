# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Product Labels (Sale Glue Module)",
    "version": "12.0.1.1.1",
    "category": "Sales",
    "author": "GRAP",
    "maintainers": ["legalsylvain"],
    "developpment_status": "Production/Stable",
    "website": "http://www.grap.coop",
    "license": "AGPL-3",
    "depends": [
        "product_label",
        "sale",
    ],
    "data": [
        "report/report_sale_order.xml",
    ],
    "images": ["./static/description/report_sale_order.png"],
    "installable": True,
    "auto_install": True,
}
