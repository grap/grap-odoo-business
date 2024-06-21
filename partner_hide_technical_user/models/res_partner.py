# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import _, api, fields, models
from odoo.exceptions import UserError
from odoo.osv import expression


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_odoo_user = fields.Boolean(
        string="Is an Odoo User",
        readonly=True,
        default=False,
        index=True,
    )

    # Overload Section
    def write(self, vals):
        self._check_technical_partner_access_user()
        return super().write(vals)

    def unlink(self):
        self._check_technical_partner_access_user()
        return super().unlink()

    # Custom section
    def _check_technical_partner_access_user(self):
        # We use SUPERUSER_ID to be sure to not skip some users, due to
        # some custom access rules deployed on databases
        ResUsers = self.env["res.users"].sudo()
        users = ResUsers.with_context(active_test=False).search(
            [("partner_id", "in", self.ids)]
        )
        if len(users):
            # Check if current user has correct access right
            if not self.env.user.has_group("base.group_erp_manager"):
                raise UserError(
                    _(
                        "You must be part of the group Administration / Access"
                        " Rights to update partners associated to"
                        " users.\n- %s"
                    )
                    % ("\n- ".join(users.mapped("name")))
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
        if not self.env.context.get("show_odoo_user", False):
            domain = expression.AND([domain, [("is_odoo_user", "=", False)]])

        return super()._search(
            domain,
            offset=offset,
            limit=limit,
            order=order,
            count=count,
            access_rights_uid=access_rights_uid,
        )
