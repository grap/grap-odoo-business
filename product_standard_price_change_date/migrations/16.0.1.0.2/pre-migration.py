# Copyright (C) 2026 - Today: GRAP (https://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade

column_renames = {
    "product_product": [("date_last_statement_price", "standard_price_change_date")],
}


@openupgrade.migrate()
def migrate(env, version):
    if openupgrade.column_exists(
        env.cr, "product_product", "date_last_statement_price"
    ):
        openupgrade.rename_columns(env.cr, column_renames)
