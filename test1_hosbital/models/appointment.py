from odoo import api, fields, models


class HosbitalAppointment(models.Model):
    _name = "hosbital.appointment"
    _description = "hosbital Appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # ديه عشان يظهر اسم المريض فوق جمب اسم الصفحه (appointment /  او رقمه او اي حاجه عايزها تتعرض name of patient )
    _rec_name = 'patient_id'

    patient_id = fields.Many2one(comodel_name='hosbital.patient', string="patient")
    gender = fields.Selection(related='patient_id.gender')
    active = fields.Boolean(string="Active", default=True, tracking=True)
    # عشان اعمل زرار ارشيف وليها تابع في ال فيو
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    ref = fields.Char(string="reference", help="Reference of The Patient From Patient Record")
    # help = "الرساله اللي هتظهر لو وقفت علي الفيلد ده "
    # عشان اعرف او اضيف html field
    prescription = fields.Html(string="Prescription")
    # ديه عشان اعمل اولويه -- وهنا كل لفل من اول 1 بيدل علي نجمه مثلا وهعرفه في ال view
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")
    # هنا عملنا سيلكشن فيلد عشان نعمل منه شريط الحاله
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        #    defualt=draft ديه عشان اخلي الافتراضي بتاعها علي draft ---- required=true عشان اخليها تتطبق علي الكل
        ('cancel', 'Cancel')], string="Status", default='draft', required=True)

    # عملنا فيلد اسمها دكتور مني تو وان ... res.users عشان تاخد من اليوزرز
    doctor_id = fields.Many2one('res.users', string='Doctor')

    # طريقه تانيه عشان اعمل relate بس بالكود علي طول  شبه ال gender
    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    #     كود عشان نجرب ننفذ ال زرار من نوع object
    def action_test(self):
        print("Button Clicked !!!!!!")

        #  الكود ده عشان يعمل افيكت لما ادوس علي الزرار
        return {
            'effect': {
                'fadeout': 'slow',
                #  عشان الافكت يختفي لوحده بعد مده
                'message': 'Click Successfuall',
                #  الرساله اللي هتظهر
                'type': 'rainbow_man',
                #  الشكل اللي هيظهر
            }
        }
