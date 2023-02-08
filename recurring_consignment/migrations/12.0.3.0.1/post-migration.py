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
                at.consignor_partner_id,
                at.company_id
            FROM account_tax at
            WHERE at.amount = 0
            AND at.consignor_partner_id is not null
            AND name ilike '%SUJ%'
            AND at.active is true
            group by at.consignor_partner_id, at.company_id
            order by at.company_id;
        """,
        (AsIs(openupgrade.get_legacy_name("is_consignment_commission")),),
    )

    for (consignor_partner_id, company_id) in env.cr.fetchall():
        partner = (
            env["res.partner"]
            .with_context(force_company=company_id)
            .browse(consignor_partner_id)
        )
        company = (
            env["res.company"].with_context(force_company=company_id).browse(company_id)
        )
        partner = partner
        company = company
        # Create a new fiscal classification

        # Get all the bad obsolete classification

        # Move product from obsolete classification to the new one

        # Disable obsolete classification

        # Disable obsolete taxes
