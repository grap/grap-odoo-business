# coding: utf-8
# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


import logging

from openerp import api, models

logger = logging.getLogger('product_taxes_group')


class AccountProductFiscalClassification(models.Model):
    _inherit = 'account.product.fiscal.classification'

    # Overload Section
    @api.model
    def rename_classification_from_group(self):
        tax_group_obj = self.env['tax.group']
        groups = tax_group_obj.with_context(active_test=False).search([])
        for group in groups:
            classification_id = self.find_or_create(
                group.company_id.id,
                group.customer_tax_ids.ids,
                group.supplier_tax_ids.ids)
            if classification_id:
                classification = self.browse(classification_id)
                logger.info("renaming classification %s by %s" % (
                    classification.name, group.name))
                classification.name = group.name
            else:
                logger.warning("classification not found for %s" % (
                    group.name))

    @api.model
    def set_fiscal_classification_to_res_partner(self):
        classifications = self.with_context(active_test=False).search([])
        for classification in classifications:
            taxes = classification.sale_tax_ids.filtered(
                lambda x: x.consignor_partner_id)
            if taxes:
                logger.info("Set consignor %s to %s" % (
                    taxes[0].consignor_partner_id.name,
                    classification.name))
                classification.consignor_partner_id =\
                    taxes[0].consignor_partner_id.id
