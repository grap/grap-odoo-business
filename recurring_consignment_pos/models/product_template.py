# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, models
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # Constrains Section
    def _check_consignor_changes(self):
        PosSession = self.env["pos.session"]
        PosOrderLine = self.env["pos.order.line"]
        res = super()._check_consignor_changes()
        if PosSession.search([("state", "!=", "closed")]):
            raise ValidationError(
                _(
                    "You can not change the value of the field"
                    " 'Consignor' because a Pos Session is opened."
                    " Please make such changement when sessions"
                    " are closed."
                )
            )

        order_lines = PosOrderLine.search(
            [("product_id", "in", self.mapped("product_variant_ids").ids)]
        )
        if len(order_lines):
            raise ValidationError(
                _(
                    "You can not change the value of the field"
                    " 'Consignor' because the product is associated"
                    " to one or more PoS Order Lines. You should"
                    " disable the product and create a new one."
                )
            )
        return res
