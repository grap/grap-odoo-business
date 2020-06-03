# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class ProductLabel(models.Model):
    _name = "product.label"
    _inherit = ["product.label", "eshop.with.image.mixin"]

    # Inherit Section
    _eshop_invalidation_type = "multiple"

    _eshop_fields = ["name", "code", "image", "image_medium", "image_small"]

    _eshop_image_fields = ["image", "image_medium", "image_small"]
