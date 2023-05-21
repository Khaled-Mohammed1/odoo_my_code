from odoo import api, fields, models, _


class PatientTags(models.Model):
    # _name="الاسم التقني الخاص بالمديول"
    _name = "patient.tags"

    # _description="الاسم اللي هيظهر او الوصف "
    _description = "Patient Tags"

    name = fields.Char(string="Name", required=True)
    # required=True ان الخانه ديه اجباري

    active = fields.Boolean(string="Active", default=True, copy=False)
    # defualt=True الافتراضي الخاص بها
    # copy=False عشان لما اعمل دوبلكيت مينسخش نفس الحاله

    # فيليد هياخد ارقام يحولها لالوان بالويدجيت في ال فيو
    color = fields.Integer(string="Color")

    # طريقه تانيه لتحويل من char الي الوان بيبقا فيها اختيارات للالوان اكتر وبرده بستخدام الويدجيت في الفيو
    color_char = fields.Char(string="Color as char")

    sequence = fields.Integer(string="Sequence")

    # ____________________________________________________________

    # هنعدل علي ال  duplicate
    # عشان لما نعملها تاخد الاسم وجمبه كلمه كوبي وكمان تاخد رقم 10 في Sequence
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}

        if not default.get('name'):
            default['name'] = _("%s (copy)", self.name)

        default['sequence'] = 10
        return super(PatientTags, self).copy(default)

    # _______________________________________________________________

    # شرط ان الاسم ميتكررش والرقم ميبقاش بالسالب او صفر
    _sql_constraints = [
        ('unique_tag_name', 'unique (name)', 'The Name Is Already Exist !!!'),
        ('check_sequence', 'check (sequence > 0)', 'The Sequence Must Be Not Zero And Positive Number !!!'),
    ]
