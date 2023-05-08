from odoo import api, fields, models
import datetime


class CancelAppointmentWizard(models.TransientModel):
    # مديول مش بيخزن داتا في الداتا بيز

    # _name="الاسم التقني الخاص بالمديول"
    _name = "cancel.appointment.wizard"
    # _description="الاسم اللي هيظهر او الوصف "
    _description = "Cancel Appointment Wizard"

    # هنا بعمل انهارت اوفر رايت علي defualt get عشان اخلي الوقت يتاخد تلقائي
    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        res['date_cancel'] = datetime.date.today()
        return res

    # many2one فيلد
    appointment_id = fields.Many2one('hosbital.appointment', string="Appointment Wizard")
    # فيلد من نوع text
    reason = fields.Text(string="Reason")
    # فيلد من نوع داتا
    date_cancel = fields.Date(string="Cancellation Date")

    # الزرار اللي عاملينه في الفيو في الفوتر
    def action_cancel_wiz(self):
        return
#     هنا معرفينه مبيعملش حاجه
