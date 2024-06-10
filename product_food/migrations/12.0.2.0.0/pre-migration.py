# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from openupgradelib import openupgrade
from psycopg2.extensions import AsIs

_logger = logging.getLogger(__name__)


column_renames = {
    "product_product": [
        ("allergens", None),
    ],
}

xmlid_renames = [
    (
        "product_food.group_certifier_manager",
        "product_food_certification.group_certifier_manager",
    ),
]


def _remove_product_views(env, field_name):
    _logger.info(f"Handle views that contains '{field_name}' ...")
    openupgrade.logged_query(
        env.cr,
        """
        SELECT id
        FROM ir_ui_view
        WHERE arch_db ilike '%%"%s"%%'
        AND (name ilike '%%product.product %%' or name ilike '%%product.template %%')
        """,
        (AsIs(field_name),),
    )
    view_ids = [x[0] for x in env.cr.fetchall()]
    _logger.info(f"Found {len(view_ids)} views. {view_ids} ...")
    _delete_views(env, view_ids)


def _delete_views(env, view_ids):
    if not view_ids:
        return
    openupgrade.logged_query(
        env.cr,
        """SELECT id from ir_ui_view where inherit_id in %s;""",
        (tuple(view_ids),),
    )
    inherited_view_ids = [x[0] for x in env.cr.fetchall()]
    # Delete first views that inherit from the views we want to delete
    _delete_views(env, inherited_view_ids)

    openupgrade.logged_query(
        env.cr,
        """
        SELECT id, module, name, res_id
        FROM  ir_model_data
        WHERE model = 'ir.ui.view' and res_id in %s;""",
        (tuple(view_ids),),
    )
    data = env.cr.fetchall()
    _logger.info(f"Dropping views {[f'{x[1]}.{x[2]}' for x in data]}")

    to_delete_xml_ids = [x[0] for x in data]
    _logger.info(f"Deleting xml IDS ... {to_delete_xml_ids}")
    openupgrade.logged_query(
        env.cr,
        """DELETE from ir_model_data where id in %s;""",
        (tuple(to_delete_xml_ids),),
    )

    to_delete_view_ids = [x[3] for x in data]
    _logger.info(f"Deleting views ... {to_delete_view_ids}")
    openupgrade.logged_query(
        env.cr,
        """DELETE from ir_ui_view where id in %s;""",
        (tuple(to_delete_view_ids),),
    )


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

    _remove_product_views(env, "country_group_id")
    _remove_product_views(env, "origin_type")

    openupgrade.rename_columns(env.cr, column_renames)
    openupgrade.rename_xmlids(env.cr, xmlid_renames)
