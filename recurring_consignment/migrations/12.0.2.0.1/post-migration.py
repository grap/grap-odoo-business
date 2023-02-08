# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import logging

from openupgradelib import openupgrade
from psycopg2.extensions import AsIs

logger = logging.getLogger(__name__)


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.logged_query(
        env.cr,
        """
        SELECT
            pt.id as product_tmpl_id,
            pt.company_id as company_id
        FROM product_template pt
        WHERE pt.%s is true
        ORDER BY pt.company_id, pt.name
        """,
        (AsIs(openupgrade.get_legacy_name("is_consignment_commission")),),
    )

    for (product_tmpl_id, company_id) in env.cr.fetchall():
        template = (
            env["product.template"]
            .with_context(force_company=company_id)
            .browse(product_tmpl_id)
        )
        company = (
            env["res.company"].with_context(force_company=company_id).browse(company_id)
        )

        if template.fiscal_classification_id.sale_tax_ids.filtered(
            lambda x: x.amount == 20
        ):
            # If it is the commission product with vat 20% we keep it
            logger.info(
                "[recurring_consigment] Set the product %s as"
                " the default consignment commission product for the company %s"
                % (template.name, company.name)
            )

            company.write({"commission_product_id": template.product_variant_id.id})

        else:
            # We disable the obsolete product
            logger.info(
                "[recurring_consigment] Disable the obsolete consignment"
                " commission product %s"
                " for the company %s" % (template.name, company.name)
            )
            template.write(
                {
                    "name": "%s (OBSOLETE)" % template.name,
                    "active": False,
                }
            )
