# Copyright (C) 2016 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class CertifierOrganization(models.Model):
    _name = "certifier.organization"
    _description = "Certifier Organization"

    code = fields.Char(string="Code", required=True)

    name = fields.Char(string="Name", required=True)

    active = fields.Boolean(string="Active", default=True)

    website = fields.Char(string="Website")

    note = fields.Text(string="Note")
