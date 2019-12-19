# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import json

from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError


class ProductProduct(models.Model):
    _inherit = "product.product"

    department_id = fields.Many2one(
        comodel_name="res.country.department",
        string="Department",
        help="Department of production of the product",
    )

    department_id_domain = fields.Char(compute="_compute_department_id_domain")

    # Constrains section
    @api.multi
    @api.constrains("state_id", "department_id")
    def _check_origin_state_country(self):
        for product in self.filtered(lambda x: x.department_id and x.state_id):
            if (product.department_id.state_id != product.state_id):
                raise UserError(_("Department must belong to the state."))

    # Compute Section
    @api.depends("state_id", "country_id")
    def _compute_department_id_domain(self):
        for product in self:
            if product.state_id:
                product.department_id_domain = json.dumps(
                    [("state_id", "=", product.state_id.id)])
            elif product.country_id:
                product.department_id_domain = json.dumps(
                    [("country_id", "=", product.country_id.id)])

    # Onchange section
    @api.onchange("country_id", "state_id", "department_id")
    def onchange_product_origin(self):
        if self.department_id:
            self.state_id = self.department_id.state_id
        return super().onchange_product_origin()
