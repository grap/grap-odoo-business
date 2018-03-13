# coding: utf-8
# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import base64
import logging
import StringIO

from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError

from openerp.addons.sale_food import radar_template

_logger = logging.getLogger(__name__)

try:
    import cairosvg
except (ImportError, IOError) as err:
    _logger.info("sale_food : Can not import 'cairosvg' librairy.")


class ProductProduct(models.Model):
    _inherit = 'product.product'

    # Constant Section
    _FRESH_CATEGORY_KEYS = [
        ('extra', 'Extra'),
        ('1', 'Category I'),
        ('2', 'Category II'),
        ('3', 'Category III'),
    ]

    _FRESH_RANGE_KEYS = [
        ('1', '1 - Fresh'),
        ('2', '2 - Canned'),
        ('3', '3 - Frozen'),
        ('4', '4 - Uncooked and Ready to Use'),
        ('5', '5 - Cooked and Ready to Use'),
        ('6', '6 - Dehydrated and Shelf'),
    ]

    _NOTATION_KEYS = [
        ('0', 'Unknown'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    # Column Section
    is_food = fields.Boolean(string='Food Product')

    is_mercuriale = fields.Boolean(
        string='Mercuriale Product', help="A product in mercuriale has price"
        " that changes very regularly.")

    country_id = fields.Many2one(
        comodel_name='res.country', string='Origin Country',
        help="Country of production of the product")

    department_id = fields.Many2one(
        comodel_name='res.country.department', string='Origin Department',
        help="Department of production of the product")

    ingredients = fields.Text(string='Ingredients')

    allergens = fields.Text(string='Allergens')

    origin_description = fields.Char(
        string='Origin Complement', size=64,
        help="Production location complementary information")

    maker_description = fields.Char(
        string='Maker', size=64)

    fresh_category = fields.Selection(
        selection=_FRESH_CATEGORY_KEYS, string='Category for Fresh Product',
        help="Extra - Hight Quality : product without default ;\n"
        "Quality I - Good Quality : Product with little defaults ;\n"
        "Quality II - Normal Quality : Product with default ;\n"
        "Quality III - Bad Quality : Use this option only in"
        " specific situation.")

    fresh_range = fields.Selection(
        selection=_FRESH_RANGE_KEYS, string='Range for Fresh Product')

    label_ids = fields.Many2many(
        comodel_name='product.label', relation='product_label_product_rel',
        column1='product_id', column2='label_id', string='Labels')

    social_notation = fields.Selection(
        selection=_NOTATION_KEYS, string='Social notation',
        required=True, default=0)

    local_notation = fields.Selection(
        selection=_NOTATION_KEYS, string='Local notation',
        required=True, default=0)

    organic_notation = fields.Selection(
        selection=_NOTATION_KEYS, string='Organic notation',
        required=True, default=0)

    packaging_notation = fields.Selection(
        selection=_NOTATION_KEYS, string='Packaging notation',
        required=True, default=0)

    spider_chart_image = fields.Binary(
        compute='_compute_spider_chart_image', string='Spider Chart',
        store=True)

    # Compute section
    @api.multi
    @api.depends(
        'social_notation', 'local_notation', 'organic_notation',
        'packaging_notation')
    def _compute_spider_chart_image(self):
        for product in self:
            codeSVG = radar_template.CodeSVG % {
                'y_social': 105 - (15 * int(product.social_notation)),
                'x_organic': 105 + (15 * int(product.organic_notation)),
                'y_packaging': 105 + (15 * int(product.packaging_notation)),
                'x_local': 105 - (15 * int(product.local_notation)),
                'organic_name': _('AE'),
                'local_name': _('local'),
                'packaging_name': _('package'),
                'social_name': _('social'),
            }
            output = StringIO.StringIO()
            cairosvg.svg2png(bytestring=codeSVG, write_to=output)
            product.spider_chart_image = base64.b64encode(output.getvalue())

    # Constraints section
    @api.multi
    @api.constrains('country_id', 'department_id')
    def _check_origin_department_country(self):
        for product in self:
            if product.department_id.country_id and \
                    product.department_id.country_id.id != \
                    product.country_id.id:
                raise UserError(_('Department must belong to the country.'))
        return True

    # Views section
    @api.onchange(
        'label_ids', 'social_notation', 'local_notation', 'organic_notation',
        'packaging_notation')
    def onchange_label_ids(self):
        for label in self.label_ids:
            self.social_notation = max(
                int(self.social_notation), int(label.minimum_social_notation))
            self.local_notation = max(
                int(self.local_notation), int(label.minimum_local_notation))
            self.organic_notation = max(
                int(self.organic_notation),
                int(label.minimum_organic_notation))
            self.packaging_notation = max(
                int(self.packaging_notation),
                int(label.minimum_packaging_notation))

    # TODO, set domain
#    @api.onchange('country_id', 'department_id')
#    def onchange_department_id(self):
#        rcd_obj = self.pool['res.country.department']
#        if self.department_id:
#        if department_id:
#            rcd = rcd_obj.browse(cr, uid, department_id, context=context)
#            res = {'value': {'country_id': rcd.country_id.id}}
#        return res

#    def onchange_country_id(
#            self, cr, uid, ids, country_id, department_id, context=None):
#        res = {}
#        rcd_obj = self.pool['res.country.department']
#        if not country_id:
#            res = {'value': {'department_id': None}}
#        elif department_id:
#            rcd = rcd_obj.browse(cr, uid, department_id, context=context)
#            if country_id != rcd.country_id.id:
#                res = {'value': {'department_id': None}}
#        return res
