# -*- coding: utf-8 -*-
# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

_logger = logging.getLogger(__name__)


def _create_column(cr, table_name, column_name, column_type):
    # pylint: disable=sql-injection
    req = "ALTER TABLE %s ADD COLUMN %s %s" % (
        table_name, column_name, column_type)
    cr.execute(req)


def pre_init_hook(cr):
    _logger.info(
        "Compute account_invoice product_expense_total and"
        "distributed_expense_total for existing lines")
    _create_column(cr, 'account_invoice', 'product_expense_total', 'numeric')
    _create_column(
        cr, 'account_invoice', 'distributed_expense_total', 'numeric')
    cr.execute("""
        UPDATE account_invoice
            SET
                product_expense_total = amount_untaxed,
                distributed_expense_total = 0.0;
        """)
