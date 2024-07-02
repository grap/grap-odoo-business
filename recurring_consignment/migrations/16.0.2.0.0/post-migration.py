# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from openupgradelib import openupgrade

from odoo import Command

_logger = logging.getLogger(__name__)


@openupgrade.logging()
def _remove_taxes_for_deposit_with_null_tax(env):
    FiscalClassification = env["account.product.fiscal.classification"].sudo()
    classifications = FiscalClassification.search(
        [("consignor_partner_id", "!=", False)]
    ).filtered(lambda x: (x.mapped("sale_tax_ids.amount") == [0.0]))

    for classification in classifications:
        _logger.info(f"Disable empty tax {classification.mapped('sale_tax_ids.name')}")
        classification.mapped("sale_tax_ids").active = False
        _logger.info(f"Remove sale taxes from {classification.name}")
        classification.sale_tax_ids = [Command.clear()]


@openupgrade.migrate()
def migrate(env, version):
    _remove_taxes_for_deposit_with_null_tax(env)
