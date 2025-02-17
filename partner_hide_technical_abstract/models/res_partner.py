# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import _, api, models
from odoo.exceptions import UserError
from odoo.osv import expression


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def _get_hidden_elements(self):
        """Overload this function to return a list of elements
        For exemple,  [
            {
                "name": "user",
                "model": "res.users",
                "partner_fields: ["partner_id"]
            },
            {
                "name": "employee",
                "model": "hr.employee",
                "partner_fields: ["work_contact_id", "address_home_id"]
            },
        ]
        """
        return []

    def write(self, vals):
        self._check_technical_partner_access("write")
        return super().write(vals)

    def unlink(self):
        self._check_technical_partner_access("unlink")
        return super().unlink()

    # Custom section
    @api.model
    def _check_technical_partner_derogation(self, model_name, items):
        """
        Return True if user without accredition can write on technical partners
        for a given model and items.
        By default, return False if items are defined.
        """
        return len(items) == 0

    def _check_technical_partner_access(self, operation):
        # We use SUPERUSER_ID to be sure to not skip some elements, due to
        # some custom access rules deployed on databases
        for element in self._get_hidden_elements():
            ElementModel = self.env[element["model"]]
            domain = []
            for partner_field in element["partner_fields"]:
                domain = expression.OR([domain, [(partner_field, "in", self.ids)]])

            items = ElementModel.sudo().with_context(active_test=False).search(domain)

            if self._check_technical_partner_derogation(element["model"], items):
                continue

            # Check if current user has correct access right
            if not ElementModel.check_access_rights(operation, raise_exception=False):
                raise UserError(
                    _(
                        "You have no right to update partners associated to"
                        " the elements.\n- %s"
                    )
                    % ("\n- ".join(items.mapped("name")))
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
        for element in self._get_hidden_elements():
            if not self.env.context.get(f"show_odoo_{element['name']}", False):
                domain = expression.AND(
                    [domain, [(f"is_odoo_{element['name']}", "=", False)]]
                )
        return super()._search(
            domain,
            offset=offset,
            limit=limit,
            order=order,
            count=count,
            access_rights_uid=access_rights_uid,
        )
