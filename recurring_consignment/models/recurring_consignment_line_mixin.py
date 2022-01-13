# Copyright (C) 2021 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class recurring_consignmentLineMixin(models.AbstractModel):
    _name = "recurring.consignment.line.mixin"
    _description = "Recurring Consignment Sale Line Mixin"

    @api.model
    def _compute_purchase_price_recurring_consignement(
        self, sale_price, tax_ids, discount1, discount2, discount3
    ):
        pass

    @api.model
    def create(self, vals):
        print("**** create")
        print(vals)
        vals.update({"purchase_price": 1})
        return super().create(vals)

    # @api.multi
    # def write(self, vals):
    #     import pdb; pdb.set_trace()
    #     print("==== write")
    #     print(vals)
    #     return super().write(vals)
