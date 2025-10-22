# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class SaleRecoveryPlace(models.Model):
    _name = "sale.recovery.place"
    _description = "Recovery Place"
    _order = "name"

    name = fields.Char(required=True)

    complete_name = fields.Char(
        compute="_compute_complete_name", index=True, store=True
    )

    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        required=True,
        default=lambda x: x._default_company_id(),
    )

    active = fields.Boolean(default=True)

    street = fields.Char()

    street2 = fields.Char()

    zip = fields.Char(change_default=True, size=24)

    city = fields.Char()

    state_id = fields.Many2one(string="State", comodel_name="res.country.state")

    country_id = fields.Many2one(string="Country", comodel_name="res.country")

    shipping_product_id = fields.Many2one(
        string="Shipping Cost Product",
        comodel_name="product.template",
        domain="[('type', '=', 'service')]",
        help="If set, this product will"
        " be added automatically to the sale order, when it is confirmed,"
        " if the sale order is associated to this recovery place.",
    )

    @api.model
    def _default_company_id(self):
        return self.env.company

    # Compute Section
    @api.depends("name", "street", "street2", "zip", "city", "state_id", "country_id")
    def _compute_complete_name(self):
        for place in self:
            address_format = (
                place.country_id
                and place.country_id.address_format
                or "%(street)s\n%(street2)s\n%(city)s %(state_code)s"
                " %(zip)s\n%(country_name)s"
            )
            args = {
                "street": place.street or "",
                "street2": place.street2 or "",
                "zip": place.zip or "",
                "city": place.city or "",
                "state_code": place.state_id and place.state_id.code or "",
                "state_name": place.state_id and place.state_id.name or "",
                "country_code": place.country_id and place.country_id.code or "",
                "country_name": place.country_id and place.country_id.name or "",
            }
            place.complete_name = "{} - {}".format(
                place.name,
                (address_format % args).replace("\n", " "),
            )

    @api.onchange("state_id")
    def _onchange_state_id(self):
        if self.state_id:
            self.country_id = self.state_id.id

    @api.onchange("country_id")
    def _onchange_country_id(self):
        if self.country_id and self.state_id:
            if self.state_id.country_id != self.country_id:
                self.state_id = False
