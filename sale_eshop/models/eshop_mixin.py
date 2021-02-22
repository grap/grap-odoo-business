# Copyright (C) 2014-Today GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

import requests
from requests.compat import urljoin

from odoo import api, models

from odoo.addons.queue_job.job import job

_logger = logging.getLogger(__name__)


class EshopMixin(models.AbstractModel):
    _name = "eshop.mixin"
    _description = "Eshop Mixin"

    _eshop_fields = []
    _eshop_invalidation_type = False

    @api.model
    def _get_eshop_fields(self):
        fields = self._eshop_fields
        fields.append("id")
        has_image = False
        for field in fields:
            has_image = True
            if "image" in field:
                fields.remove(field)
                has_image = True
        if has_image:
            fields.append("write_date")
        return fields

    @api.model
    def eshop_load_data(self, domain=False):
        if not domain:
            domain = self._get_eshop_domain()
        return self.search_read(domain, self._get_eshop_fields())

    # Private Function
    @api.model
    def _get_eshop_domain(self):
        return []

    @api.model
    @job(
        default_channel="root.sale_eshop_invalidate_eshop",
        retry_pattern={1: 10 * 60, 6: 60 * 60, 12: 12 * 60 * 60},
    )
    def _invalidate_eshop(self, company, item_identifier):
        base_url = company.eshop_url
        private_key = company.eshop_invalidation_key
        if not (base_url and private_key):
            _logger.warning(
                "Invalidation has not been possible because"
                " eshop_url and or eshop_invalidation_key is not available"
                " for company %d" % company.id
            )
            return

        url = urljoin(
            base_url,
            "invalidation_cache/%s/%s/%d/" % (private_key, self._name, item_identifier),
        )
        requests.get(url, verify=False)

    @api.multi
    def write(self, vals):
        self._write_eshop_invalidate(vals)
        return super().write(vals)

    @api.multi
    def _write_eshop_invalidate(self, vals):
        ResCompany = self.env["res.company"]

        update_fields = vals.keys()
        intersec_fields = [x for x in self._eshop_fields if x in update_fields]
        if not intersec_fields:
            # No fields synchronised has changed
            return

        # Some fields are loaded and cached by the eShop
        if self._eshop_invalidation_type == "single":
            for item in self:
                if self._name == "res.company" and item.has_eshop:
                    self.with_delay()._invalidate_eshop(item, item.id)

                elif self._name != "res.company" and item.company_id.has_eshop:
                    self.with_delay()._invalidate_eshop(item.company_id, item.id)

        elif self._eshop_invalidation_type == "multiple":
            for company in ResCompany.sudo().search([("has_eshop", "=", True)]):
                for _id in self.ids:
                    self.with_delay()._invalidate_eshop(company, _id)
