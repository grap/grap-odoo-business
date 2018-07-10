# coding: utf-8
# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp.osv import fields
from openerp.osv.orm import Model
from openerp.osv.osv import except_osv
from openerp.tools.translate import _


class ProductPricelist(Model):
    _inherit = 'product.pricelist'

    _columns = {
        'is_simple': fields.boolean(
            "Is Simple", help="""Check this box if you want to edit this"""
            """ pricelist by product"""),
    }

    # Constraints Section
    def _check_company_id_is_simple(self, cr, uid, ids, context=None):
        for pp in self.browse(cr, uid, ids, context=context):
            if (pp.is_simple and not pp.company_id):
                return False
        return True

    _constraints = [
        (
            _check_company_id_is_simple,
            """Error: Simple Pricelist must have a company defined""",
            ['company_id', 'is_simple']),
    ]

    def action_edit_simple_pricelist(self, cr, uid, ids, context=None):
        """
        This function returns an action that allow user to edit pricelist
        by products.
        """
        imd_obj = self.pool['ir.model.data']
        iaw_obj = self.pool['ir.actions.act_window']

        if len(ids) != 1:
            raise except_osv(
                _('Error!'),
                _("You can not Edit simple pricelist for many pricelists"))

        # Get the correct action
        id = imd_obj.get_object_reference(
            cr, uid, 'product_simple_pricelist',
            'action_edit_simple_pricelist')[1]
        res = iaw_obj.read(cr, uid, [id], context=context)[0]
        res['domain'] = "[('pricelist_id', '=', " + str(ids[0]) + ")]"
        return res
