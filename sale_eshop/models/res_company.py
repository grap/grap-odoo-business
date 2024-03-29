# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ResCompany(models.Model):
    _name = "res.company"
    _inherit = ["res.company", "eshop.with.image.mixin"]

    # Inherit Section
    _eshop_invalidation_type = "single"

    _eshop_fields = [
        "eshop_home_text",
        "name",
        "has_eshop",
        "eshop_minimum_price",
        "eshop_title",
        "website",
        "eshop_list_view_enabled",
        "eshop_tree_view_enabled",
        "social_facebook",
        "social_linkedin",
        "social_instagram",
        "eshop_image_small",
        "eshop_vat_included",
        "eshop_register_allowed",
        "eshop_manage_recovery_moment",
    ]

    _eshop_image_fields = ["eshop_image_small"]

    # Columns Section
    has_eshop = fields.Boolean(string="Has eShop")

    eshop_pricelist_id = fields.Many2one(
        comodel_name="product.pricelist", string="Pricelist Used"
    )

    eshop_minimum_price = fields.Float(string="Minimum Price by eShop")

    eshop_manage_recovery_moment = fields.Boolean(string="Manage recovery Moment")

    eshop_title = fields.Char(string="eShop Title")

    eshop_home_text = fields.Html(string="Text for the eShop Home Page")

    eshop_image_small = fields.Binary(string="Small Image for the eShop Menu")

    eshop_vat_included = fields.Boolean(string="VAT Included")

    eshop_register_allowed = fields.Boolean(
        string="Allow Register", help="Allow new customer to register on eShop"
    )

    eshop_list_view_enabled = fields.Boolean(
        string="Enable List View",
        default=True,
        help="Provide a List view to realize quick purchase.",
    )

    eshop_tree_view_enabled = fields.Boolean(
        string="Enable Tree View",
        default=True,
        help="Provide a Tree view to navigate into the catalog.",
    )

    # fields related to ir.config_parameter
    eshop_url = fields.Char(
        string="eShop URL",
        compute="_compute_eshop_url",
    )

    eshop_invalidation_key = fields.Char(
        string="Invalidation Key",
        compute="_compute_eshop_invalidation_key",
    )

    def _get_eshop_config_name(self, param_name):
        self.ensure_one()
        db_prefix = self._cr.dbname.split("_")[0]
        return f"sale_eshop.{param_name}__{db_prefix}__{self.id}"

    # Compute Section
    def _compute_eshop_url(self):
        IrConfigParameter = self.env["ir.config_parameter"].sudo()
        for company in self:
            company.eshop_url = IrConfigParameter.get_param(
                company._get_eshop_config_name("eshop_url")
            )

    def _compute_eshop_invalidation_key(self):
        IrConfigParameter = self.env["ir.config_parameter"].sudo()
        for company in self:
            company.eshop_invalidation_key = IrConfigParameter.get_param(
                company._get_eshop_config_name("eshop_invalidation_key")
            )

    # Overwrite section
    @api.model
    def _get_eshop_domain(self):
        return [("id", "=", self.env.user.company_id.id)]

    @api.model
    def create(self, vals):
        res = super().create(vals)
        res._create_parameter_if_not_exists()
        return res

    @api.multi
    def write(self, vals):
        res = super().write(vals)
        self._create_parameter_if_not_exists()
        return res

    @api.multi
    def _create_parameter_if_not_exists(self):
        IrConfigParameter = self.env["ir.config_parameter"].sudo()
        for company in self.filtered(lambda x: x.has_eshop):
            for config_name in ["eshop_url", "eshop_invalidation_key"]:
                key = company._get_eshop_config_name(config_name)
                param = IrConfigParameter.search([("key", "=", key)])
                if not param:
                    IrConfigParameter.create(
                        {
                            "key": key,
                            "value": "unset",
                        }
                    )
