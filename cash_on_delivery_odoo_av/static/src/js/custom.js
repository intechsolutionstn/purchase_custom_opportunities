odoo.define('cash_on_delivery_odoo_av.website_cod_payment', function(require) {
    
    "use strict";
    
    var core = require('web.core');
    var ajax = require('web.ajax');
    var _t = core._t;

    var flag = 0;

    $(document).ready(function() {
        var oe_website_sale = this;
        var $payment = $("panel panel-default");
        var $carrier = $("#delivery_carrier");
        var payment_form = $('.o_payment_form');
        payment_form.find('.card-body').each(function(){
            if($(this).find('label').length == 0){
                $(this).hide();
            }
        });
        if(payment_form.find('.card-body').css('display') == 'none'){
            payment_form.parent().hide()
        }
    });       
});
