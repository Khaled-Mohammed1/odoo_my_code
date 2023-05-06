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
    # ملحوظه ال many2one لازم ينتهي ب id
    # ال one2many لازم ينتهي ب ids

    # هعرف هنا الموديول الي one2many
    # pharmacy_line_ids = fields.One2many('العلاقه بين المودل', 'اسم الموديل اللي هشوفه هنا ', string="اسمه")
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string="Pharmacy Lines")

    # ده عشان نعمل زرار وهمي عشان يعمل شرط معين عشان يخفي او يظهر سعر المنتجات
    # هنضيفه جوا الموديل الرئيسي
    hide_sales_price = fields.Boolean(string="Hide Sales Price")

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

    # في حاله الضغط علي زر action_in_consultation هتغير الحاله الي in_consultation
    # ده الفانكشن اللي هيتنفذ لما ندوس علي الزراير اللي عملناها في ال هيدر في الفيو
    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'
        # rec.state ديه عشان تعدل علي ال حاله

    # في حاله الضغط علي زر action_in_consultation هتغير الحاله الي done
    def action_done(self):
        for rec in self:
            rec.state = 'done'
            # rec.state ديه عشان تعدل علي ال حاله

    # الطريقه التانيه اللي تخليني بالضغط علي الزر اروح لصفحه Cancel appointment wizard
    def action_cancel(self):
        action = self.env.ref('test1_hosbital.action_cancel_appointment_view').read()[0]
        return action
        # self.env.ref('مكان الاكشن اللي هيتعرض اللي هوا الصفحه') .read()[0] ده عشان تتعرض من غيرها مش هتظهر

        # الفانكشن القديم اللي شيلناه
        # في حاله الضغط علي زر action_in_consultation هتغير الحاله الي cancel
        # for rec in self:
        #     rec.state = 'cancel'
        # rec.state ديه عشان تعدل علي ال حاله

    # في حاله الضغط علي زر action_in_consultation هتغير الحاله الي draft
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
            # rec.state ديه عشان تعدل علي ال حاله


# هعمل موديل جديد زي ال appointment وال patient بس في نفس الصفحه
# طبعا لازم اديله صلاحيات في ال securty
# ولازم اديله اسم ووصف
# و هعمله وهعرفه في الموديل الرئيسي فوق  one2many


class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "Appointment Pharmacy Lines"

    # وهعرف جواه فيلد many2one
    # ('product.product') ديه من مديول اسمه بروداكت وهنا لازمه اضيفه جوال ال manifest .. depends
    # required=True ديه عشان اخلي الخانه ديه اجباري تتملي
    product_id = fields.Many2one('product.product', required=True)
    # related='product_id.list_price' عشان اربط السعر باسم المنتج وديه جايبنا من مديول ال product
    price_unit = fields.Float(related='product_id.list_price')
    # default=1 ديه عشان اخلي القيمه الافتراضيه للعدد واحد
    qty = fields.Integer(string='Quantity', default=1)

    # هعمل هنا فيلد many2one عشان اعمل ريليشن بين الموديل ده والموديل الرئيسي
    appointment_id = fields.Many2one('hosbital.appointment', string="Appointment")
