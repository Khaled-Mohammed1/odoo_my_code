from odoo import api, fields, models


class CancelAppointmentWizard(models.TransientModel):
    # مديول مش بيخزن داتا في الداتا بيز

    # _name="الاسم التقني الخاص بالمديول"
    _name = "cancel.appointment.wizard"
    # _description="الاسم اللي هيظهر او الوصف "
    _description = "Cancel Appointment Wizard"

    # many2one فيلد
    appointment_id = fields.Many2one('hosbital.appointment', string="Appointment Wizard")
    # فيلد من نوع text
    reason = fields.Text(string="Reason")

    # الزرار اللي عاملينه في الفيو في الفوتر
    def action_cancel(self):
        return
#     هنا معرفينه مبيعملش حاجه
