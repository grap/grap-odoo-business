# Copyright (C) 2020 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from openupgradelib import openupgrade

logger = logging.getLogger(__name__)

column_renames = {
    "eshop_category": [
        ("image", None),
        ("image_medium", None),
        ("image_small", None),
    ],
}


@openupgrade.migrate(no_version=True, use_env=True)
def migrate(env, version):
    logger.info("[sale_eshop] Preserve image fields ...")
    openupgrade.rename_columns(env.cr, column_renames)
