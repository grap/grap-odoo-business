# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)


_xmlid_renames = [
    (
        "product_print_category_food_report.category_pricetag_middle_square",
        "product_print_category_food_report.print_category_pricetag_01",
    ),
    (
        "product_print_category_food_report.category_pricetag_square_small",
        "product_print_category_food_report.print_category_pricetag_02",
    ),
    (
        "product_print_category_food_report.category_pricetag_normal",
        "product_print_category_food_report.print_category_pricetag_10",
    ),
]


@openupgrade.migrate()
def migrate(env, version):
    _logger.info(
        "Rename all product print categories of product_print_category_food_report..."
    )
    openupgrade.rename_xmlids(env.cr, _xmlid_renames)
