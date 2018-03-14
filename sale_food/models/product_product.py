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
    _NOTATION_SELECTION = [
        ('0', 'Unknown'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    # Column Section
    is_food = fields.Boolean(string='Food Product')

    is_alcohol = fields.Boolean(string='Contain Alcohol')

    is_mercuriale = fields.Boolean(
        string='Mercuriale Product', help="A product in mercuriale has price"
        " that changes very regularly.")

    country_id = fields.Many2one(
        comodel_name='res.country', string='Origin Country',
        help="Country of production of the product")

    state_id = fields.Many2one(
        comodel_name='res.country.state', string='Origin State',
        help="State of production of the product")

    department_id = fields.Many2one(
        comodel_name='res.country.department', string='Origin Department',
        help="Department of production of the product")

    ingredients = fields.Text(string='Ingredients')

    allergens = fields.Text(string='Allergens')

    origin_description = fields.Char(
        string='Origin Complement', size=64,
        help="Production location complementary information")

    maker_description = fields.Char(string='Maker')

    label_ids = fields.Many2many(
        comodel_name='product.label', relation='product_label_product_rel',
        column1='product_id', column2='label_id', string='Labels')

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

    # Constrains section
    @api.multi
    @api.constrains('country_id', 'department_id')
    def _check_origin_department_country(self):
        for product in self:
            if product.department_id.country_id and \
                    product.department_id.country_id.id != \
                    product.country_id.id:
                raise UserError(_('Department must belong to the country.'))

    @api.multi
    @api.constrains('is_alcohol', 'label_ids')
    def _check_alcohol_labels(self):
        label_obj = self.env['product.label']
        for product in self:
            if product.is_alcohol:
                # Check that all the alcohol labels are set
                alcohol_label_ids = label_obj.search(
                    [('is_alcohol', '=', True)]).ids
                if [x for x in alcohol_label_ids
                        if x not in product.label_ids.ids]:
                    raise UserError(_(
                        "Incorrect Setting. the product %s is checked as"
                        " 'Contain Alcohol' but some related labels are not"
                        " set.") % (product.name))
            if product.label_ids.filtered(lambda x: x.is_alcohol):
                # Check that 'contain Alcohol' is checked
                if not product.is_alcohol:
                    raise UserError(_(
                        "Incorrect Setting. the product %s has a label"
                        " that mentions that the product contains alcohol, "
                        " but the 'Contain Alcohol' is not checked") % (
                            product.name))

    # Onchange section
    @api.onchange(
        'label_ids', 'social_notation', 'local_notation', 'organic_notation',
        'packaging_notation')
    def onchange_label_ids(self):
        for label in self.label_ids:
            self.social_notation = str(max(
                int(self.social_notation), int(label.minimum_social_notation)))
            self.local_notation = str(max(
                int(self.local_notation), int(label.minimum_local_notation)))
            self.organic_notation = str(max(
                int(self.organic_notation),
                int(label.minimum_organic_notation)))
            self.packaging_notation = str(max(
                int(self.packaging_notation),
                int(label.minimum_packaging_notation)))

    @api.onchange('categ_id')
    def onchange_categ_id_is_food(self):
        if self.categ_id:
            self.is_food = self.categ_id.is_food
            self.is_alcohol = self.categ_id.is_alcohol

    @api.onchange('is_food')
    def onchange_is_food(self):
        if not self.is_food:
            self.is_alcohol = False

    @api.onchange('is_alcohol')
    def onchange_is_alcohol(self):
        label_obj = self.env['product.label']
        if self.is_alcohol:
            self.is_food = True
            alcohol_label_ids = label_obj.search(
                [('is_alcohol', '=', True)]).ids
            for alcohol_label_id in alcohol_label_ids:
                self.label_ids = [(4, alcohol_label_id)]
        else:
            self.label_ids = self.label_ids.filtered(
                lambda x: not x.is_alcohol)

    @api.onchange('country_id')
    def onchange_country_id(self):
        if self.country_id:
            if self.state_id and\
                    self.state_id.country_id != self.country_id:
                self.state_id = False
            if self.department_id and\
                    self.department_id.country_id != self.country_id:
                self.department_id = False
            return {'domain': {
                'state_id': [('country_id', '=', self.country_id.id)],
                'department_id': [('country_id', '=', self.country_id.id)],
            }}

    @api.onchange('state_id')
    def onchange_state_id(self):
        if self.state_id:
            self.country_id = self.state_id.country_id
            if self.department_id and\
                    self.department_id.state_id != self.state_id:
                self.department_id = False
            return {'domain': {
                'department_id': [('state_id', '=', self.state_id.id)],
            }}

    @api.onchange('department_id')
    def onchange_department_id(self):
        if self.department_id:
            self.state_id = self.department_id.state_id
            self.country_id = self.department_id.country_id
