from odoo import models, fields, api

class PlanSaleOrder(models.Model):
    _name = "plan.sale.order"
    _description = "Plan Sale Order"
    _inherit = ['mail.thread']

    name = fields.Text(string="Plan Name", required=True)
    quotation = fields.Many2one("sale.order", string="Quotation")
    information = fields.Text(string="Infomation", required=True)
    approver = fields.Many2one("res.partner", string="Approver")
    status = fields.Selection([
        ('confirm', 'Confirm'),
        ('unconfirmed', 'Unconfirmed'),
        ('refuse', 'Refuse'),
    ], string="Status", default='confirm')
    res_partner_id = fields.Many2many("res.partner", "plan_sale_order_res_partner_rel", "plan_sale_order_id", "res_partner_id", string="Approver List", store=True)

    # @api.multi
    # def action_accept(self):
    #     for rec in self.env["plan.sale.order"].search([]):
    #         partner_id_list = rec.res_partner_id
    #         self.message_post(body="your message", partner_ids=partner_id_list)






