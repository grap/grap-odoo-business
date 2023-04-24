# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from openupgradelib import openupgrade

logger = logging.getLogger(__name__)

column_renames = {
    "res_company": [
        ("eshop_facebook_url", None),
        ("eshop_twitter_url", None),
        ("eshop_instagram_url", None),
    ],
}


@openupgrade.migrate()
def migrate(env, version):
    logger.info("[sale_eshop] Preserve Social Network URL fields ...")
    openupgrade.rename_columns(env.cr, column_renames)
