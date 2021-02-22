// Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
// @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
// License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

odoo.define('recurring_consignment_pos.recurring_consignment', function (require) {
    'use strict';

    var models = require('point_of_sale.models');

    var PosModel_super = models.PosModel.prototype;

    models.PosModel = models.PosModel.extend({
        load_server_data: function () {
            var self = this;
            _.each(self.models, function (item) {
                if (item.model === 'res.partner') {
                    item.domain.push(['is_consignor', '=', false]);
                }
            });
            return PosModel_super.load_server_data.apply(this, arguments);
        },
    });

});
