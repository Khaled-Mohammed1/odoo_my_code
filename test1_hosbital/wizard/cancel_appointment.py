from odoo import api, fields, models, _
import datetime
from odoo.exceptions import ValidationError


class CancelAppointmentWizard(models.TransientModel):
    # مديول مش بيخزن داتا في الداتا بيز

    # _name="الاسم التقني الخاص بالمديول"
    _name = "cancel.appointment.wizard"
    # _description="الاسم اللي هيظهر او الوصف "
    _description = "Cancel Appointment Wizard"

    # هنا بعمل انهارت اوفر رايت علي defualt get عشان اخلي الوقت يتاخد تلقائي
    # يعني من الاخر لو انا عامل default لحاجه هنا بعمل اوفرايت عليها وبغيرها
    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        res['date_cancel'] = datetime.date.today()
        # هنعمل الطريقه التانيه عشان ياخد الاى دي بتاع الكشف اللي واقفين فيه ويحطه في الخانه تلقائي
        if self.env.context.get('active_id'):
            res['appointment_id'] = self.env.context.get('active_id')
        return res

    # many2one فيلد
    appointment_id = fields.Many2one('hosbital.appointment', string="Appointment Wizard",
                                     domain=[('state', '=', 'draft'), ('priority', 'in', (False, '0', '1'))])
    # domain ده عشان احدد نقدر نلغي في انهي حاله وممكن نفس النص ده يتكتب في ال اكس ام ال
    # بنعمل بيه فيلتر يعني

    # -------------------------------------------------

    # فيلد من نوع text
    reason = fields.Text(string="Reason")
    # فيلد من نوع داتا
    date_cancel = fields.Date(string="Cancellation Date")

    # الزرار اللي عاملينه في الفيو في الفوتر
    def action_cancel_wiz(self):
        if self.appointment_id.booking_date == fields.Date.today():
            raise ValidationError(_("Sorry, Cancellation Is Not Allowed On The Same Day Of Booking day !"))
        #  ديه عشان اخلي مينفعش نلغي الحجز اللي لسه محجوز في نفس البوم
        self.appointment_id.state = 'cancel'
        return
#     هنا معرفينه مبيعملش حاجه
