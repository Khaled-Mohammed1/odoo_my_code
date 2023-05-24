from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "sales_order_inharting"

    confirmed_user_id = fields.Many2one('res.users', string="Confirmed User")
