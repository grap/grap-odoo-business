# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_odoo_user = fields.Boolean(
        string="Is an Odoo User", readonly=True, default=False
    )
    is_odoo_company = fields.Boolean(
        string="Is an Odoo Company", readonly=True, default=False
    )

    @api.model
    def create(self, vals):
        if self.env.context.get("is_odoo_company"):
            vals["is_odoo_company"] = True
        return super().create(vals)

    # Overload Section
    @api.multi
    def write(self, vals):
        self._check_technical_partner_access()
        return super().write(vals)

    @api.multi
    def unlink(self):
        self._check_technical_partner_access()
        return super().unlink()

    # Custom section
    @api.multi
    def _check_technical_partner_access(self):
        # We use SUPERUSER_ID to be sure to not skip some users, due to
        # some custom access rules deployed on databases
        ResUsers = self.env["res.users"].sudo()
        users = ResUsers.with_context(active_test=False).search(
            [("partner_id", "in", self.ids)]
        )
        ResCompany = self.env["res.company"].sudo()
        companies = ResCompany.with_context(active_test=False).search(
            [("partner_id", "in", self.ids)]
        )
        if len(users) != 0 or len(companies) != 0:
            # Check if current user has correct access right
            if not self.env.user.has_group("base.group_erp_manager"):
                raise UserError(
                    _(
                        "You must be part of the group Administration / Access"
                        " Rights to update partners associated to"
                        " users or companies.\n- %s"
                    )
                    % ("\n- ".join(users.mapped("name")))
                )

    # Overload the private _search function:
    # This function is used by the other ORM functions
    # (name_search, search_read)
    @api.model
    def _search(
        self,
        args,
        offset=0,
        limit=None,
        order=None,
        count=False,
        access_rights_uid=None,
    ):
        args += [
            ("is_odoo_user", "=", bool(self.env.context.get("show_odoo_user", False))),
            (
                "is_odoo_company",
                "=",
                bool(self.env.context.get("show_odoo_company", False)),
            ),
        ]
        return super()._search(
            args=args,
            offset=offset,
            limit=limit,
            order=order,
            count=count,
            access_rights_uid=access_rights_uid,
        )

    @api.model
    def _name_search(
        self, name, args=None, operator="ilike", limit=100, name_get_uid=None
    ):
        # Overload also _name_search
        # because res.partner._name_search doesn't call super in all
        # cases. (so doesn't call _search)
        if name and operator in ("=", "ilike", "=ilike", "like", "=like"):
            args += [
                (
                    "is_odoo_user",
                    "=",
                    bool(self.env.context.get("show_odoo_user", False)),
                ),
                (
                    "is_odoo_company",
                    "=",
                    bool(self.env.context.get("show_odoo_company", False)),
                ),
            ]
        return super()._name_search(
            name, args, operator=operator, limit=limit, name_get_uid=name_get_uid
        )
