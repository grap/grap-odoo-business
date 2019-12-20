# Copyright (C) 2012 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    label_ids = fields.Many2many(
        comodel_name="product.label",
        string="Labels",
        compute="_compute_label_ids")

    @api.depends(
        "invoice_line_ids.product_id.label_ids.display_on_invoice")
    def _compute_label_ids(self):
        for invoice in self:
            invoice.label_ids = invoice.mapped(
                'invoice_line_ids.product_id.label_ids').filtered(
                lambda x: x.display_on_invoice)
