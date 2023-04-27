from odoo import api, fields, models
from datetime import date


class HosbitalPatient(models.Model):
    _name = "hosbital.patient"
    _description = "hosbital Patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True)
    ref = fields.Char(string="reference", tracking=True)
    date_of_birth = fields.Date(string="Date Of Birth")
    age = fields.Integer(string="Age",compute='_compute_age', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string=' Gender', tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)

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


