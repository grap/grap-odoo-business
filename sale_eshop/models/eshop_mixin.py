# coding: utf-8
# Copyright (C) 2014-Today GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from datetime import datetime
from openerp import api, models


class EshopMixin(models.AbstractModel):
    _name = "eshop.mixin"

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

    def _invalidate_eshop(self, company, item_identifier):
        EshopQueueJob = self.env["eshop.queue.job"]
        EshopQueueJob.sudo().create(
            {
                "job_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "model_name": self._name,
                "item_identifier": item_identifier,
                "company_id": company.id,
            }
        )

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
                    self._invalidate_eshop(item, item.id)

                elif self._name != "res.company" and item.company_id.has_eshop:
                    self._invalidate_eshop(item.company_id, item.id)

        elif self._eshop_invalidation_type == "multiple":
            for company in ResCompany.sudo().search(
                [("has_eshop", "=", True)]
            ):
                for id in self.ids:
                    self._invalidate_eshop(company, id)
