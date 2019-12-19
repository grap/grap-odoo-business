# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import json

from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError


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

    state_id_domain = fields.Char(compute="_compute_state_id_domain")

    origin_description = fields.Char(string="Origin Complement")

    maker_description = fields.Char(string="Maker")

    # Constrains section
    @api.multi
    @api.constrains("country_id", "state_id")
    def _check_origin_state_country(self):
        for product in self.filtered(lambda x: x.state_id and x.country_id):
            if (product.state_id.country_id != product.country_id):
                raise UserError(_("State must belong to the country."))

    # Compute section
    @api.depends("country_id")
    def _compute_state_id_domain(self):
        for product in self:
            if product.country_id:
                product.state_id_domain = json.dumps(
                    [("country_id", "=", product.country_id.id)])

    # Onchange section
    @api.onchange("country_id", "state_id")
    def onchange_product_origin(self):
        if self.state_id:
            self.country_id = self.state_id.country_id
