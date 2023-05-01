from odoo import api, fields, models
from datetime import date


class HosbitalPatient(models.Model):
    _name = "hosbital.patient"
    _description = "hosbital Patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True)
    ref = fields.Char(string="reference", tracking=True)
    date_of_birth = fields.Date(string="Date Of Birth")
    age = fields.Integer(string="Age", compute='_compute_age', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string=' Gender', tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)
    # عشان نعمل فيلد نعرض فيه صوره المريض
    image = fields.Image(string="Image")
    # همعمل فيلد many2many
    # tag_ids = fields.Many2many('co model الموديل الي هاخد منه العلاقه', 'DB table Name اسم التيبول ديه في الداتا بيز',
    # 'First t name اسم اول كولم في العلاقه ' ,'second t name اسم الكولم التاني في العلاقه ' string='Tags')
    tag_ids = fields.Many2many('patient.tags', 'many2may_tags', 'pi', 'ti', string='Tags')

    # عشان اخلي السن يتحسب اوتوماتك من تاريخ الميلاد
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            # الكود ده عشان اخد تاريخ النهارده
            today = date.today()
            if rec.date_of_birth:
                # الفانكشن اللي هتتنفذ .... السنه الحاليه - يوم الميلاد بس بالسنه
                rec.age = today.year - rec.date_of_birth.year

            # هنا هنعمل else عشان ميظهر ال error عشان لو مخترناش تاريخ الميلاد
            else:
                rec.age = 0
