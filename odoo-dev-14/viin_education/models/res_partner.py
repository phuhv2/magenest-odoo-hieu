from odoo import fields, models, api

class ResPartner(models.Model):
    # kế thừa Class (mở rộng), thêm các trường hoặc phương thức mới vào các model hiện có
    _inherit = 'res.partner'

    is_teacher = fields.Boolean(string='Is Teacher')

    def _get_all_teacher(self):
        return self.searcher([('is_teacher', '=', True)])