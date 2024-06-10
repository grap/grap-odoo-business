# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)


_xmlid_renames = [
    (
        "grap_qweb_report.category_pricetag_small",
        "product_print_category_food_report.category_pricetag_small",
    ),
    (
        "grap_qweb_report.category_pricetag_large",
        "product_print_category_food_report.category_pricetag_large",
    ),
    (
        "grap_qweb_report.category_pricetag_square_small",
        "product_print_category_food_report.category_pricetag_square_small",
    ),
    (
        "grap_qweb_report.category_pricetag_square_large",
        "product_print_category_food_report.category_pricetag_square_large",
    ),
]


@openupgrade.migrate()
def migrate(env, version):
    _logger.info(
        "Move 4 print categories from grap_qweb_report"
        " to product_print_category_food_report..."
    )
    openupgrade.rename_xmlids(env.cr, _xmlid_renames)
