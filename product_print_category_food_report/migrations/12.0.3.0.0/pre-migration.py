# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)


_xmlid_renames = [
    (
        "product_print_category_food_report.category_pricetag_square_large",            # A) Carré large - 92x85mm
        "product_print_category_food_report.",                                          # TODO
    ),
    (
        "product_print_category_food_report.category_pricetag_middle_square",           # B) Square pricetag - 40x36mm
        "product_print_category_food_report.print_category_pricetag_01",                # 01
    ),
    (
        "product_print_category_food_report.category_pricetag_square_small",            # C) Carré petit - 30x30mm
        "product_print_category_food_report.print_category_pricetag_02",                # 02
    ),
    (
        "product_print_category_food_report.category_pricetag_counter",                 # D) Counter pricetag - 55*94mm
        "product_print_category_food_report.print_category_pricetag_20",                # 20
    ),
    (
        "product_print_category_food_report.category_pricetag_large",                   # E) Normal (large) - 76x43mm
        "product_print_category_food_report.print_category_pricetag_12",                # 12
    ),
    (
        "product_print_category_food_report.category_pricetag_normal",                  # F) Normal pricetag normal - 76x31mm
        "product_print_category_food_report.print_category_pricetag_10",                # 10
    ),
    (
        "product_print_category_food_report.category_pricetag_small",                   # G) Normal (small) - 76x33mm
        "product_print_category_food_report.print_category_pricetag_11",                # 11
    ),
    (
        "product_print_category_food_report.category_pricetag_bulk_selling_applimage",  # H) Bulk pricetag long Applimage - 52x101mm
        "product_print_category_food_report.print_category_pricetag_30",                # 30
    ),
    (
        "product_print_category_food_report.category_pricetag_bulk_selling",            # I) Bulk pricetag square - 93x93mm
        "product_print_category_food_report.",                                          # TODO
    ),

]


@openupgrade.migrate()
def migrate(env, version):
    _logger.info(
        "Rename all product print categories of product_print_category_food_report..."
    )
    openupgrade.rename_xmlids(env.cr, _xmlid_renames)
