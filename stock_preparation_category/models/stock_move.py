# coding: utf-8
# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    # Column Section
    prepare_categ_id = fields.Many2one(
        related="product_id.preparation_categ_id",
        comodel_name="stock.preparation.category",
        store=True,
        string="Preparation Category",
        readonly=True,
    )
