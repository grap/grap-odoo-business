# Copyright (C) 2013 - Today: GRAP (http://www.grap.coop)
# @author Julien WESTE
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from lxml import etree
from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError
import odoo.addons.decimal_precision as dp
from odoo.osv.orm import setup_modifiers


class ProductSupplierinfo(models.Model):
    _inherit = 'product.supplierinfo'

    # Columns section
    package_qty = fields.Float(
        string='Package Qty', digits_compute=dp.get_precision('Product UoM'),
        default=1, help="The quantity of products in the supplier package."
        " You will always have to buy a multiple of this quantity.")

    indicative_package = fields.Boolean(
        string='Indicative Package',
        help="If checked, the system will not force you to purchase"
        "a strict multiple of package quantity")

    # Constrains Section
    @api.constrains('package_qty')
    def _check_package_qty(self):
        names = self.filtered(lambda x: x.package_qty == 0)
        if names:
            raise UserError(_(
                "Error for the following products. The package quantity"
                " cannot be null.\n - " % ('\n -'.join(names))))

    # View Section
    @api.model
    def fields_view_get(
            self, view_id=None, view_type='form', toolbar=False,
            submenu=False):
        res = super(ProductSupplierinfo, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar,
            submenu=False)
        if view_type == 'form':
            doc = etree.XML(res['arch'])
            nodes = doc.xpath("//field[@name='package_qty']")
            if nodes:
                nodes[0].set('required', '1')
                setup_modifiers(nodes[0], res['fields']['package_qty'])
                res['arch'] = etree.tostring(doc)
        return res
