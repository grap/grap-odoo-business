# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import logging
import re

from openupgradelib import openupgrade
from psycopg2.extensions import AsIs

logger = logging.getLogger(__name__)


def migrate_product_template_to_company(env, company):
    """Move the setting done previously done in product.template in res.company"""
    commission_template = False
    openupgrade.logged_query(
        env.cr,
        """
        SELECT pt.id as product_tmpl_id
        FROM product_template pt
        WHERE pt.%s is true
        AND pt.company_id = %s
        """,
        (
            AsIs(openupgrade.get_legacy_name("is_consignment_commission")),
            company.id,
        ),
    )

    for product_tmpl_id in env.cr.fetchall():
        template = (
            env["product.template"]
            .with_context(force_company=company.id)
            .browse(product_tmpl_id)
        )
        if template.fiscal_classification_id.sale_tax_ids.filtered(
            lambda x: x.amount == 20
        ):
            # If it is the commission product with vat 20% we keep it
            logger.info(
                "Set the product %s as"
                " the default consignment commission product for the company %s"
                % (template.name, company.name)
            )

            company.write({"commission_product_id": template.product_variant_id.id})
            commission_template = template
        else:
            # We disable the obsolete product
            logger.info(
                "Disable the obsolete consignment"
                " commission product %s"
                " for the company %s" % (template.name, company.name)
            )
            template.write(
                {
                    "name": "%s (OBSOLETE)" % template.name,
                    "active": False,
                }
            )

    if not commission_template:
        raise NotImplementedError(
            "We should write migration script to create commision product with vat 20%"
        )
    return commission_template


def migrate_non_taxable_consignor(env, company, partner):
    """Check if the consignor is taxable.
    - If yes, return.
    - If no, create a new fiscal classification (if doesn't exist) 0%
    - If mixted, raise an error
    """
    Wizard = env["consignor.create.wizard"]
    AccountAccount = env["account.account"].with_context(force_company=company.id)
    AccountTax = env["account.tax"].with_context(force_company=company.id)
    AccountClassification = env["account.product.fiscal.classification"].with_context(
        force_company=company.id
    )

    classifications = partner.consignor_fiscal_classification_ids

    taxable_classifications = classifications.filtered(
        lambda x: x.mapped("sale_tax_ids.amount") != [0.0]
    )
    non_taxable_classifications = classifications.filtered(
        lambda x: x.mapped("sale_tax_ids.amount") == [0.0]
    )

    for classification in taxable_classifications:
        if "SUJ" in classification.name:
            raise NotImplementedError(
                "Data looks corrupted."
                f" classification #{classification.id} - {classification.name}"
            )

    if len(non_taxable_classifications) != len(classifications):
        logger.info("Ignoring The supplier, because it is vat subject.")
        return

    # Get sequence. (Prodxxx)
    pattern = re.compile(r"(Prod\d\d\d) - (.*)")

    groups = pattern.match(partner.name).groups()
    if len(groups) != 2:
        raise NotImplementedError("Sequence / partner name not found.")
    sequence = groups[0]
    partner_name = groups[1]

    account = AccountAccount.search(
        [("code", "=", "467"), ("company_id", "=", company.id)]
    )

    if len(account) != 1:
        raise NotImplementedError("Account not found.")

    # Create a new fiscal classification
    tax_vals = Wizard._prepare_tax_model(
        sequence, account, partner, 0.0, False, partner_name, company
    )
    tax_vals.update({"company_id": company.fiscal_company_id.id})
    new_tax = AccountTax.create(tax_vals)
    classification_vals = Wizard._prepare_fiscal_classification_model(
        sequence, partner, new_tax, False, partner_name, company
    )
    new_classification = AccountClassification.create(classification_vals)

    # Move product from obsolete classifications to the new one
    products = classifications.mapped("product_tmpl_ids")
    logger.info(
        f"Move {len(products)}"
        f" products with classification {classifications.ids} to {new_classification.id}"
    )
    products.write({"fiscal_classification_id": new_classification.id})

    # Disable obsolete classification
    for classification in classifications:
        classification.write(
            {
                "name": f"{classification.name} (OBSOLETE)",
                "active": False,
            }
        )
        logger.info(f"Classification '{classification.name}' disabled.")

    # Disable obsolete taxes
    for tax in classifications.mapped("sale_tax_ids"):
        tax.write(
            {
                "name": f"{tax.name} (OBSOLETE)",
                "active": False,
            }
        )
        logger.info(f"Tax '{tax.name}' disabled.")


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.logged_query(
        env.cr,
        """
        SELECT id
        FROM res_company
        WHERE id in (SELECT company_id FROM res_partner WHERE is_consignor is true);
        """,
    )

    for company_id in env.cr.fetchall():
        company = (
            env["res.company"].with_context(force_company=company_id).browse(company_id)
        )
        logger.info(f"Company #{company.id} - {company.name} ...")

        migrate_product_template_to_company(env, company)

        openupgrade.logged_query(
            env.cr,
            """
            SELECT id
            FROM res_partner
            WHERE is_consignor is true
            AND company_id = %s;
            """,
            (company.id,),
        )
        for partner_id in env.cr.fetchall():
            partner = (
                env["res.partner"]
                .with_context(force_company=company_id)
                .browse(partner_id)
            )
            logger.info(f"Consignor #{partner.id} - {partner.name} ...")

            migrate_non_taxable_consignor(env, company, partner)
