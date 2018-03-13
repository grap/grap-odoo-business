# coding: utf-8
# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError


class ResCompany(models.Model):
    _inherit = 'res.company'

    certifier_organization_id = fields.Many2one(
        comodel_name='certifier.organization',
        string='Certifier Organization')
