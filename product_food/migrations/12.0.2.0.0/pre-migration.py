# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade

column_renames = {
    "product_product": [
        ("allergens", None),
    ],
}


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    openupgrade.rename_columns(env.cr, column_renames)


# delete
# from ir_ui_view where inherit_id in (
#     select res_id
#     from ir_model_data where module='product_food'
#     and name='view_product_product_form'
# );
# delete
# from ir_ui_view where id in (
#     select res_id
#     from ir_model_data where module='product_food'
#     and name in (
#         'view_product_product_form',
#         'view_product_product_form_origin',
#         'view_product_product_form_variant_origin',
#         'view_product_template_form_origin'
#     )
# );
