# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    # Force to recompute images
    for label in env["product.label"].search([("id", "!=", 0)]):
        if label.image_1920:
            label.write({"image_1920": label.image_1920})
