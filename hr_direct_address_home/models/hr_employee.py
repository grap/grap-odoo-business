# Copyright (C) 2025 - Today: Sylvain LE GAL (http://www.grap.coop)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import api, fields, models
from odoo.tools import clean_context


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    address_home_street = fields.Char(
        string="Street (Private)",
        compute="_compute_address_home_details",
        inverse="_inverse_address_home_details",
        groups="hr.group_hr_user",
        store=True,
    )

    address_home_street2 = fields.Char(
        string="Street 2 (Private)",
        compute="_compute_address_home_details",
        inverse="_inverse_address_home_details",
        groups="hr.group_hr_user",
        store=True,
    )

    address_home_city = fields.Char(
        string="City (Private)",
        compute="_compute_address_home_details",
        inverse="_inverse_address_home_details",
        store=True,
        groups="hr.group_hr_user",
    )

    address_home_state_id = fields.Many2one(
        string="State (Private)",
        comodel_name="res.country.state",
        ondelete="restrict",
        compute="_compute_address_home_details",
        inverse="_inverse_address_home_details",
        domain="[('country_id', '=?', country_id)]",
        groups="hr.group_hr_user",
        store=True,
    )

    address_home_zip = fields.Char(
        string="ZIP (Private)",
        compute="_compute_address_home_details",
        inverse="_inverse_address_home_details",
        groups="hr.group_hr_user",
        store=True,
    )

    address_home_country_id = fields.Many2one(
        string="Country (Private)",
        comodel_name="res.country",
        ondelete="restrict",
        compute="_compute_address_home_details",
        inverse="_inverse_address_home_details",
        groups="hr.group_hr_user",
        store=True,
    )

    address_home_phone = fields.Char(
        string="Phone (Private)",
        compute="_compute_address_home_details",
        inverse="_inverse_address_home_details",
        groups="hr.group_hr_user",
        store=True,
    )

    address_home_mobile = fields.Char(
        string="Mobile (Private)",
        compute="_compute_address_home_details",
        inverse="_inverse_address_home_details",
        groups="hr.group_hr_user",
        store=True,
    )

    address_home_email = fields.Char(
        string="Email (Private)",
        compute="_compute_address_home_details",
        inverse="_inverse_address_home_details",
        groups="hr.group_hr_user",
        store=True,
    )

    @api.depends(
        "address_home_id",
        "address_home_id.street",
        "address_home_id.street2",
        "address_home_id.city",
        "address_home_id.state_id",
        "address_home_id.zip",
        "address_home_id.country_id",
        "address_home_id.phone",
        "address_home_id.mobile",
        "address_home_id.email",
    )
    def _compute_address_home_details(self):
        for employee in self:
            if employee.address_home_id:
                employee.address_home_street = employee.address_home_id.street
                employee.address_home_street2 = employee.address_home_id.street2
                employee.address_home_city = employee.address_home_id.city
                employee.address_home_state_id = employee.address_home_id.state_id
                employee.address_home_zip = employee.address_home_id.zip
                employee.address_home_country_id = employee.address_home_id.country_id
                employee.address_home_phone = employee.address_home_id.phone
                employee.address_home_mobile = employee.address_home_id.mobile
                employee.address_home_email = employee.address_home_id.email

    def _inverse_address_home_details(self):
        ResPartnerSudo = (
            self.env["res.partner"].sudo().with_context(**clean_context(self._context))
        )
        for employee in self:
            vals = {
                "street": employee.address_home_street,
                "street2": employee.address_home_street2,
                "city": employee.address_home_city,
                "state_id": employee.address_home_state_id,
                "zip": employee.address_home_zip,
                "country_id": employee.address_home_country_id,
                "phone": employee.address_home_phone,
                "mobile": employee.address_home_mobile,
                "email": employee.address_home_email,
            }
            if not employee.address_home_id:
                vals["name"] = employee.name
                employee.address_home_id = ResPartnerSudo.create(vals)
            else:
                employee.address_home_id.sudo().write(vals)
