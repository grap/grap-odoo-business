# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


def post_init_hook(env):
    pass
    env.cr.execute(
        """
        UPDATE res_partner rp
            SET is_odoo_user = True
            FROM res_users ru
            where ru.partner_id = rp.id
            AND ru.id in (
                SELECT uid
                FROM res_groups_users_rel
                WHERE gid in (
                    SELECT res_id
                    FROM ir_model_data
                    WHERE module = 'base' and name ='group_user'
                )
            );
     """
    )
