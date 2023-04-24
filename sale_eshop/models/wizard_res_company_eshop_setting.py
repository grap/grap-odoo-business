# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class WizardResCompanyEshopSetting(models.TransientModel):
    _name = "wizard.res.company.eshop.setting"
    _description = "Wizard Company Eshop Setting"

    # Columns Section
    company_id = fields.Many2one(
        comodel_name="res.company",
        required=True,
        readonly=True,
        default=lambda s: s._default_company_id(),
    )
    social_facebook = fields.Char(
        string="Facebook URL",
        default=lambda s: s._default_social_facebook(),
    )

    social_linkedin = fields.Char(
        string="LinkedIn URL", default=lambda s: s._default_social_linkedin()
    )

    social_instagram = fields.Char(
        string="Instagram URL",
        default=lambda s: s._default_social_instagram(),
    )

    eshop_home_text = fields.Html(
        string="Text for the eShop Home Page",
        default=lambda s: s._default_eshop_home_text(),
    )

    # Default Section
    @api.model
    def _default_company_id(self):
        return self.env.user.company_id.id

    @api.model
    def _default_social_facebook(self):
        return self.env.user.company_id.social_facebook

    @api.model
    def _default_social_linkedin(self):
        return self.env.user.company_id.social_linkedin

    @api.model
    def _default_social_instagram(self):
        return self.env.user.company_id.social_instagram

    @api.model
    def _default_eshop_home_text(self):
        return self.env.user.company_id.eshop_home_text

    # View Section
    @api.multi
    def button_apply_setting(self):
        self.ensure_one()
        self.company_id.sudo().write(
            {
                "social_facebook": self.social_facebook,
                "social_linkedin": self.social_linkedin,
                "social_instagram": self.social_instagram,
                "eshop_home_text": self.eshop_home_text,
            }
        )
