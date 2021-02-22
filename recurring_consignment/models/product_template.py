# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # Columns Section
    consignor_partner_id = fields.Many2one(
        string="Consignor",
        comodel_name="res.partner",
        old_name="consignor_id",
        domain="[('is_consignor', '=', True)]",
    )

    is_consignment = fields.Boolean(
        string="Is Consignment Product", store=True, compute="_compute_is_consignment"
    )

    is_consignment_commission = fields.Boolean(string="Is Consignment Commission")

    # Overload to update domain
    fiscal_classification_id = fields.Many2one(
        domain="[('company_id', '=', company_id),"
        "('consignor_partner_id', '=', consignor_partner_id)"
        "]"
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
                "pricelist_ids": [],
                "name": item.consignor_partner_id.id,
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
    def _check_consignor_partner_id_fields(self):
        for template in self.filtered(lambda x: x.consignor_partner_id):
            if template.standard_price:
                raise UserError(_("A consigned product must have null Cost Price"))
            if len(
                template.seller_ids.filtered(
                    lambda x: x.name != template.consignor_partner_id
                )
            ):
                raise UserError(
                    _(
                        "A consigned product can only have the consignor"
                        " in the field 'Suppliers'."
                    )
                )

    # Overload Section
    @api.model
    def create(self, vals):
        vals = self._update_vals_consignor(vals)
        res = super().create(vals)
        if vals.get("consignor_partner_id", False):
            self.env["product.pricelist"].consignmment_create([res.id])
        return res

    @api.multi
    def write(self, vals):
        ProductPricelist = self.env["product.pricelist"]
        self._check_consignor_changes(vals)
        vals = self._update_vals_consignor(vals)
        drop_template_ids = []
        new_template_ids = []
        if "consignor_partner_id" in vals:
            for template in self:
                if template.consignor_partner_id and not vals.get(
                    "consignor_partner_id"
                ):
                    drop_template_ids.append(template.id)
                if not template.consignor_partner_id and vals.get(
                    "consignor_partner_id"
                ):
                    new_template_ids.append(template.id)
        if drop_template_ids:
            ProductPricelist.consignmment_drop(drop_template_ids)
        if new_template_ids:
            ProductPricelist.consignmment_create(new_template_ids)
        if vals.get("recurring_consignment", False):
            for template in self:
                if template.recurring_consignment != vals.get(
                    "recurring_consignment", False
                ):
                    raise UserError(
                        _(
                            "You can not change the value of the field"
                            " 'Is Consignment Commission'. You can disable"
                            " this product and create a new one properly."
                        )
                    )
        return super().write(vals)

    @api.multi
    def _check_consignor_changes(self, vals):
        AccountInvoiceLine = self.env["account.invoice.line"]
        if vals.get("consignor_partner_id", False):
            for template in self:
                product_ids = template.product_variant_ids.ids
                if template.consignor_partner_id.id != vals.get(
                    "consignor_partner_id", False
                ):
                    invoice_lines = AccountInvoiceLine.search(
                        [("product_id", "in", product_ids)]
                    )
                    if len(invoice_lines):
                        raise UserError(
                            _(
                                "You can not change the value of the field"
                                " 'Consignor' because the product is associated"
                                " to one or more Account Invoice Lines. You should"
                                " disable the product and create a new one."
                            )
                        )

    @api.model
    def _update_vals_consignor(self, vals):
        ResPartner = self.env["res.partner"]
        if vals.get("consignor_partner_id", False):
            partner = ResPartner.browse(vals.get("consignor_partner_id"))
            vals["purchase_ok"] = True
            vals["property_account_income_id"] = partner.consignment_account_id.id
            vals["property_account_expense_id"] = partner.consignment_account_id.id
        return vals
