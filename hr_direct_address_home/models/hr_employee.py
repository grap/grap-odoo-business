# Copyright (C) 2025 - Today: Sylvain LE GAL (http://www.grap.coop)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import api, fields, models
from odoo.tools import clean_context


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    address_home_id = fields.Many2one(copy=False)

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

    @api.model
    def _get_address_home_fields(self):
        return [
            "street",
            "street2",
            "city",
            "state_id",
            "zip",
            "country_id",
            "phone",
            "email",
        ]

    @api.depends(
        lambda self: ["address_home_id"]
        + [f"address_home_id.{x}" for x in self._get_address_home_fields()]
    )
    def _compute_address_home_details(self):
        """Compute hr employee fields,
        based on the data of the related address_home_id partner."""
        for employee in self:
            if employee.address_home_id:
                for field in self._get_address_home_fields():
                    setattr(
                        employee,
                        f"address_home_{field}",
                        getattr(employee.address_home_id, field),
                    )

    def _inverse_address_home_details(self):
        """Apply changes to Compute hr employee fields,
        based on the data of the related address_home_id partner."""

        ResPartnerSudo = (
            self.env["res.partner"].sudo().with_context(**clean_context(self._context))
        )
        for employee in self:
            vals = {}
            for field in self._get_address_home_fields():
                vals[field] = getattr(employee, f"address_home_{field}")
            if not employee.address_home_id:
                vals["name"] = employee.name
                employee.address_home_id = ResPartnerSudo.create(vals)
            else:
                employee.address_home_id.sudo().write(vals)

    @api.returns("self", lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if self.address_home_id:
            for field in self._get_address_home_fields():
                current_value = getattr(self.address_home_id, field)
                default[f"address_home_{field}"] = current_value
        return super().copy(default)
