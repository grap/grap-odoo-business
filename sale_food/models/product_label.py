# coding: utf-8
# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models  # , tools


class ProductLabel(models.Model):
    _name = 'product.label'

    # Columns Section
    code = fields.Char(string='Code', required=True)

    name = fields.Char(string='Name', required=True)

    image = fields.Binary(string='Image')

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

#    image_small = fields.function(
#            _get_image, fnct_inv=_set_image,
#            string='Small-sized image', type='binary', multi='_get_image',
#            store={
#            product.label = (
#                    lambda self, cr, uid, ids, c={}: ids, ['image'], 10)}),
#    image_medium = fields.function(
#            _get_image, fnct_inv=_set_image,
#            string='Medium-sized image', type='binary', multi='_get_image',
#            store={
#            product.label = (
#                    lambda self, cr, uid, ids, c={}: ids, ['image'], 10)}),


#    # Compute Section
#    def _get_image(self, cr, uid, ids, name, args, context=None):
#        res = {}
#        for label in self.browse(cr, uid, ids, context=context):
#            res[label.id] = tools.image_get_resized_images(
#                label.image, avoid_resize_medium=True)
#        return res

#    def _set_image(self, cr, uid, pId, name, value, args, context=None):
#        return self.write(
#            cr, uid, [pId], {'image = tools.image_resize_image_big(value)},
#            context=context)
