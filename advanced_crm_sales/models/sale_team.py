from odoo import models, fields

class MonthlySales(models.Model):
    _inherit = "crm.team"
    _sql_constraints = [
        ("check_january_sales", "CHECK(january_sales > 0)", "The expected price must be strictly positive"),
        ("check_february_sales", "CHECK(february_sales > 0)", "The expected price must be strictly positive"),
        ("check_march_sales", "CHECK(march_sales > 0)", "The expected price must be strictly positive"),
        ("check_april_sales", "CHECK(april_sales > 0)", "The expected price must be strictly positive"),
        ("check_may_sales", "CHECK(may_sales > 0)", "The expected price must be strictly positive"),
        ("check_june_sales", "CHECK(june_sales > 0)", "The expected price must be strictly positive"),
        ("check_july_sales", "CHECK(july_sales > 0)", "The expected price must be strictly positive"),
        ("check_august_sales", "CHECK(august_sales > 0)", "The expected price must be strictly positive"),
        ("check_september_sales", "CHECK(september_sales > 0)", "The expected price must be strictly positive"),
        ("check_october_sales", "CHECK(october_sales > 0)", "The expected price must be strictly positive"),
        ("check_november_sales", "CHECK(november_sales > 0)", "The expected price must be strictly positive"),
        ("check_december_sales", "CHECK(december_sales > 0)", "The expected price must be strictly positive"),
    ]

    january_sales = fields.Float("January Sales", digits=(12, 3))
    february_sales = fields.Float("February Sales", digits=(12, 3))
    march_sales = fields.Float("March Sales", digits=(12, 3))
    april_sales = fields.Float("April Sales", digits=(12, 3))
    may_sales = fields.Float("May Sales", digits=(12, 3))
    june_sales= fields.Float("June Sales", digits=(12, 3))
    july_sales = fields.Float("July Sales", digits=(12, 3))
    august_sales = fields.Float("August Sales", digits=(12, 3))
    september_sales = fields.Float("September Sales", digits=(12, 3))
    october_sales = fields.Float("October Sales", digits=(12, 3))
    november_sales = fields.Float("November Sales", digits=(12, 3))
    december_sales = fields.Float("December Sales", digits=(12, 3))

