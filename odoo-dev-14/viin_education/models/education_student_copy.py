from odoo import fields, models

# kế thừa Prototype(nguyên mẫu) sử dụng cả _inherit và _name, tạo model mới sao chép từ model cha
# kế thừa Delegation(ủy thác) cho phép đa kế thừa, database lưu trữ khác bảng gốc, model mới có trường tham chiếu đến bảng gốc

class EducationStudentCopy(models.Model):
    _name = 'education.student.copy'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Education Student - Copy'

    partner_id = fields.Many2one('res.partner', string='Student', ondelete='restrict', required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age')