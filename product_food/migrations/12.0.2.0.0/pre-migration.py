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

xmlid_renames = [
    (
        "product_food.group_certifier_manager",
        "product_food_certification.group_certifier_manager",
    ),
]


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
    openupgrade.rename_xmlids(env.cr, xmlid_renames)
