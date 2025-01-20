# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    certifier_organization_id = fields.Many2one(
        comodel_name="certifier.organization", string="Certifier Organization"
    )

    report_certifier_text = fields.Text(compute="_compute_report_certifier_text")

    def _compute_report_certifier_text(self):
        for company in self:
            if company.certifier_organization_id:
                company.report_certifier_text = _(
                    "Products marked as 'ORG' are certified by %(certifier_code)s.",
                    certifier_code=company.certifier_organization_id.code,
                )
            else:
                company.report_certifier_text = ""
