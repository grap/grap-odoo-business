# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author: Quentin DUPONT (quentin.dupont@grap.coop)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError

_logger = logging.getLogger(__name__)


class ProductProduct(models.Model):
    _inherit = "product.product"

    country_id = fields.Many2one(
        comodel_name="res.country",
        string="Country",
        help="Country of production of the product",
    )

    state_id = fields.Many2one(
        comodel_name="res.country.state",
        string="State",
        help="State of production of the product",
    )

    origin_description = fields.Char(string="Location (Complement)")

    maker_description = fields.Char(string="Maker")

    # Constrains section
    @api.multi
    @api.constrains("country_id", "state_id")
    def _check_origin_state_country(self):
        for product in self.filtered(lambda x: x.state_id and x.country_id):
            if product.state_id.country_id != product.country_id:
                raise UserError(_("State must belong to the country."))

    # Onchange section
    @api.onchange("state_id")
    def onchange_state_id(self):
        if self.state_id:
            self.country_id = self.state_id.country_id

    @api.onchange("country_id")
    def onchange_country_id(self):
        if self.state_id and self.state_id.country_id != self.country_id:
            self.state_id = False
