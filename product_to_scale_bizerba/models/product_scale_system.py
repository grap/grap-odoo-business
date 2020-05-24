# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductScaleSystem(models.Model):
    _name = 'product.scale.system'
    _description = "Product Scale System"

    # Constant section
    _ENCODING_SELECTION = [
        ('iso-8859-1', 'Latin 1 (iso-8859-1)'),
    ]

    # Column Section
    name = fields.Char(string='Name', required=True)

    company_id = fields.Many2one(
        comodel_name='res.company', string='Company', index=True,
        default=lambda s: s._default_company_id())

    active = fields.Boolean(string='Active', default=True)

    ftp_url = fields.Char(string='FTP Server URL')

    ftp_login = fields.Char(string='FTP Login')

    ftp_password = fields.Char(string='FTP Password')

    encoding = fields.Selection(
        selection=_ENCODING_SELECTION, string='Encoding', required=True,
        default='iso-8859-1')

    csv_relative_path = fields.Char(
        string='Relative Path for CSV', required=True, default='/')

    product_image_relative_path = fields.Char(
        string='Relative Path for Product Images', required=True, default='/')

    product_text_file_pattern = fields.Char(
        string='Product Text File Pattern', required=True,
        default='product.csv', help="Pattern"
        " of the Product file. Use % to include dated information.\n"
        " Ref: https://docs.python.org/2/library/time.html#time.strftime")

    external_text_file_pattern = fields.Char(
        string='External Text File Pattern', required=True,
        default='external_text.csv', help="Pattern"
        " of the External Text file. Use % to include dated information.\n"
        " Ref: https://docs.python.org/2/library/time.html#time.strftime")

    screen_text_file_pattern = fields.Char(
        string='Screen Text File Pattern', required=True, help="Pattern"
        " of the Screen Text file. Use % to include dated information.\n"
        " Ref: https://docs.python.org/2/library/time.html#time.strftime")

    product_line_ids = fields.One2many(
        comodel_name='product.scale.system.product.line',
        inverse_name='scale_system_id', string='Product Lines')

    field_ids = fields.One2many(
        comodel_name='ir.model.fields', string='Fields',
        compute='_compute_field_ids')

    product_id_field_id = fields.Many2one(
        comodel_name='ir.model.fields', string='Product ID Field',
        domain=[('model', '=', 'product.product')], required=True,
        help="Set the field that will be used as the ID of the product"
        " in the extra CSV file in Bizerba and in the PLNR field.\n"
        " type of field = id")

    # Default Section
    @api.model
    def _default_company_id(self):
        return self.env.user.company_id.id

    # Compute Section
    @api.multi
    @api.depends('product_line_ids.field_id')
    def _compute_field_ids(self):
        for system in self:
            system.field_ids = system.product_line_ids.filtered(
                lambda x: x.field_id).mapped('field_id').ids
