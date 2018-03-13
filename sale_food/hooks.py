# coding: utf-8
# Copyright (C) 2016 : tecnativa (https://www.tecnativa.com)
# Copyright (C) 2018 : GRAP (http://www.grap.coop)
# @author: Antonio Espinosa <antonio.espinosa@tecnativa.com>
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging
from psycopg2.extensions import AsIs

_logger = logging.getLogger(__name__)


def column_exists(cr, table, column):
    cr.execute("""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = %s AND column_name = %s""", (table, column))
    return bool(cr.fetchall())


def column_add_with_value(cr, table, column, field_type, value):
    if not column_exists(cr, table, column):
        _logger.info(
            "Creating column %s (%s) on table %s with default value %s" % (
                column, field_type, table, value))
        cr.execute("""
            ALTER TABLE %s
            ADD COLUMN %s %s""", (AsIs(table), AsIs(column), AsIs(field_type)))
        cr.execute("""
            UPDATE %s SET %s = %s""", (AsIs(table), AsIs(column), value))


def pre_init_hook(cr):
    column_add_with_value(
        cr, 'product_product', 'social_notation', 'varchar', 0)
    column_add_with_value(
        cr, 'product_product', 'organic_notation', 'varchar', 0)
    column_add_with_value(
        cr, 'product_product', 'packaging_notation', 'varchar', 0)
    column_add_with_value(
        cr, 'product_product', 'local_notation', 'varchar', 0)
