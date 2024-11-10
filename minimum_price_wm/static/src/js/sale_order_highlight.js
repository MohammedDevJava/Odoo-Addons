odoo.define('minimum_price_wm.sale_order', function (require) {
    "use strict";

    var core = require('web.core');
    var _t = core._t;
    var ListRenderer = require('web.ListRenderer');

    ListRenderer.include({
        _renderRow: function (record, index) {
            var $row = this._super.apply(this, arguments);
                // If the 'price_below_minimum' field is set, apply the 'text-danger' class
            if (record.data.test_js) {
                    $row.addClass('text-danger');
            }

            // Check if the record contains the 'price_below_minimum' field, which indicates the price is below the minimum
//            var priceUnit = record.data.price_unit;
//            var minimumPrice = record.data.product_id && record.data.product_id.minimum_price;
//            if (priceUnit && minimumPrice && priceUnit < minimumPrice) {

//               console.log("this is working")
//               $row.addClass('text-danger'); // Apply the 'text-danger' class to make text red
//            }
            return $row;
        },
    });

});

