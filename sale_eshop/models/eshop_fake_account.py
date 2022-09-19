# Copyright (C) 202-Today GRAP (http://www.grap.coop)
# @author: Mouna Sebti (https://twitter.com/m0unasb)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class EshopFakeAccount(models.Model):
    _name = "eshop.fake.account"
    _description = "Eshop Fake Account"
    _order = "create_date desc"

    form_data = fields.Char("Form Data")
    company_id = fields.Many2one(string="Company", comodel_name="res.company")

    @api.model
    def eshop_log_fake_account(self, form_data):
        self.create(
            {"form_data": str(form_data), "company_id": self.env.user.company_id.id}
        )
