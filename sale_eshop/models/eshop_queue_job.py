# coding: utf-8
# Copyright (C) 2014-Today GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging
import requests
from requests.compat import urljoin

from openerp import api, fields, models

_logger = logging.getLogger(__name__)


class EshopQueueJob(models.Model):
    _name = "eshop.queue.job"
    _inherit = "ir.needaction_mixin"
    _order = "job_date desc"

    job_date = fields.Datetime(
        string="Job Date", required=True, readonly=True, select=True
    )

    company_id = fields.Many2one(comodel_name="res.company")

    model_name = fields.Char(required=True)

    item_identifier = fields.Integer(required=True)

    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("done", "Done"),
            ("skipped", "Skipped"),
            ("errored", "Errored"),
        ],
        default="draft",
    )

    # View Section
    @api.model
    def _needaction_count(self, domain=None, context=None):
        return len(self.search([("state", "not in", ["done", "skipped"])]))

    # Cron Section
    @api.model
    def cron_run(self):
        jobs = self.search(
            [("state", "not in", ["done", "skipped"])], order="job_date"
        )
        jobs.send_invalidation()

    @api.multi
    def send_invalidation(self):
        done_list = []
        for job in self:
            signature = (job.model_name, job.item_identifier)
            base_url = job.company_id.eshop_url
            private_key = job.company_id.eshop_invalidation_key
            if not (base_url and private_key):
                job.state = "skipped"
                _logger.warning(
                    "Invalidation has not been possible because"
                    " eshop_url and or eshop_invalidation_key is not available"
                    " for company %d" % job.company_id.id
                )
                continue

            if signature in done_list:
                job.state = "skipped"
                continue

            url = urljoin(
                base_url,
                "invalidation_cache/%s/%s/%d/"
                % (private_key, job.model_name, job.item_identifier),
            )
            try:
                req = requests.get(url, verify=False)
                if req.status_code == 200:
                    job.state = "done"
                    done_list.append(signature)
                else:
                    job.state = "errored"
                    _logger.error(
                        "Error when calling invalidation url '%s' "
                        " status Code : %s (company #%d)"
                        % (url, req.status_code, job.company_id.id)
                    )
            except Exception:
                job.state = "errored"
                _logger.error(
                    "Unable to call the invalidation url '%s' "
                    "(company #%d)" % (url, job.company_id.id)
                )
