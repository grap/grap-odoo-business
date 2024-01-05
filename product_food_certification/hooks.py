# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from openupgradelib import openupgrade

from odoo import SUPERUSER_ID
from odoo.api import Environment

_logger = logging.getLogger(__name__)


def _migrate_openupgrade_legacy_12_0_country_group_id(env):
    env.cr.execute(
        """
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name='product_product'
        AND column_name='openupgrade_legacy_12_0_country_group_id';
        """
    )
    if not env.cr.fetchone():
        _logger.info(
            "openupgrade_legacy_12_0_country_group_id not found in the database."
        )
        return

    # Europe >> 'eu'
    _logger.info(
        "Initialize 'ingredient_origin_type', set 'eu',"
        "based on previous country_group_id configuration."
        " (Europe)"
    )
    env.cr.execute(
        """
        UPDATE product_product
        SET ingredient_origin_type = 'eu'
        WHERE openupgrade_legacy_12_0_country_group_id = %s;""",
        (env.ref("base.europe").id,),
    )

    # 'South America' >> 'no_eu'
    _logger.info(
        "Initialize 'ingredient_origin_type', set 'eu_no_eu',"
        "based on previous country_group_id configuration."
        " (South America)"
    )
    env.cr.execute(
        """
        UPDATE product_product
        SET ingredient_origin_type = 'no_eu'
        WHERE openupgrade_legacy_12_0_country_group_id = %s;""",
        (env.ref("base.south_america").id,),
    )

    # 'UE - non UE' >> 'eu_no_eu'
    eu_no_eu_country_group = env.ref(
        "product_print_category_food_report.countr_group_ue_nonue",
        raise_if_not_found=False,
    )
    if eu_no_eu_country_group:
        _logger.info(
            "Initialize 'ingredient_origin_type', set 'eu_no_eu',"
            "based on previous country_group_id configuration."
            " (UE - non UE)"
        )
        env.cr.execute(
            """
            UPDATE product_product
            SET ingredient_origin_type = 'eu_no_eu'
            WHERE openupgrade_legacy_12_0_country_group_id = %s;""",
            (eu_no_eu_country_group.id,),
        )
        _logger.info(
            "Unlink Custom product_print_category_food_report country group 'UE / non UE"
        )
        openupgrade.delete_records_safely_by_xml_id(
            env, ["product_print_category_food_report.countr_group_ue_nonue"]
        )

    # Custom 'Autre non UE' >> 'no_eu' (If exists)
    env.cr.execute(
        """
        SELECT id from res_country_group
        where name='Autre non UE'
        """
    )
    res = env.cr.fetchone()
    country_group_id = res and res[0]
    if country_group_id:
        _logger.info(
            "Initialize 'ingredient_origin_type', set 'no_eu',"
            "based on previous country_group_id configuration."
            " (Autre non UE)"
        )
        env.cr.execute(
            """
            UPDATE product_product
            SET ingredient_origin_type = 'no_eu'
            WHERE openupgrade_legacy_12_0_country_group_id = %s;""",
            (country_group_id,),
        )
        _logger.info("Unlink Custom obsolete country group 'non UE")
        eu_no_eu_country_group.unlink()


def _migrate_label_ids(env):
    eu_no_eu_label = env["product.label"].search([("code", "=", "AB-UE UE/NON-UE")])
    if eu_no_eu_label:
        _logger.info(
            "Initialize 'ingredient_origin_type', set 'eu_no_eu',"
            "based on previous label_ids configuration."
            " (AB-UE UE/NON-UE)"
        )
        env.cr.execute(
            """
            UPDATE product_product
            SET ingredient_origin_type = 'eu_no_eu'
            WHERE id in (
                SELECT product_id
                FROM product_label_product_rel
                WHERE label_id = %s);""",
            (eu_no_eu_label.id,),
        )

    eu_label = env["product.label"].search([("code", "=", "AB-UE UE")])
    if eu_label:
        _logger.info(
            "Initialize 'ingredient_origin_type', set 'eu',"
            "based on previous label_ids configuration."
            " (AB-UE UE)"
        )
        env.cr.execute(
            """
            UPDATE product_product
            SET ingredient_origin_type = 'eu'
            WHERE id in (
                SELECT product_id
                FROM product_label_product_rel
                WHERE label_id = %s);""",
            (eu_label.id,),
        )

    fr_label = env["product.label"].search([("code", "=", "AB-UE FR")])
    if fr_label:
        _logger.info(
            "Initialize 'ingredient_origin_type', set 'fr',"
            "based on previous label_ids configuration."
            " (AB-UE FR)"
        )
        env.cr.execute(
            """
            UPDATE product_product
            SET ingredient_origin_type = 'fr'
            WHERE id in (
                SELECT product_id
                FROM product_label_product_rel
                WHERE label_id = %s);""",
            (fr_label.id,),
        )

    # Remove 'AB-UE FR' Label
    _logger.info("Set 'AB Europe' to products that has 'AB-UE FR' label.")
    env.cr.execute(
        """
        INSERT INTO product_label_product_rel
            SELECT
                product_id,
                (SELECT id FROM product_label WHERE code = 'AB Europe') as label_id
            FROM product_label_product_rel
            WHERE label_id = (
                SELECT id FROM product_label WHERE code = 'AB-UE FR'
            )
            AND product_id not in (
                SELECT product_id FROM product_label_product_rel WHERE label_id = (
                    SELECT id FROM product_label WHERE code = 'AB Europe')
            );
        """
    )
    _logger.info("Drop 'AB-UE FR' label.")
    env.cr.execute("DELETE FROM product_label WHERE code = 'AB-UE FR';")

    # Remove 'AB-UE UE' Label
    _logger.info("Set 'AB Europe' to products that has 'AB-UE UE' label.")
    env.cr.execute(
        """
        INSERT INTO product_label_product_rel
            SELECT
                product_id,
                (SELECT id FROM product_label WHERE code = 'AB Europe') as label_id
            FROM product_label_product_rel
            WHERE label_id = (
                SELECT id FROM product_label WHERE code = 'AB-UE UE'
            )
            AND product_id not in (
                SELECT product_id FROM product_label_product_rel WHERE label_id = (
                    SELECT id FROM product_label WHERE code = 'AB Europe')
            );
        """
    )
    _logger.info("Drop 'AB-UE UE' label.")
    env.cr.execute("DELETE FROM product_label WHERE code = 'AB-UE UE';")

    # Remove 'AB-UE UE/NON-UE' Label
    _logger.info("Set 'AB Europe' to products that has 'AB-UE UE/NON-UE' label.")
    env.cr.execute(
        """
        INSERT INTO product_label_product_rel
            SELECT
                product_id,
                (SELECT id FROM product_label WHERE code = 'AB Europe') as label_id
            FROM product_label_product_rel
            WHERE label_id = (
                SELECT id FROM product_label WHERE code = 'AB-UE UE/NON-UE'
            )
            AND product_id not in (
                SELECT product_id FROM product_label_product_rel WHERE label_id = (
                    SELECT id FROM product_label WHERE code = 'AB Europe')
            );
        """
    )
    _logger.info("Drop 'AB-UE UE/NON-UE' label.")
    env.cr.execute("DELETE FROM product_label WHERE code = 'AB-UE UE/NON-UE';")


def post_init_hook(cr, pool):
    env = Environment(cr, SUPERUSER_ID, {})
    _migrate_openupgrade_legacy_12_0_country_group_id(env)
    _migrate_label_ids(env)
