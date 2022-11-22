from odoo import fields, models, api


class SchoolProfile(models.Model):
    _name = "school.profile"

    name = fields.Char(string="School Name", copy=False)
    email = fields.Char(string="Email")
    phone = fields.Char("Phone")
    is_virtual_class = fields.Boolean(string="Virtual Class Support ?")
    school_rank = fields.Integer(string="Rank")
    result = fields.Float(string="Result")
    address = fields.Text(string="Address")
    establish_date = fields.Date(string="Establish Date", default=fields.Date.today())
    open_date = fields.Datetime("Open Date", default=fields.Datetime.now())
    school_type = fields.Selection([
        ('public', 'Public School'),
        ('private', 'Private School')
    ], string="School Type", default='public')
    documents = fields.Binary("Document")
    document_name = fields.Char("File Name")
    school_image = fields.Image("Upload Image School", max_width=100, max_height=100, readonly=True)
    school_description = fields.Html(string="School Description")
    auto_rank = fields.Integer(compute="_auto_rank_populate", string="Auto Rank", store=True)

    @api.depends("school_type")
    def _auto_rank_populate(self):
        for rec in self:
            if rec.school_type == "public":
                rec.auto_rank = 100
            elif rec.school_type == "private":
                rec.auto_rank = 50
            else:
                rec.auto_rank = 0