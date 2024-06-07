# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)

column_renames = {
    "product_product": [
        ("origin_description", None),
    ],
}


@openupgrade.migrate()
def migrate(env, version):
    _logger.info("Backup product_product.origin_description field ...")
    openupgrade.rename_columns(env.cr, column_renames)
