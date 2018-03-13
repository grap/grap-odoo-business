# coding: utf-8
# Copyright (C) 2016 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class CertifierOrganization(models.Model):
    _name = 'certifier.organization'

    code = fields.Char(string='Code', required=True)

    name = fields.Char(string='Name', required=True)
