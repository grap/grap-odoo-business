# Copyright (C) 2026 - Today: GRAP (https://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openupgradelib import openupgrade

from odoo import SUPERUSER_ID, api

_logger = logging.getLogger(__name__)


def post_init_hook(cr):
    env = api.Environment(cr, SUPERUSER_ID, {})

    _logger.info("Fast computation of product_product.standard_price_change_date ...")
    openupgrade.logged_query(
        env.cr,
        """
            UPDATE product_product
                SET standard_price_change_date = date_last_statement_price;
        """,
    )
