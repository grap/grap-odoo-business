# coding: utf-8
# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import _, api, fields, models
from openerp.exceptions import ValidationError
from openerp.exceptions import Warning as UserError


class SaleRecoveryMoment(models.Model):
    _description = 'Recovery Moment'
    _name = 'sale.recovery.moment'
    _order = 'min_recovery_date desc, max_recovery_date desc, place_id'

    # Defaults Section
    @api.model
    def _default_code(self):
        return self.env['ir.sequence'].get('sale.recovery.moment')

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id

    # Columns Section
    code = fields.Char(
        string='Code', readonly=True, required=True, default=_default_code)

    name = fields.Char(
        string='Name', compute='_compute_name', store=True)

    place_id = fields.Many2one(
        comodel_name='sale.recovery.place', string='Place', required=True)

    group_id = fields.Many2one(
        string='Recovery Moment Group',
        comodel_name='sale.recovery.moment.group')

    company_id = fields.Many2one(
        string='Company', comodel_name='res.company', required=True,
        default=_default_company_id)

    specific_min_sale_date = fields.Datetime(
        string='Specific Minimum date for the Sale')

    specific_max_sale_date = fields.Datetime(
        string='Specific Maximum date for the Sale')

    min_sale_date = fields.Datetime(
        string='Minimum date for the Sale', compute='_compute_sale_date',
        store=True)

    max_sale_date = fields.Datetime(
        string='Maximum date for the Sale', compute='_compute_sale_date',
        store=True)

    min_recovery_date = fields.Datetime(
        string='Minimum date for the Recovery', required=True)

    max_recovery_date = fields.Datetime(
        string='Maximum date for the Recovery', required=True)

    description = fields.Text(string='Description')

    max_order_qty = fields.Integer('Max Order Quantity')

    order_ids = fields.One2many(
        comodel_name='sale.order', inverse_name='recovery_moment_id',
        string='Sale Orders', readonly=True)

    order_qty = fields.Integer(
        compute='_compute_order_multi', multi='order', store=True,
        string='Sale Orders Quantity')

    valid_order_qty = fields.Integer(
        compute='_compute_order_multi', multi='order', store=True,
        string='Valid Sale Orders Quantity')

    is_complete = fields.Boolean(
        compute='_compute_order_multi', multi='order', store=True,
        string='Is Complete')

    quota_description = fields.Char(
        compute='_compute_order_multi', multi='order', store=True,
        string='Quota Description')

    picking_ids = fields.One2many(
        comodel_name='stock.picking', inverse_name='recovery_moment_id',
        string='Delivery Orders', readonly=True)

    picking_qty = fields.Integer(
        compute='_compute_picking_multi', multi='picking', store=True,
        string='Delivery Orders Quantity')

    valid_picking_qty = fields.Integer(
        compute='_compute_picking_multi', multi='picking', store=True,
        string='Valid Delivery Orders Quantity')

    # Compute Section
    @api.multi
    @api.depends(
        'group_id.min_sale_date', 'group_id.max_sale_date',
        'specific_min_sale_date', 'specific_max_sale_date')
    def _compute_sale_date(self):
        for moment in self.filtered(lambda x: x.group_id):
            moment.min_sale_date = moment.group_id.min_sale_date
            moment.max_sale_date = moment.group_id.max_sale_date
        for moment in self.filtered(lambda x: not x.group_id):
            moment.min_sale_date = moment.specific_min_sale_date
            moment.max_sale_date = moment.specific_max_sale_date

    @api.multi
    @api.depends(
        'order_ids', 'order_ids.recovery_moment_id', 'order_ids.state',
        'max_order_qty')
    def _compute_order_multi(self):
        for recovery_moment in self:
            recovery_moment.order_qty = len(recovery_moment.order_ids)

            recovery_moment.valid_order_qty = len(
                recovery_moment.order_ids.filtered(
                    lambda x: x.state not in ('draft', 'cancel')))

            if recovery_moment.max_order_qty:
                recovery_moment.is_complete =\
                    recovery_moment.valid_order_qty >=\
                    recovery_moment.max_order_qty

            # Update Quota Description Field
            if recovery_moment.max_order_qty:
                recovery_moment.quota_description = _('%d / %d Orders') % (
                    recovery_moment.valid_order_qty,
                    recovery_moment.max_order_qty)
            elif recovery_moment.valid_order_qty:
                recovery_moment.quota_description = _('%d Order(s)') % (
                    recovery_moment.valid_order_qty)
            else:
                recovery_moment.quota_description = _('No Orders')

    @api.multi
    @api.depends(
        'picking_ids', 'picking_ids.recovery_moment_id', 'picking_ids.state')
    def _compute_picking_multi(self):
        for recovery_moment in self:
            recovery_moment.picking_qty = len(recovery_moment.picking_ids)

            recovery_moment.valid_picking_qty = len(
                recovery_moment.picking_ids.filtered(
                    lambda x: x.state not in ('draft', 'cancel')))

    @api.multi
    @api.depends(
        'code', 'min_recovery_date', 'place_id', 'group_id.short_name')
    def _compute_name(self):
        for moment in self.filtered(lambda x: x.group_id):
            moment.name = "%s - %s - %s - %s" % (
                moment.code,
                moment.group_id.short_name,
                moment.place_id.name,
                moment.min_recovery_date)
        for moment in self.filtered(lambda x: not x.group_id):
            moment.name = "%s - %s - %s" % (
                moment.code,
                moment.place_id.name,
                moment.min_recovery_date)

    # Constraint Section
    @api.multi
    @api.constrains('min_recovery_date', 'max_recovery_date')
    def _check_recovery_dates(self):
        for moment in self:
            if moment.min_recovery_date >= moment.max_recovery_date:
                raise ValidationError(_(
                    "The minimum Date of Recovery must be before the maximum"
                    " Date of Recovery."))

    # Overload Section
    @api.multi
    def unlink(self):
        if self.filtered(lambda x: x.valid_order_qty):
            raise UserError(
                _("You can not delete this Recovery Moment because there"
                    " is Valid Sale Orders associated.\nPlease move"
                    " Sale orders on an other Recovery Moment and contact"
                    " your customers."))
        return super(SaleRecoveryMoment, self).unlink()
