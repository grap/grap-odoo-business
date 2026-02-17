# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from datetime import datetime, timedelta

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.exceptions import Warning as UserError
from odoo.fields import Datetime
from odoo.osv import expression


class SaleRecoveryMomentGroup(models.Model):
    _name = "sale.recovery.moment.group"
    _description = "Recovery Groups"
    _order = "min_sale_date desc, name"

    _STATE_SELECTION = [
        ("futur", "Futur"),
        ("pending_sale", "Pending Sale"),
        ("finished_sale", "Finished Sale"),
        ("pending_recovery", "Pending Recovery"),
        ("finished_recovery", "Finished Recovery"),
    ]

    code = fields.Char(readonly=True, required=True, default="/")

    short_name = fields.Char(required=True)

    name = fields.Char(compute="_compute_name", store=True)

    min_sale_date = fields.Datetime(
        string="Minimum date for the Sale",
        required=True,
        default=lambda x: x._default_min_sale_date(),
    )

    max_sale_date = fields.Datetime(
        string="Maximum date for the Sale",
        required=True,
        default=lambda x: x._default_max_sale_date(),
    )

    min_recovery_date = fields.Datetime(
        string="Minimum date for the Recovery",
        compute="_compute_recovery_date",
        store=True,
    )

    max_recovery_date = fields.Datetime(
        string="Maximum date for the Recovery",
        compute="_compute_recovery_date",
        store=True,
    )

    moment_ids = fields.One2many(
        string="Recovery Moments",
        comodel_name="sale.recovery.moment",
        inverse_name="group_id",
    )

    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        required=True,
        default=lambda x: x._default_company_id(),
    )

    order_qty = fields.Integer(
        string="Sale Orders Quantity", compute="_compute_order_multi", store=True
    )

    valid_order_qty = fields.Integer(
        string="Valid Sale Orders Quantity", compute="_compute_order_multi", store=True
    )

    picking_qty = fields.Integer(
        string="Delivery Orders Quantity", compute="_compute_picking_multi", store=True
    )

    valid_picking_qty = fields.Integer(
        string="Valid Delivery Orders Quantity",
        compute="_compute_picking_multi",
        store=True,
    )

    excl_total = fields.Float(
        string="Total (VAT Excluded)",
        compute="_compute_total_multi",
        store=True,
        digits="Account",
    )

    incl_total = fields.Float(
        string="Total (VAT Included)",
        compute="_compute_total_multi",
        store=True,
        digits="Account",
    )

    state = fields.Selection(
        compute="_compute_state", search="_search_state", selection=_STATE_SELECTION
    )

    # Defaults Section
    @api.model
    def _default_company_id(self):
        return self.env.company

    @api.model
    def _default_min_sale_date(self):
        return datetime.now()

    @api.model
    def _default_max_sale_date(self):
        return datetime.now() + timedelta(hours=6)

    # Overload Section
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals["code"] = self.env["ir.sequence"].next_by_code(
                "sale.recovery.moment.group"
            )
        return super().create(vals_list)

    # Compute Section
    @api.depends("moment_ids.min_recovery_date", "moment_ids.max_recovery_date")
    def _compute_recovery_date(self):
        for moment_group in self:
            if len(moment_group.moment_ids) > 0:
                moments = moment_group.moment_ids
                moment_group.min_recovery_date = min(
                    [x.min_recovery_date for x in moments]
                )
                moment_group.max_recovery_date = min(
                    [x.max_recovery_date for x in moments]
                )

    @api.depends("moment_ids.order_qty", "moment_ids.valid_order_qty")
    def _compute_order_multi(self):
        for moment_group in self:
            moment_group.order_qty = sum(moment_group.mapped("moment_ids.order_qty"))
            moment_group.valid_order_qty = sum(
                moment_group.mapped("moment_ids.valid_order_qty")
            )

    @api.depends("moment_ids.picking_qty", "moment_ids.valid_picking_qty")
    def _compute_picking_multi(self):
        for moment_group in self:
            moment_group.picking_qty = sum(
                moment_group.mapped("moment_ids.picking_qty")
            )
            moment_group.valid_picking_qty = sum(
                moment_group.mapped("moment_ids.valid_picking_qty")
            )

    @api.depends("valid_order_qty")
    def _compute_total_multi(self):
        for moment_group in self:
            orders = moment_group.mapped("moment_ids.order_ids").filtered(
                lambda x: x.state not in ("draft", "cancel")
            )
            moment_group.excl_total = sum(orders.mapped("amount_untaxed"))
            moment_group.incl_total = sum(orders.mapped("amount_total"))

    @api.depends("code", "short_name")
    def _compute_name(self):
        for moment_group in self:
            moment_group.name = f"{moment_group.code} - {moment_group.short_name}"

    @api.depends(
        "min_sale_date", "max_sale_date", "min_recovery_date", "max_recovery_date"
    )
    def _compute_state(self):
        now = datetime.now()
        for moment_group in self:
            if now < moment_group.min_sale_date:
                moment_group.state = "futur"
            elif now < moment_group.max_sale_date:
                moment_group.state = "pending_sale"
            elif now < moment_group.min_recovery_date:
                moment_group.state = "finished_sale"
            elif now < moment_group.max_recovery_date:
                moment_group.state = "pending_recovery"
            else:
                moment_group.state = "finished_recovery"

    # Search Functions Section
    def _search_state(self, operator, operand):
        domain = []
        now = Datetime.now()
        if operator not in ("=", "in"):
            raise UserError(_("The Operator %s is not implemented !") % (operator))
        if operator == "=":
            lst = [operand]
        else:
            lst = operand
        if "futur" in lst:
            expression.OR([domain, [("min_sale_date", ">", now)]])
        if "pending_sale" in lst:
            expression.OR(
                [domain, [("min_sale_date", "<", now), ("max_sale_date", ">", now)]]
            )
        if "finished_sale" in lst:
            expression.OR(
                [domain, [("max_sale_date", "<", now), ("min_recovery_date", ">", now)]]
            )
        if "pending_recovery" in lst:
            expression.OR(
                [
                    domain,
                    [("min_recovery_date", "<", now), ("max_recovery_date", ">", now)],
                ]
            )
        if "finished_recovery" in lst:
            expression.OR([domain, [("max_recovery_date", "<", now)]])
        return domain

    # Constraint Section
    @api.constrains("min_sale_date", "max_sale_date")
    def _check_sale_dates(self):
        for moment_group in self:
            if moment_group.min_sale_date >= moment_group.max_sale_date:
                raise ValidationError(
                    _(
                        "The minimum Date of Sale must be before the maximum"
                        " Date of Sale."
                    )
                )
