# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = "res.partner"

    # Columns Section
    is_consignor = fields.Boolean(readonly=True)

    consignment_commission = fields.Float(string="Commission Rate", tracking=True)

    consignment_account_id = fields.Many2one(
        string="Consignment Account",
        comodel_name="account.account",
        readonly=True,
        tracking=True,
    )

    consignor_fiscal_classification_ids = fields.One2many(
        string="Consignor Fiscal Classifications",
        comodel_name="account.product.fiscal.classification",
        inverse_name="consignor_partner_id",
        readonly=True,
    )

    # Constrains Section
    @api.constrains("is_consignor", "consignment_commission", "consignment_account_id")
    def _check_is_consignor_consignment_account_id(self):
        for partner in self:
            if partner.is_consignor:
                if not partner.consignment_account_id:
                    raise UserError(
                        _("A Consignor must have a 'Consignment Account' defined.")
                    )
            else:
                if (
                    partner.consignment_account_id
                    or partner.consignment_commission != 0
                ):
                    raise UserError(
                        _(
                            "A Non Consignor partner can not have 'Consignment"
                            " Commission' neither 'Consignment Account' defined."
                        )
                    )
