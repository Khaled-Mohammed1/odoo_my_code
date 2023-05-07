from odoo import api, fields, models


class PatientTags(models.Model):
    # _name="الاسم التقني الخاص بالمديول"
    _name = "patient.tags"

    # _description="الاسم اللي هيظهر او الوصف "
    _description = "Patient Tags"

    name = fields.Char(string="Name", required=True)
    # required=True ان الخانه ديه اجباري

    active = fields.Boolean(string="Active", default=True)
    # defualt=True الافتراضي الخاص بها

    # فيليد هياخد ارقام يحولها لالوان بالويدجيت في ال فيو
    color = fields.Integer(string="Color")

    # طريقه تانيه لتحويل من char الي الوان بيبقا فيها اختيارات للالوان اكتر وبرده بستخدام الويدجيت في الفيو
    color_char = fields.Char(string="Color as char")
