from odoo import api, fields, models, _
from odoo.exceptions import UserError



class SaleOrder(models.Model):
    _inherit = 'sale.order'
    test_js = fields.Boolean(string="Test",  store=True, default=True)

    @api.onchange('order_line', 'order_line.price_unit')
    def _onchange_order_line(self):
        warning = self.check_min_price_warning()
        if warning:
            return warning
    def check_min_price_warning(self):
        warning = {}
        for order in self:
            for line in order.order_line:
                if line.product_id and (line.price_unit < line.product_id.minimum_price):
                    warning = {
                        'title': _("Warning for %s") % line.product_id.name,
                        'message': _(
                            "Le prix est inférieur au prix minimum du produit! Revérifiez s'il vous plait %s") % line.product_id.name,

                    }
                    # line.price_unit = line.product_id.minimum_price  # Optionally, you can set it to the minimum price
        return {'warning': warning} if warning else {}

    def check_min_pricefor_confirm(self):
        for order in self:
            for line in order.order_line:
                if line.product_id and (line.price_unit < line.product_id.minimum_price):
                    raise UserError(
                        _("Le prix est inférieur au prix minimum du produit! Revérifiez s'il vous plait %s") % (
                            line.product_id.name))
        return True

    def action_confirm(self):
        self.check_min_pricefor_confirm()

        return super(SaleOrder, self).action_confirm()





