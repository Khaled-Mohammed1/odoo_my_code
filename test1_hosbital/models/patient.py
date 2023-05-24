from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError


class HosbitalPatient(models.Model):
    _name = "hosbital.patient"
    _description = "hosbital Patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True)
    ref = fields.Char(string="reference", tracking=True)
    date_of_birth = fields.Date(string="Date Of Birth")
    age = fields.Integer(string="Age", compute='_compute_age', tracking=True, store=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string=' Gender', tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)
    number = fields.Char(string="Mobile Number", size=11)
    # عشان نعمل فيلد نعرض فيه صوره المريض
    image = fields.Image(string="Image")
    # همعمل فيلد many2many
    # tag_ids = fields.Many2many('co model الموديل الي هاخد منه العلاقه', 'DB table Name اسم التيبول ديه في الداتا بيز',
    # 'First t name اسم اول كولم في العلاقه ' ,'second t name اسم الكولم التاني في العلاقه ' string='Tags')
    tag_ids = fields.Many2many('patient.tags', 'many2may_tags', 'pi', 'ti', string='Tags')

    # __________________________________________________________________________________________________________________

    # ده عشان اخلي مينفعش ادخل تاريخ ميلاد بعد تاريخ اليوم
    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError(_("The Entered Date Of Birth Is Not Acceptable"))

    # __________________________________________________________________________________________________________________

    # method overwrite
    # عشان اعمل اوفررايت علي الميثود اللي موجوده يبقا بالشكل ده
    # @api.model ده الديكوريشن لازم اكتبه
    @api.model
    def create(self, vals):
        # هنا بنعدل علي ميثود الانشاء
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient.ref.id')
        # vals['الفيلد اللي هنعدل عليها '] = 'التعديل '
        # vals['ref'] = self.env['ir.sequence'].next_by_code('الاسم التقني لملف التسلسل في الاكس ام ال ')
        # ----------------------------------------------------------------
        # return super(اسم الكلاس مديول,self).create(اللي موجود في القوس فوق بعد سيلف)
        # الامر ده مهم عشان ينفذ الميثود الاساسيه بعد التعديل
        return super(HosbitalPatient, self).create(vals)

    # __________________________________________________________________________________________________________________

    # method overwrite
    # ده عشان نعدل علي التعديل ان في حاله ان ال رقم التسلسلي فاضي ضيف تسلسل
    def write(self, vals):
        # and not vals.get('ref') ديه بقوله لو المريض واخد اي مدخل غير التسلسل اللي عاملينه سيبه متغيروش
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient.ref.id')
            # vals['الفيلد اللي هنعدل عليها '] = 'التعديل '
            # vals['ref'] = self.env['ir.sequence'].next_by_code('الاسم التقني لملف التسلسل في الاكس ام ال ')
            # ----------------------------------------------------------------
            # return super(اسم الكلاس مديول,self).create(اللي موجود في القوس فوق بعد سيلف)
            # الامر ده مهم عشان ينفذ الميثود الاساسيه بعد التعديل
        return super(HosbitalPatient, self).write(vals)

    # __________________________________________________________________________________________________________________

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

    # __________________________________________________________________________________________________________________

    # ده عشان الاسم اللي هيظهر في ال appointment يبقا رقم المريض واسمه
    def name_get(self):
        return [(record.id, "[%s] %s" % (record.ref, record.name)) for record in self]
        # return [(record.id, "[اول واحده اللي هيه ال ref] record.name" % (record.ref, record.name)) for record in self]
        # عملت table  بتحتوي علي الرقم والاسم

    # __________________________________________________________________________________________________________________

    # ديه عشان اخلي الرقم الموبيال مينفعش يتكرر في السيستم
    _sql_constraints = [
        ('number_uniq', 'unique (number)', "Mobile Number Already Exists !"),
    ]

    # __________________________________________________________________________________________________________________
