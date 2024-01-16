# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)

renamed_modules = {
    "product_origin_l10n_fr_department": "l10n_fr_department_product_origin",
}


@openupgrade.migrate()
def migrate(env, version):
    _logger.info("RENAME module product_origin_l10n_fr_department...")
    openupgrade.update_module_names(env.cr, renamed_modules.items(), merge_modules=True)
