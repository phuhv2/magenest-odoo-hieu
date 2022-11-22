from odoo import fields, models, api, _
from odoo.exceptions import ValidationError, UserError

class EducationStudent(models.Model):
    _name = 'education.student'
    _description = 'Education Student'
    # ràng buộc
    _sql_constraints = [
        ('student_code_unique', 'unique(student_code)', "The student code must be unique!"),
        ('check_total_score', 'CHECK(total_score >= 0)', "The Total Score must be greater than 0!")
    ]

    name = fields.Char(string='Student Name', required=True, translate=True)
    student_code = fields.Char(string='Student Code', required=True, index=True, help="Student ID is unique")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender', default='male')
    date_of_birth = fields.Date(string='Date of Birth')
    # trường tính toán compute
    age = fields.Integer(string='Age', compute='_compute_age', inverse='_inverse_age', search='_search_age', store=False, compute_sudo=True)
    active = fields.Boolean(string='Active', default=True)
    notes = fields.Text(string='Internal Notes')
    description = fields.Html(string='Description', sanitize=True, strip_style=False)
    attached_file = fields.Binary('Attached File', groups='base.group_user')
    total_score = fields.Float(string='Total Score')
    write_date = fields.Datetime(string='Last Updated on')
    total_score = fields.Float(string='Total Score', digits='Score')
    currency_id = fields.Many2one('res.currency', string='Currency')
    amount_paid = fields.Monetary('Amount Paid')
    # hiển thị các trường Related code, address từ model school, đảm bảo có trường Many2one đến school
    school_id = fields.Many2one('education.school', string='School')
    school_code = fields.Char(related='school_id.code', string='School Code')
    school_address = fields.Char(related='school_id.address', string='School Address')
    # đĩnh nghĩa phương thức để thay đổi trạng thái của học sinh được chọn
    state = fields.Selection(string='Status', selection=[
        ('new', 'New'),
        ('studying', 'Studying'),
        ('off', 'Off')
    ], default='new')
    # cách lấy recordset cho model student từ model class
    class_id = fields.Many2one('education.class', string='Class', ondelete='restrict')

    # ràng buộc phức tạp
    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for r in self:
            if r.date_of_birth > fields.Date.today():
                raise ValidationError('Date of Birth must be in the past')

    # hàm tính toán compute tính toán động trong thời gian chạy, nó cần biết các trường khác mà nó phụ thuộc vào để tính toán
    # @depends để phát hiện khi nào các giá trị được lưu trong bộ nhớ đệm được tính toán lại
    @api.depends('date_of_birth')
    def _compute_age(self):
        curent_year = fields.Date.today().year
        for r in self:
            if r.date_of_birth:
                r.age = curent_year - r.date_of_birth.year
            else:
                r.age = 0

    # hàm nghịch đảo inverse, sử dụng gán giá trị cho trường được tính toán để cập nhật là trường gốc
    def _inverse_age(self):
        for r in self:
            if r.age and r.date_of_birth:
                curent_year = fields.Date.today().year
                dob_year = curent_year - r.age
                dob_month = r.date_of_birth.month
                dob_day = r.date_of_birth.day
                date_of_birth = date(dob_year, dob_month, dob_day)
                r.date_of_birth = date_of_birth

    # tìm kiếm các bản ghi theo trường age
    def _search_age(self, operator, value):
        new_year = fields.Date.today().year - value
        new_value = date(1, 1, new_year)
        # age > value => date_of_birth < new_value
        operator_map = {'>': '<', '>=': '<=', '<': '>', '<=': '>='}
        new_operator = operator_map.get(operator, operator)
        return [('date_of_birth', new_operator, new_value)]

    # tạo helper method để kiểm tra xem đầu vào trạng thái có hợp lệ hay không, ở ví dụ này ta không muốn thay đổi trạng
    # thái từ student từ off sang new, nên không có điều kiện ('off', 'new') vào hàm.
    # Khi dùng @api.model trên một method, thì self ở đây chỉ liên quan đến model và không còn liên quan đến tập bản ghi
    # tương ứng trên database
    @api.model
    def is_allowed_state(self, current_state, new_state):
        allowed_states = [('new', 'studying'), ('studying', 'off'), ('off', 'studying'), ('new', 'off')]
        return (current_state, new_state) in allowed_states

    # tạo method cho phép thay đổi state mới
    # Khi hàm được gọi nó sẽ thay đổi trạng thái của student với tham số state đẫ cho nếu trạng thái hợp lệ.
    def change_student_state(self, state):
        for student in self:
            if student.is_allowed_state(student.state, state):
                student.state = state
            else:
                raise UserError(_(f"Changing student status from {student.state} to {state} is not allowed."))

    # tạo các method để thay đổi sang một trạng thái mới tương ứng
    def change_to_new(self):
        self.change_student_state('new')

    def change_to_studying(self):
        self.change_student_state('studying')

    def change_to_off(self):
        self.change_student_state('off')


