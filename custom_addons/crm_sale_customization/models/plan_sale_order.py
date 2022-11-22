from odoo import models, fields, api


class PlanSaleOrder(models.Model):
    _name = "plan.sale.order"
    _inherit = ['mail.thread']
    _description = "Plan Sale Order"

    name = fields.Text(string="Plan Name", required=True)
    quotation = fields.Many2one("sale.order", string="Quotation", readonly=True)
    description = fields.Text(string="Description", required=True)
    res_partner_id = fields.Many2many("res.partner", "plan_sale_order_res_partner_rel", "plan_sale_order_id",
                                      "res_partner_id", string="Partner List")
    state = fields.Selection(string="Status", selection=[
        ('draft', 'Draft'), ('confirm', 'Confirm'), ('validate', 'Validate'),
        ('refuse', 'Refuse'), ('approved', 'Approved'),
    ], default='draft', track_visibility='onchange')

    def confirm_request(self):
        self.state = 'confirm'

    def validate_request(self):
        self.state = 'validate'

    def refuse_request(self):
        self.state = 'refuse'

    def approve_request(self):
        self.state = 'approved'

