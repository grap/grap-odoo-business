# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Origin Information for Products",
    "version": "12.0.1.0.0",
    "category": "Sales",
    "author": "GRAP",
    "website": "http://www.grap.coop",
    "license": "AGPL-3",
    "depends": [
        "product",
        # TODO Wait for https://github.com/OCA/web/issues/1464
        # "web_domain_field",
    ],
    "data": [
        "views/view_product_product.xml",
    ],
    "demo": [
        "demo/product_product.xml",
    ],
    "images": [
    ],
    "installable": True,
}
