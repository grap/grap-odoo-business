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
    # Basic Settings
    eshop_title = fields.Char(
        string="eShop Title",
        default=lambda s: s._default_eshop_title(),
    )

    eshop_minimum_price = fields.Float(
        string="Minimum Cart Amount",
        default=lambda s: s._default_eshop_minimum_price(),
    )

    eshop_pricelist_id = fields.Many2one(
        comodel_name="product.pricelist",
        string="Pricelist Used",
        default=lambda s: s._default_eshop_pricelist_id(),
    )

    eshop_vat_included = fields.Boolean(
        string="VAT Included",
        default=lambda s: s._default_eshop_vat_included(),
    )

    # Hosting informations
    eshop_hosting = fields.Html(
        string="Web hosting informations",
        default=lambda s: s._default_eshop_hosting(),
    )

    eshop_registered_capital = fields.Float(
        string="Registered capital",
        default=lambda s: s._default_eshop_registered_capital(),
    )

    eshop_consumer_mediation = fields.Char(
        string="Consumer Mediator",
        default=lambda s: s._default_eshop_consumer_mediation(),
    )

    # Options
    eshop_register_allowed = fields.Boolean(
        string="Allow register",
        default=lambda s: s._default_eshop_register_allowed(),
    )
    eshop_register_phone_required = fields.Boolean(
        string="Phone number is required",
        default=lambda s: s._default_eshop_register_phone_required(),
    )
    eshop_list_view_enabled = fields.Boolean(
        string="Enable List View",
        default=lambda s: s._default_eshop_list_view_enabled(),
    )
    eshop_catalog_view_enabled = fields.Boolean(
        string="Enable Tree View",
        default=lambda s: s._default_eshop_catalog_view_enabled(),
    )

    # Payment options
    eshop_pay_on_site = fields.Boolean(
        string="Enable payment on site",
        default=lambda s: s._default_eshop_pay_on_site(),
    )
    eshop_pay_on_site_text = fields.Html(
        string="Payment methods on site",
        default=lambda s: s._default_eshop_pay_on_site_text(),
    )
    eshop_wallet_enabled = fields.Boolean(
        string="Enable Account Customer Wallet",
        default=lambda s: s._default_eshop_wallet_enabled(),
    )
    eshop_wallet_recharge_bank_transfer = fields.Boolean(
        string="Enable recharging Wallet account with bank transfer",
        default=lambda s: s._default_eshop_wallet_recharge_bank_transfer(),
    )
    eshop_mollie_enabled = fields.Boolean(
        string="Enable online payment with Mollie.com",
        default=lambda s: s._default_eshop_mollie_enabled(),
    )

    # Social fields
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

    # Technical Settings
    eshop_url = fields.Char(
        string="eShop URL",
        default=lambda s: s._default_eshop_url(),
        readonly=True,
    )

    eshop_invalidation_key = fields.Char(
        string="Invalidation Key",
        default=lambda s: s._default_eshop_invalidation_key(),
        readonly=True,
    )

    # Default Section
    @api.model
    def _default_company_id(self):
        return self.env.company.id

    # Basic Settings
    @api.model
    def _default_eshop_title(self):
        return self.env.company.eshop_title

    @api.model
    def _default_eshop_minimum_price(self):
        return self.env.company.eshop_minimum_price

    @api.model
    def _default_eshop_pricelist_id(self):
        return self.env.company.eshop_pricelist_id

    @api.model
    def _default_eshop_vat_included(self):
        return self.env.company.eshop_vat_included

    # Hosting informations
    @api.model
    def _default_eshop_hosting(self):
        return self.env.company.eshop_hosting

    @api.model
    def _default_eshop_registered_capital(self):
        return self.env.company.eshop_registered_capital

    @api.model
    def _default_eshop_consumer_mediation(self):
        return self.env.company.eshop_consumer_mediation

    # Options
    @api.model
    def _default_eshop_register_allowed(self):
        return self.env.company.eshop_register_allowed

    @api.model
    def _default_eshop_register_phone_required(self):
        return self.env.company.eshop_register_phone_required

    @api.model
    def _default_eshop_list_view_enabled(self):
        return self.env.company.eshop_list_view_enabled

    @api.model
    def _default_eshop_catalog_view_enabled(self):
        return self.env.company.eshop_catalog_view_enabled

    # Payment options
    @api.model
    def _default_eshop_pay_on_site(self):
        return self.env.company.eshop_pay_on_site

    @api.model
    def _default_eshop_pay_on_site_text(self):
        return self.env.company.eshop_pay_on_site_text

    @api.model
    def _default_eshop_wallet_enabled(self):
        return self.env.company.eshop_wallet_enabled

    @api.model
    def _default_eshop_wallet_recharge_bank_transfer(self):
        return self.env.company.eshop_wallet_recharge_bank_transfer

    @api.model
    def _default_eshop_mollie_enabled(self):
        return self.env.company.eshop_mollie_enabled

    # Social fields
    @api.model
    def _default_social_facebook(self):
        return self.env.company.social_facebook

    @api.model
    def _default_social_linkedin(self):
        return self.env.company.social_linkedin

    @api.model
    def _default_social_instagram(self):
        return self.env.company.social_instagram

    @api.model
    def _default_eshop_home_text(self):
        return self.env.company.eshop_home_text

    # Technical fields related to ir.config_parameter
    @api.model
    def _default_eshop_url(self):
        return self.env.company.eshop_url

    @api.model
    def _default_eshop_invalidation_key(self):
        return self.env.company.eshop_invalidation_key

    # View Section
    def button_apply_settings(self):
        self.ensure_one()
        self.company_id.sudo().write(
            {
                "eshop_title": self.eshop_title,
                "eshop_minimum_price": self.eshop_minimum_price,
                "eshop_pricelist_id": self.eshop_pricelist_id,
                "eshop_vat_included": self.eshop_vat_included,
                "eshop_register_allowed": self.eshop_register_allowed,
                "eshop_register_phone_required": self.eshop_register_phone_required,
                "eshop_list_view_enabled": self.eshop_list_view_enabled,
                "eshop_catalog_view_enabled": self.eshop_catalog_view_enabled,
                "eshop_pay_on_site": self.eshop_pay_on_site,
                "eshop_pay_on_site_text": self.eshop_pay_on_site_text,
                "eshop_wallet_enabled": self.eshop_wallet_enabled,
                "eshop_wallet_recharge_bank_transfer": self.eshop_wallet_recharge_bank_transfer,
                "eshop_mollie_enabled": self.eshop_mollie_enabled,
                "social_facebook": self.social_facebook,
                "social_linkedin": self.social_linkedin,
                "social_instagram": self.social_instagram,
            }
        )

    def button_apply_website(self):
        self.ensure_one()
        self.company_id.sudo().write(
            {
                "eshop_title": self.eshop_title,
                "eshop_hosting": self.eshop_hosting,
                "eshop_registered_capital": self.eshop_registered_capital,
                "eshop_consumer_mediation": self.eshop_consumer_mediation,
                "eshop_home_text": self.eshop_home_text,
            }
        )
