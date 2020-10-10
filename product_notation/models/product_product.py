# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import base64
import logging
import tempfile

from openerp import _, api, fields, models

from .. import radar_template

_logger = logging.getLogger(__name__)

try:
    import cairosvg
except ImportError:
    _logger.debug("product_notation : Can not import 'cairosvg' librairy.")


class ProductProduct(models.Model):
    _inherit = 'product.product'

    # Constant Section
    _NOTATION_SELECTION = [
        ('0', 'Unknown'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    # Column Section
    social_notation = fields.Selection(
        selection=_NOTATION_SELECTION, string='Social notation',
        required=True, default='0')

    local_notation = fields.Selection(
        selection=_NOTATION_SELECTION, string='Local notation',
        required=True, default='0')

    organic_notation = fields.Selection(
        selection=_NOTATION_SELECTION, string='Organic notation',
        required=True, default='0')

    packaging_notation = fields.Selection(
        selection=_NOTATION_SELECTION, string='Packaging notation',
        required=True, default='0')

    spider_chart_image = fields.Binary(
        compute='_compute_spider_chart_image', string='Spider Chart',
        attachment=True, store=True)

    # Compute section
    @api.depends(
        'social_notation', 'local_notation', 'organic_notation',
        'packaging_notation')
    def _compute_spider_chart_image(self):
        for product in self:
            if (product.social_notation and
                    product.organic_notation and
                    product.packaging_notation and
                    product.local_notation):
                codeSVG = radar_template.CodeSVG % {
                    'y_social': 105 - (15 * int(product.social_notation)),
                    'x_organic': 105 + (15 * int(product.organic_notation)),
                    'y_packaging':
                    105 + (15 * int(product.packaging_notation)),
                    'x_local': 105 - (15 * int(product.local_notation)),
                    'organic_name': _('AE'),
                    'local_name': _('local'),
                    'packaging_name': _('package'),
                    'social_name': _('social'),
                }
                tmpFile = tempfile.TemporaryFile()
                cairosvg.svg2png(bytestring=codeSVG, write_to=tmpFile)
                tmpFile.seek(0)
                product.spider_chart_image = base64.b64encode(tmpFile.read())
            else:
                product.spider_chart_image = False
