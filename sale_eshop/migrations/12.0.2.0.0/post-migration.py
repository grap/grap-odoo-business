# Copyright (C) 2020 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from openupgradelib import openupgrade

logger = logging.getLogger(__name__)


@openupgrade.migrate()
def migrate(env, version):
    logger.info("[sale_eshop] Get Social Network URL fields ...")
    env.cr.execute(
        """
        UPDATE res_company
        SET social_facebook = openupgrade_legacy_12_0_eshop_facebook_url
        where openupgrade_legacy_12_0_eshop_facebook_url is not null;
    """
    )

    env.cr.execute(
        """
        UPDATE res_company
        SET social_twitter = openupgrade_legacy_12_0_eshop_twitter_url
        where openupgrade_legacy_12_0_eshop_twitter_url is not null;
    """
    )

    env.cr.execute(
        """
        UPDATE res_company
        SET social_instagram = openupgrade_legacy_12_0_eshop_instagram_url
        where openupgrade_legacy_12_0_eshop_instagram_url is not null;
    """
    )
