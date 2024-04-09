# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


import logging

from openupgradelib import openupgrade
from psycopg2.extensions import AsIs

from ...models.tools import get_allergen_data

_logger = logging.getLogger(__name__)


@openupgrade.logging()
def _populate_allergen_ids(env, company, all_allergens):
    residual_words = {}
    env.cr.execute(
        """
    SELECT pp.id, pp.%s
    FROM product_product pp
    INNER JOIN product_template pt
    ON pt.id = pp.product_tmpl_id
    WHERE company_id = %s
    AND COALESCE(pp.%s, '') != ''
    """,
        (
            AsIs(openupgrade.get_legacy_name("allergens")),
            company.id,
            AsIs(openupgrade.get_legacy_name("allergens")),
        ),
    )

    results = env.cr.fetchall()
    _logger.info(f"Found {len(results)} products...")
    for (product_id, allergen_html) in results:
        (
            allergen_text,
            allergens,
            residual,
            trace_allergens,
            trace_residual,
        ) = get_allergen_data(env, allergen_html, all_allergens)
        if not allergen_text:
            continue

        if allergens or trace_allergens:
            vals = {}
            product = (
                env["product.product"]
                .with_context(force_company=company)
                .browse(product_id)
            )
            if allergens:
                vals.update({"allergen_ids": [(6, 0, allergens.ids)]})
            if allergens:
                vals.update({"trace_allergen_ids": [(6, 0, trace_allergens.ids)]})
            _logger.debug(
                f"Update product {product.name}."
                f" {allergens.mapped('code')} //"
                f" {trace_allergens.mapped('code')} "
            )
            product.write(vals)

        for residual_word in residual.split(" "):
            if residual_word:
                if residual_word not in residual_words:
                    residual_words[residual_word] = [product_id]
                else:
                    residual_words[residual_word].append(product_id)

    for k, v in residual_words.items():
        _logger.warning(f"Found {len(v)} time the word '{k}' ...")


@openupgrade.migrate()
def migrate(env, version):
    all_allergens = env["product.allergen"].search([])
    for company in env["res.company"].with_context(active_test=False).search([]):
        _logger.info(
            f"Migrate allergens for company #{company.id} - {company.name} ..."
        )
        _populate_allergen_ids(env, company, all_allergens)
