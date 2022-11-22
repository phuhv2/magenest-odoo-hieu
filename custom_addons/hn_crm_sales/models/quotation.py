from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    plan_sale_order = fields.Many2one("plan.sale.order", string="Plan Sale Order")

    def new_plan(self):
        return{
            'res_model': 'plan.sale.order',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': self.env.ref('hn_crm_sales.plan_sale_order_form_view').id
        }