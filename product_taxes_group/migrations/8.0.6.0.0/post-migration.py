# coding: utf-8
# Copyright (C) 2017-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging
from openupgradelib import openupgrade

from openerp.modules.registry import RegistryManager
from openerp import SUPERUSER_ID

logger = logging.getLogger('product_taxes_group')


@openupgrade.migrate()
def migrate(cr, version):
    registry = RegistryManager.get(cr.dbname)
    classification_obj = registry['account.product.fiscal.classification']
    classification_obj.rename_classification_from_group(cr, SUPERUSER_ID)
    classification_obj.set_fiscal_classification_to_res_partner(
        cr, SUPERUSER_ID)
