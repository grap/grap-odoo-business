# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models


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
        """Handle Shipping product of recovery_moment"""
        self._set_commitment_date_from_moment_id(vals)

        for order in self:
            if "recovery_moment_id" in vals:
                SaleOrderLine = self.env["sale.order.line"]
                SaleRecoveryMoment = self.env["sale.recovery.moment"]
                SaleRecoveryPlace = self.env["sale.recovery.place"]
                # For all changes on recovery_moment_id changes,
                # delete shipping line to be idempotent
                SaleOrderLine.search(
                    [("order_id", "=", order.id), ("is_shipping", "=", True)]
                ).unlink()

                if not vals.get("recovery_moment_id"):
                    # User delete recovery moment, nothing to do
                    continue
                else:
                    # Create Shipping line
                    rec_mom = SaleRecoveryMoment.browse(vals.get("recovery_moment_id"))
                    place = SaleRecoveryPlace.browse(rec_mom.place_id.id)
                    if place.shipping_product_id:
                        prod = place.shipping_product_id.product_variant_ids[0].id
                        SaleOrderLine.create(
                            {
                                "order_id": order.id,
                                "is_shipping": True,
                                "product_id": prod,
                                "name": str(
                                    _("Extra cost linked to Recovery Moment:")
                                    + rec_mom.name
                                ),
                            }
                        )
        return super().write(vals)

    # Custom Section
    @api.model
    def _set_commitment_date_from_moment_id(self, vals):
        SaleRecoveryMoment = self.env["sale.recovery.moment"]
        if vals.get("recovery_moment_id", False):
            moment = SaleRecoveryMoment.browse(vals.get("recovery_moment_id"))
            vals["commitment_date"] = moment.min_recovery_date
