# coding: utf-8
# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models, tools


class ProductLabel(models.Model):
    _name = 'product.label'

    # Columns Section
    code = fields.Char(string='Code', required=True)

    name = fields.Char(string='Name', required=True)

    image = fields.Binary(string='Image')

    image_medium = fields.Binary(
        string='Medium-sized image',
        compute='_compute_images', store=True, multi='images',
        help="Medium-sized image of the label. It is automatically "
        "resized as a 128x128px image, with aspect ratio preserved, "
        "only when the image exceeds one of those sizes. Use this field in"
        " form views or some kanban views.")

    image_small = fields.Binary(
        string='Small-sized image',
        compute='_compute_images', store=True, multi='images',
        help="Small-sized image of the label. It is automatically "
        "resized as a 64x64px image, with aspect ratio preserved. "
        "Use this field anywhere a small image is required.")

    active = fields.Boolean(string='Active', default=True)

    company_id = fields.Many2one(
        comodel_name='res.company', string='Company')

    website = fields.Char(string='Website')

    note = fields.Text(string='Note')

    mandatory_on_invoice = fields.Boolean(
        string='Mandatory on invoice',
        help="By checking this field, the label will be printed on"
        " all the customers invoices.")

    minimum_social_notation = fields.Integer(
        string='Minimum Social Notation')

    minimum_local_notation = fields.Integer(
        string='Minimum Local Notation')

    minimum_organic_notation = fields.Integer(
        string='Minimum Organic Notation')

    minimum_packaging_notation = fields.Integer(
        string='Minimum Packaging Notation')

    is_organic = fields.Boolean(
        string='Is Organic',
        help="Check this box if this label is an organic label."
        " If products has no organic label, a text will be displayed"
        " on Price Tag.")

    is_alcohol = fields.Boolean(
        string='Is Alcohol',
        help="Check this box if this label is a label that mentions that"
        " products contain alcohol. If checked, the products that"
        " contains alcohol will have this label set automatically.")

    # Compute Section
    @api.multi
    @api.depends('image')
    def _compute_images(self):
        for label in self:
            label.update(tools.image_get_resized_images(
                label.image, avoid_resize_medium=True))
