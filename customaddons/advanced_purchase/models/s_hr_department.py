from odoo import models, fields

class SHrDepartment(models.Model):
    _inherit = 'hr.department'
    _sql_constraints = [
        ("check_spending_limit", "CHECK(spending_limit > 0)", "The expected price must be strictly positive")
    ]

    spending_limit = fields.Float('Spending Limit/Month', digits=(12,3))
