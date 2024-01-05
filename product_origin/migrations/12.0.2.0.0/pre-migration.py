# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from openupgradelib import openupgrade

logger = logging.getLogger(__name__)

column_renames = {
    "product_product": [
        ("country_group_id", None),
    ],
}


@openupgrade.migrate()
def migrate(env, version):
    logger.info("[product_origin] Preserve country Group field on product.product ...")
    openupgrade.rename_columns(env.cr, column_renames)
