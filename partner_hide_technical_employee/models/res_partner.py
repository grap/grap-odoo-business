# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import _, api, fields, models
from odoo.exceptions import UserError
from odoo.osv import expression


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_odoo_employee = fields.Boolean(
        string="Is an Odoo Employee",
        readonly=True,
        default=False,
        index=True,
    )

    @api.model_create_multi
    def create(self, vals_list):
        if self.env.context.get("create_hr_employee", False):
            for vals in vals_list:
                vals["is_odoo_employee"] = True
        res = super().create(vals_list)
        # import pdb; pdb.set_trace()
        return res

    # Overload Section
    def write(self, vals):
        self._check_technical_partner_access_employee("write")
        return super().write(vals)

    def unlink(self):
        self._check_technical_partner_access_employee("unlink")
        return super().unlink()

    # Custom section
    def _check_technical_partner_access_employee(self, operation):
        # We use SUPERUSER_ID to be sure to not skip some users, due to
        # some custom access rules deployed on databases
        HrEmployee = self.env["hr.employee"]
        employees = (
            HrEmployee.sudo()
            .with_context(active_test=False)
            .search([("work_contact_id", "in", self.ids)])
        )
        if not employees:
            return

        # Check if current user has correct access right
        if not HrEmployee.check_access_rights(operation, raise_exception=False):
            raise UserError(
                _("You have no right to update partners associated to employee.\n- %s")
                % ("\n- ".join(employees.mapped("name")))
            )

    # Overload the private _search function:
    # This function is used by the other ORM functions
    # (name_search, search_read)
    @api.model
    def _search(
        self,
        domain,
        offset=0,
        limit=None,
        order=None,
        count=False,
        access_rights_uid=None,
    ):
        if not self.env.context.get("show_odoo_employee", False):
            domain = expression.AND([domain, [("is_odoo_employee", "=", False)]])

        return super()._search(
            domain,
            offset=offset,
            limit=limit,
            order=order,
            count=count,
            access_rights_uid=access_rights_uid,
        )
