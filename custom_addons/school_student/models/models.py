# -*- coding: utf-8 -*-

from odoo import fields, models, _, api


class school_student(models.Model):
    _name = 'school.student'

    name = fields.Char()
    school_id = fields.Many2one("school.profile", string="School Name")
    hobby_list = fields.Many2many("hobby", "school_hobby_rel", "student_id", "hobby_id", string="Hobbies", required=True)

    is_virtual_school = fields.Boolean(related="school_id.is_virtual_class", string="Is Virtual School", store=True)
    school_address = fields.Text(related="school_id.address", string="School Address")
    currency_id = fields.Many2one("res.currency", string="Currency")
    student_fees = fields.Monetary(string="Student Fees", index=True)
    total_fees = fields.Float(string="Total Fees")
    ref_id = fields.Reference(selection=[('school.profile', 'School'),
                                         ('account.move', 'Invoice')], string="Reference",
                              default="account.move,1")
    active = fields.Boolean("Active", default=True)

    @api.model_create_multi
    def create(self, values):
        rtn = super(school_student, self).create(values)
        return rtn

    def write(self, values):
        values['active'] = True
        rtn = super(school_student, self).write(values)
        return rtn


class SchoolProfile(models.Model):
    _inherit = "school.profile"

    school_list = fields.One2many("school.student", "school_id", string="School List")


class Hobbies(models.Model):
    _name = "hobby"

    name = fields.Char("Hobby")
