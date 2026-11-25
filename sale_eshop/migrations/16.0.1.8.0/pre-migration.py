# Copyright (C) 2026 - Today: GRAP (https://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)

_field_renames = [
    ("eshop.category", "eshop_category", "image", "image_1920"),
]


@openupgrade.migrate()
def migrate(env, version):
    _logger.info("[sale_eshop] PRE-MIG : Rename Image fields ...")
    openupgrade.rename_fields(env, _field_renames)
