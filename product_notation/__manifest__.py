# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Product Notation",
    "version": "12.0.3.0.0",
    "category": "Product",
    "author": "GRAP",
    "website": "http://www.grap.coop",
    "license": "AGPL-3",
    "depends": [
        "product",
    ],
    "data": [
        "views/templates.xml",
        "views/view_product_product.xml",
    ],
    "demo": [
        "demo/product_product.xml",
    ],
    "external_dependencies": {
        "python": ["cairosvg"],
    },
    "images": [
        "static/description/product_product_form.png",
    ],
    "installable": True,
}
