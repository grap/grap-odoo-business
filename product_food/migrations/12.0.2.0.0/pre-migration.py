# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)


column_renames = {
    "product_product": [
        ("allergens", None),
    ],
}


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    _logger.info("FORCE UNINSTALL 'product_notation' ...")
    openupgrade.logged_query(
        env.cr,
        """
    UPDATE ir_module_module
    SET state = 'to remove'
    WHERE name = 'product_notation'
    AND state != 'uninstalled';
    """,
    )

    _logger.info("FORCE INSTALL 'product_food_certification' ...")
    openupgrade.logged_query(
        env.cr,
        """
    UPDATE ir_module_module
    SET state = 'to install'
    WHERE name = 'product_food_certification'
    AND state != 'installed';
    """,
    )

    openupgrade.rename_columns(env.cr, column_renames)


# delete
# from ir_ui_view where inherit_id in (
#     select res_id
#     from ir_model_data where module='product_food'
#     and name='view_product_product_form'
# );
# delete
# from ir_ui_view where id in (
#     select res_id
#     from ir_model_data where module='product_food'
#     and name in (
#         'view_product_product_form',
#         'view_product_product_form_origin',
#         'view_product_product_form_variant_origin',
#         'view_product_template_form_origin'
#     )
# );
