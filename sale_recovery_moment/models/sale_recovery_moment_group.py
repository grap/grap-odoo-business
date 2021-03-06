# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from datetime import datetime

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError, Warning as UserError

import odoo.addons.decimal_precision as dp


class SaleRecoveryMomentGroup(models.Model):
    _name = "sale.recovery.moment.group"
    _description = "Recovery Groups"
    _order = "min_sale_date desc, name"

    _STATE_SELECTION = [
        ("undefined", "Undefined"),
        ("futur", "Futur"),
        ("pending_sale", "Pending Sale"),
        ("finished_sale", "Finished Sale"),
        ("pending_recovery", "Pending Recovery"),
        ("finished_recovery", "Finished Recovery"),
    ]

    # Column Section
    code = fields.Char(string="Code", readonly=True, required=True, default="/")

    short_name = fields.Char(string="Short Name", required=True)

    name = fields.Char(compute="_compute_name", string="Name", store=True)

    min_sale_date = fields.Datetime(string="Minimum date for the Sale", required=True)

    max_sale_date = fields.Datetime(string="Maximum date for the Sale", required=True)

    min_recovery_date = fields.Datetime(
        compute="_compute_recovery_date",
        multi="recovery_date",
        string="Minimum date for the Recovery",
        store=True,
    )

    max_recovery_date = fields.Datetime(
        compute="_compute_recovery_date",
        multi="recovery_date",
        string="Maximum date for the Recovery",
        store=True,
    )

    moment_ids = fields.One2many(
        comodel_name="sale.recovery.moment",
        inverse_name="group_id",
        string="Recovery Moments",
    )

    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        required=True,
        default=lambda x: x._default_company_id(),
    )

    order_qty = fields.Integer(
        compute="_compute_order_multi",
        multi="order",
        store=True,
        string="Sale Orders Quantity",
    )

    valid_order_qty = fields.Integer(
        compute="_compute_order_multi",
        multi="order",
        store=True,
        string="Valid Sale Orders Quantity",
    )

    picking_qty = fields.Integer(
        compute="_compute_picking_multi",
        multi="picking",
        store=True,
        string="Delivery Orders Quantity",
    )

    valid_picking_qty = fields.Integer(
        compute="_compute_picking_multi",
        multi="picking",
        store=True,
        string="Valid Delivery Orders Quantity",
    )

    excl_total = fields.Float(
        compute="_compute_total_multi",
        multi="total",
        store=True,
        digits=dp.get_precision("Account"),
        string="Total (VAT Excluded)",
    )

    incl_total = fields.Float(
        compute="_compute_total_multi",
        multi="total",
        store=True,
        digits=dp.get_precision("Account"),
        string="Total (VAT Included)",
    )

    state = fields.Selection(
        compute="_compute_state",
        string="State",
        search="_search_state",
        selection=_STATE_SELECTION,
    )

    # Defaults Section
    @api.model
    def _default_company_id(self):
        return self.env.user.company_id.id

    # Overload Section
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals["code"] = self.env["ir.sequence"].next_by_code(
                "sale.recovery.moment.group"
            )
        return super().create(vals_list)

    # Compute Section
    @api.multi
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

    @api.multi
    @api.depends("moment_ids.order_qty", "moment_ids.valid_order_qty")
    def _compute_order_multi(self):
        for moment_group in self:
            moment_group.order_qty = sum(moment_group.mapped("moment_ids.order_qty"))
            moment_group.valid_order_qty = sum(
                moment_group.mapped("moment_ids.valid_order_qty")
            )

    @api.multi
    @api.depends("moment_ids.picking_qty", "moment_ids.valid_picking_qty")
    def _compute_picking_multi(self):
        for moment_group in self:
            moment_group.picking_qty = sum(
                moment_group.mapped("moment_ids.picking_qty")
            )
            moment_group.valid_picking_qty = sum(
                moment_group.mapped("moment_ids.valid_picking_qty")
            )

    @api.multi
    @api.depends("valid_order_qty")
    def _compute_total_multi(self):
        for moment_group in self:
            orders = moment_group.mapped("moment_ids.order_ids").filtered(
                lambda x: x.state not in ("draft", "cancel")
            )
            moment_group.excl_total = sum(orders.mapped("amount_untaxed"))
            moment_group.incl_total = sum(orders.mapped("amount_total"))

    @api.multi
    @api.depends("code", "short_name")
    def _compute_name(self):
        for moment_group in self:
            moment_group.name = "{} - {}".format(
                moment_group.code,
                moment_group.short_name,
            )

    @api.multi
    def _compute_state(self):
        now = datetime.now()
        for moment_group in self:
            if not moment_group.moment_ids:
                moment_group.state = "undefined"
            elif now < moment_group.min_sale_date:
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
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if operator not in ("=", "in"):
            raise UserError(_("The Operator %s is not implemented !") % (operator))
        if operator == "=":
            lst = [operand]
        else:
            lst = operand
        sql_lst = []
        if "futur" in lst:
            sql_lst.append("('%s' < min_sale_date)" % (now))
        if "pending_sale" in lst:
            sql_lst.append(
                ("(min_sale_date < '%s'" + " AND '%s' < max_sale_date)") % (now, now)
            )
        if "finished_sale" in lst:
            sql_lst.append(
                ("(max_sale_date < '%s'" + " AND '%s'<min_recovery_date)") % (now, now)
            )
        if "pending_recovery" in lst:
            sql_lst.append(
                ("(min_recovery_date < '%s'" + " AND '%s' < max_recovery_date)")
                % (now, now)
            )
        if "finished_recovery" in lst:
            sql_lst.append("(max_recovery_date < '%s')" % (now))

        where = sql_lst[0]
        for item in sql_lst[1:]:
            where += " OR %s" % (item)

        req = "SELECT id FROM sale_recovery_moment_group WHERE %s;" % (where)

        sql_req = req  # pylint: disable=sql-injection
        self.env.cr.execute(sql_req)  # pylint: disable=invalid-commit
        res = self.env.cr.fetchall()
        return [("id", "in", [x[0] for x in res])]

    # Constraint Section
    @api.multi
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
