from odoo import models, fields, api

class SPurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    hr_department_id = fields.Many2one('hr.department', string='Department', required=True)

    # @api.depends('product_id')
    # def _compute_supplier(self):
    #     for rec in self:
    #         results = self.env['product.supplierinfo'].search([], order='price asc', limit=1)
    #         result = results.mapped('partner_id')
    #         for i in result:
    #             rec.supplier = i.id
