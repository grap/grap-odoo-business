# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # Columns Section
    consignor_partner_id = fields.Many2one(
        string="Consignor",
        comodel_name="res.partner",
        domain="[('is_consignor', '=', True)]",
    )

    is_consignment = fields.Boolean(
        string="Is Consignment Product", store=True, compute="_compute_is_consignment"
    )

    # Overload to update domain
    fiscal_classification_id = fields.Many2one(
        domain="[('company_id', '=', company_id),"
        "('consignor_partner_id', '=', consignor_partner_id)"
        "]"
    )

    # Constrains section
    @api.constrains("consignor_partner_id", "fiscal_classification_id")
    def _check_consignor_fiscal_classification(self):
        # Note: when writting correct (new_consignor, new_fiscal_classification)
        # on a product.product, it will realize 2 write on product.template
        # a field then the other field. As a result, the constrains will
        # be raised.
        # Looks like a new weird behaviour of the ORM in V16.
        # Let's wait if it's a blocking point, and if it requires to
        # write alternative check.
        for product in self:
            if (
                product.consignor_partner_id
                != product.fiscal_classification_id.consignor_partner_id
            ):
                raise ValidationError(
                    _(
                        "The product '{product_name} has inconsistent"
                        " consignor ({consignor_name}) and"
                        " fiscal classification ({classification_name})."
                    ).format(
                        product_name=product.name,
                        consignor_name=product.consignor_partner_id.name,
                        classification_name=product.fiscal_classification_id.name,
                    )
                )

    # Compute Section
    @api.depends("consignor_partner_id")
    def _compute_is_consignment(self):
        for template in self:
            template.is_consignment = template.consignor_partner_id.id is not False

    # Onchange Section
    @api.onchange("consignor_partner_id")
    def onchange_consignor_partner_id_template(self):
        self._onchange_consignor_partner_id(self)

    @api.model
    def _onchange_consignor_partner_id(self, item):
        """Private function called with product or template in the item."""
        if not item.consignor_partner_id:
            return
        else:
            item.standard_price = 0
            item.seller_ids = False
            vals = {
                # "pricelist_ids": [],
                "partner_id": item.consignor_partner_id.id,
                "sequence": 1,
                "company_id": item.company_id.id,
                "delay": 1,
                "min_qty": 0,
                "product_code": False,
                "product_name": False,
            }
            item.seller_ids = [(0, False, vals)]
            if len(item.consignor_partner_id.consignor_fiscal_classification_ids):
                item.fiscal_classification_id = (
                    item.consignor_partner_id.consignor_fiscal_classification_ids[0]
                )
            else:
                item.fiscal_classification_id = False

    # Constrains Section
    @api.constrains("standard_price", "consignor_partner_id", "seller_ids")
    def _check_consignor_partner_id_fields_template(self):
        self._check_consignor_partner_id_fields()

    def _check_consignor_partner_id_fields(self):
        for template in self.filtered(lambda x: x.consignor_partner_id):
            if template.standard_price:
                raise ValidationError(
                    _("A consigned product must have null Cost Price")
                )
            if len(
                template.seller_ids.filtered(
                    lambda x, template=template: x.partner_id
                    != template.consignor_partner_id
                )
            ):
                raise ValidationError(
                    _(
                        "A consigned product can only have the consignor"
                        " in the field 'Suppliers'."
                    )
                )

    # Overload Section
    @api.model_create_multi
    def create(self, vals_list):
        templates = super().create(vals_list)

        # Handle pricelist exceptions
        new_templates = templates.filtered(lambda x: x.consignor_partner_id)
        if new_templates:
            self.env["product.pricelist"].consignmment_create(new_templates)
        return templates

    def write(self, vals):
        if "consignor_partner_id" in vals.keys():
            templates = self.filtered(
                lambda x: x.consignor_partner_id.id != vals.get("consignor_partner_id")
            )
            templates._check_consignor_changes()

        # Handle pricelist exceptions
        ProductPricelist = self.env["product.pricelist"]
        drop_templates = self.env["product.template"]
        new_templates = self.env["product.template"]
        if "consignor_partner_id" in vals:
            for template in self:
                if template.consignor_partner_id and not vals.get(
                    "consignor_partner_id"
                ):
                    drop_templates |= template
                if not template.consignor_partner_id and vals.get(
                    "consignor_partner_id"
                ):
                    new_templates |= template
        if drop_templates:
            ProductPricelist.consignmment_drop(drop_templates)
        if new_templates:
            ProductPricelist.consignmment_create(new_templates)

        return super().write(vals)

    def _check_consignor_changes(self):
        """Prevent to change the consignor of the product if the product has
        been sold, via invoices.
        Overload this function in extra modules. (purchase, sale, point_of_sale, etc...)
        """
        AccountMoveLine = self.env["account.move.line"]
        for template in self:
            invoice_lines = AccountMoveLine.search(
                [("product_id", "in", template.product_variant_ids.ids)]
            )
            if len(invoice_lines):
                raise ValidationError(
                    _(
                        "You can not change the value of the field"
                        " 'Consignor' because the product is associated"
                        " to one or more Account Invoice Lines. You should"
                        " disable the product and create a new one."
                    )
                )

    def _get_product_accounts(self):
        if self.consignor_partner_id:
            return {
                "income": self.consignor_partner_id.consignment_account_id,
                "expense": self.consignor_partner_id.consignment_account_id,
            }
        return super()._get_product_accounts()
