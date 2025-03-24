# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # Column Section
    recovery_moment_id = fields.Many2one(
        comodel_name="sale.recovery.moment",
        string="Recovery Moment",
        copy=False,
        readonly=True,
        states={"draft": [("readonly", False)]},
    )

    recovery_group_id = fields.Many2one(
        related="recovery_moment_id.group_id",
        comodel_name="sale.recovery.moment.group",
        readonly=True,
        string="Recovery Group",
        store=True,
    )

    # Overload Section
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            self._set_commitment_date_from_moment_id(vals)
        return super().create(vals_list)

    def write(self, vals):
        self._set_commitment_date_from_moment_id(vals)
        return super().write(vals)

    def action_confirm(self):
        # Add shipping product if the recovery moment
        # is related to a place with shipping product
        SaleOrderLine = self.env["sale.order.line"]
        for order in self.filtered(lambda x: x.recovery_moment_id.place_id):
            product = order.recovery_moment_id.place_id.shipping_product_id
            if product:
                SaleOrderLine.create(
                    {
                        "order_id": order.id,
                        "product_id": product.id,
                    }
                )

        return super().action_confirm()

    # Custom Section
    @api.model
    def _set_commitment_date_from_moment_id(self, vals):
        SaleRecoveryMoment = self.env["sale.recovery.moment"]
        if vals.get("recovery_moment_id", False):
            moment = SaleRecoveryMoment.browse(vals.get("recovery_moment_id"))
            vals["commitment_date"] = moment.min_recovery_date
