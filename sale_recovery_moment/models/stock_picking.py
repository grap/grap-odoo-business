# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    recovery_moment_id = fields.Many2one(
        string="Recovery Moment", comodel_name="sale.recovery.moment"
    )

    recovery_group_id = fields.Many2one(
        string="Recovery Group",
        related="recovery_moment_id.group_id",
        comodel_name="sale.recovery.moment.group",
        store=True,
        readonly=True,
    )
