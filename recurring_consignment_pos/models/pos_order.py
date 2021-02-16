# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, models
from odoo.exceptions import UserError


class PosOrder(models.Model):
    _inherit = "pos.order"

    @api.constrains("partner_id")
    def _check_partner_id_recurring_consignment(self):
        if self.partner_id.is_consignor:
            raise UserError(_("You can not make PoS Orders to consignors"))
