from odoo import fields, models

class EducationClass(models.Model):
    _name = 'education.class'
    # kế thừa để dùng trường active
    # _inherit = 'base.education'

    _description = 'Education Class'
    name = fields.Char(string='Name', required=True)
    school_id = fields.Many2one('education.school', string='School', required=True)
    teacher_ids = fields.Many2many('res.partner', string='Teachers')
    # cách lấy recordset cho model student từ model class
    student_ids = fields.One2many('education.student', 'class_id', string='Students')

    # cách lấy recordset cho model student từ model class
    def get_all_students(self):
        # Khởi tạo đối tượng education.student (đây là 1 recordset rỗng của model education.student)
        student = self.env['education.student']
        all_students = student.search([])
        print('All Students: ', all_students)

    # tạo mới các bản ghi
    def create_classes(self):
        # giá trị để tạo bản ghi student 01
        student_01 = {
            'name': 'Student 01',
        }
        # giá trị để tạo bản ghi student 02
        student_02 = {
            'name': 'Student 02',
        }
        # giá trị để tạo bản ghi lớp học
        class_value = {
            'student_ids': [
                (0, 0, student_01),
                (0, 0, student_02)
            ]
        }
        record = self.env['education.class'].create(class_value)

    # cập nhật giá trị bản ghi
    def change_class_name(self):
        # kiểm tra self có đúng 1 bản ghi hay không, nếu muốn thay đổi hết thì bỏ self.ensure_one()
        self.ensure_one()
        # cách 1: gán trực tiếp giác trị cho thuộc tính
        self.name = 'Class 12A1'
        # cách 2: sử dụng hàm write với tham số là 1 dict
        # self.write({
        #     'name': 'Class 12A1'
        # })

    def add_student(self):
        self.ensure_one()
        self.write({
            'student_ids': [(0, 0, {
                'name': 'Student'
            })]
        })