# Copyright (C) 2026 - Today: GRAP (https://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    _logger.info("[sale_eshop] POST-MIG : Force to recompute images ...")

    for categ in env["eshop.category"].search([("id", "!=", 0)]):
        if categ.image_1920:
            categ.write({"image_1920": categ.image_1920})
