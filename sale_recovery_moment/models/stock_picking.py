# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    recovery_moment_id = fields.Many2one(
        comodel_name="sale.recovery.moment", string="Recovery Moment"
    )

    recovery_group_id = fields.Many2one(
        related="recovery_moment_id.group_id",
        comodel_name="sale.recovery.moment.group",
        store=True,
        string="Recovery Group",
        readonly=True,
    )

    @api.multi
    def _compute_print_summary_extra_info(self):
        super()._compute_print_summary_extra_info()
        for picking in self.filtered(lambda x: x.recovery_moment_id):
            extra_info = picking.print_summary_extra_info
            if not extra_info:
                extra_info = ""
            else:
                extra_info += "<br />"
            if picking.sale_id and picking.sale_id.note:
                extra_info += picking.sale_id.note
            extra_info += "<br />"
            extra_info += _("Recovery: %s (%s)") % (
                picking.recovery_moment_id.place_id.name,
                picking.recovery_moment_id.min_sale_date,
            )
            picking.print_summary_extra_info = extra_info
