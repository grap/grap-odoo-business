# Copyright (C) 2021-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


def migrate(cr, version):
    # Move data
    # > FROM product_to_scale_bizerba / product_template.scale_tare_weight
    # > TO : pos_tare / product_product.tare_weight
    cr.execute(
        """
        UPDATE product_template pt
        SET tare_weight = pp.scale_tare_weight
        FROM product_product pp
        WHERE pp.product_tmpl_id = pt.id
        AND pp.scale_tare_weight != 0
        """
    )

    cr.execute(
        """
        UPDATE product_scale_system_product_line
        SET field_id = (
            SELECT id
            FROM ir_model_fields
            WHERE model = 'product.product'
            AND name='tare_weight')
        WHERE field_id = (
            SELECT id
            FROM ir_model_fields
            WHERE model = 'product.product'
            AND name='scale_tare_weight');
        """
    )
