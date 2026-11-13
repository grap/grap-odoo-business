# Copyright (C) 2026 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    if openupgrade.column_exists(env.cr, "product_product", "is_alcohol"):
        openupgrade.rename_columns(
            env.cr, {"product_product": [("is_alcohol", "has_alcohol")]}
        )

    if openupgrade.column_exists(env.cr, "product_category", "is_alcohol"):
        openupgrade.rename_columns(
            env.cr, {"product_category": [("is_alcohol", "has_alcohol")]}
        )
