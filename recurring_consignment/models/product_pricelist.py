# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductPricelist(models.Model):
    _inherit = "product.pricelist"

    # Column Section
    consignment_pricelist_id = fields.Many2one(
        comodel_name="product.pricelist", string="Pricelist for Consigned Products"
    )

    # Overload Section
    @api.model
    def create(self, vals):
        pricelist = super().create(vals)
        if pricelist.consignment_pricelist_id:
            pricelist._consignmment_update_multi()
        return pricelist

    @api.multi
    def write(self, vals):
        res = super().write(vals)
        if "consignment_pricelist_id" in vals:
            self._consignmment_update_multi()
        return res

    @api.model
    def consignmment_create(self, template_ids):
        pricelists = self.search([("consignment_pricelist_id", "!=", False)])
        templates = self.env["product.template"].browse(template_ids)
        pricelists._consignmment_update_multi(templates)

    @api.model
    def consignmment_drop(self, template_ids):
        # Drop all previous exceptions
        pricelists = self.search([])
        items = pricelists.mapped("item_ids").filtered(
            lambda x: x.product_tmpl_id.id in template_ids
        )
        # We use sudo, to avoid error, if current user
        # doesn't have correct access write / delete
        # pricelist.item
        items.sudo().unlink()

    @api.multi
    def _consignmment_update_multi(self, templates=False):
        ProductPricelistItem = self.env["product.pricelist.item"]
        ProductTemplate = self.env["product.template"]
        # We use sudo, to avoid error, if current user
        # doesn't have correct access write / delete
        # pricelist.item
        for pricelist in self:
            if not templates:
                # Drop all previous exceptions
                items = pricelist.mapped("item_ids").filtered(
                    lambda x: x.product_tmpl_id.consignor_partner_id
                )
                items.sudo().unlink()
            if pricelist.consignment_pricelist_id:
                if not templates:
                    # Create exceptions for all templates
                    templates = ProductTemplate.with_context(active_test=False).search(
                        [("consignor_partner_id", "!=", False)]
                    )
                for template in templates:
                    ProductPricelistItem.sudo().create(
                        ProductPricelistItem._prepare_consignment_exception(
                            pricelist,
                            template,
                        )
                    )
