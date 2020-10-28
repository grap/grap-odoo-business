# Copyright (C) 2020 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from openupgradelib import openupgrade
from openupgradelib import openupgrade_90

logger = logging.getLogger(__name__)


attachment_fields = {
    'product.label': [
        ('image', None),
        ('image_medium', None),
        ('image_small', None),
    ],
}


@openupgrade.migrate(no_version=True, use_env=True)
def migrate(env, version):
    logger.info("[product_label] Converting fields to attachement")
    openupgrade_90.convert_binary_field_to_attachment(env, attachment_fields)
