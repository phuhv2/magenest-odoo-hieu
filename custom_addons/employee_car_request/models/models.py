# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CarRequest(models.Model):
    _name = "car.request"
    _inherit = ['mail.thread']
    _description = "Car Request"

    name = fields.Char(string="Request", required=True)
    date_from = fields.Datetime(string="Starting Date", default=fields.Datetime.now())
    date_to = fields.Datetime(string="End Date", required=False)
    employee_id = fields.Many2one("hr.employee", string="Employee", required=True)
    car_id = fields.Many2one("fleet.vehicle", string="Car", required=True)
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
