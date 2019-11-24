# Copyright (C) 2018-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_impact_standard_price = fields.Boolean(
        string='Impact Standard Price', help="Check this box if you want"
        " that purchasing this product impact the standard price of the"
        " products purchased with that product.\n"
        "A typical case is for Landing Cost.")
