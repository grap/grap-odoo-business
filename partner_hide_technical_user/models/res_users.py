# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import _, api, models
from odoo.exceptions import UserError


class ResUsers(models.Model):
    _inherit = "res.users"

    @api.model_create_multi
    def create(self, vals_list):
        users = super(ResUsers, self.with_context(create_mode=True)).create(vals_list)
        users.filtered(lambda x: not x.share).write({"is_odoo_user": True})
        return users

    def write(self, vals):
        # TODO: prevent to move from share to non share
        return super().write(vals)

    @api.depends("groups_id")
    def _compute_share(self):
        current_vals = {user: user.share for user in self}
        res = super()._compute_share()
        for user, share in current_vals.items():
            if (
                "create_mode" not in self.env.context
                and not isinstance(user.id, models.NewId)
                and user.share != share
            ):
                raise UserError(
                    _(
                        "You can not change the User Types of %(user_name)s",
                        user_name=user.name,
                    )
                )
        return res
