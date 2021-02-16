# Copyright (C) 2020 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class ResCompany(models.Model):
    _inherit = "res.company"

    @api.model
    def create(self, vals):
        res = super().create(vals)
        res._create_consignor_sequence()
        return res

    @api.multi
    def _create_consignor_sequence(self):
        ResPartner = self.env["res.partner"]
        Irsequence = self.env["ir.sequence"]
        for company in self:
            _logger.info(
                "Creating consignor sequence for company '%s'" % (company.name)
            )
            current_consignor_qty = len(
                ResPartner.with_context(active_test=False).search(
                    [
                        ("company_id", "=", company.id),
                        ("is_consignor", "=", True),
                    ]
                )
            )
            Irsequence.create(
                company._prepare_consignor_sequence(current_consignor_qty)
            )

    @api.multi
    def _prepare_consignor_sequence(self, current_consignor_qty):
        self.ensure_one()
        return {
            "name": "Consignor sequence",
            "code": "consignor.create.wizard",
            "implementation": "no_gap",
            "company_id": self.id,
            "prefix": "Prod",
            "padding": 3,
            "number_next_actual": current_consignor_qty + 1,
        }
