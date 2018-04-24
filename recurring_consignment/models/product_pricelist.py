# coding: utf-8
# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'

    # Column Section
    consignment_pricelist_id = fields.Many2one(
        comodel_name='product.pricelist',
        string='Pricelist for Consigned Products')

    # Overload Section
    @api.model
    def create(self, vals):
        pricelist = super(ProductPricelist, self).create(vals)
        if pricelist.consignment_pricelist_id:
            pricelist._consignmment_update_multi()
        return pricelist

    @api.multi
    def write(self, vals):
        res = super(ProductPricelist, self).write(vals)
        if 'consignment_pricelist_id' in vals:
            self._consignmment_update_multi()
        return res

    @api.model
    def consignmment_create(self, template_ids):
        pricelists = self.search([
            ('type', '=', 'sale'),
            ('consignment_pricelist_id', '!=', False)])
        templates = self.env['product.template'].browse(template_ids)
        pricelists._consignmment_update_multi(templates)

    @api.model
    def consignmment_drop(self, template_ids):
        # Drop all previous exceptions
        pricelists = self.search([('type', '=', 'sale')])
        items = pricelists.mapped('version_id.items_id').filtered(
            lambda x: x.product_tmpl_id.id in template_ids)
        items.unlink()

    @api.multi
    def _consignmment_update_multi(self, templates=False):
        item_obj = self.env['product.pricelist.item']
        template_obj = self.env['product.template']
        for pricelist in self:
            if not pricelist.consignment_pricelist_id:
                # Drop all previous exceptions
                items = pricelist.mapped('version_id.items_id').filtered(
                    lambda x: x.product_tmpl_id.consignor_partner_id)
                items.unlink()
            else:
                if not templates:
                    # Create exceptions for all templates
                    templates = template_obj.with_context(
                        active_test=False).search(
                            [('consignor_partner_id', '!=', False)])
                for template in templates:
                    for version in pricelist.version_id:
                        item_obj.create(
                            template._prepare_consignment_exception(
                                version, pricelist.consignment_pricelist_id))
