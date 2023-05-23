from odoo import http
from odoo.http import request


class Hospital(http.Controller):
    @http.route('/hospital/patient/', website=True, auth='user')
    def hosbital_patient(self, **kw):
        patients = request.env['hosbital.patient'].sudo().search([])
        return request.render("test1_hosbital.patients_page", {'patients': patients
                                                               })

    @http.route('/create_patient', type='json', auth='user')
    def create_patient(self, **rec):
        if request.jsonrequest:
            print("rec", rec)
            if rec['name']:
                vals = {
                    'name': rec['name']
                }
        new_patient = request.env['hosbital.patient'].sudo().create(vals)
        print("New Patient Is ", new_patient)
        args = {'success': True, 'message': 'Success created new patient', 'id': new_patient.id}
        return args

    @http.route('/get_patients', type='json', auth='user')
    def get_patients(self):
        print("yes here entered")
        patients_rec = request.env['hosbital.patient'].search([])
        patients = []
        for rec in patients_rec:
            vals = {
                'id': rec.id,
                'name': rec.name,
                'ref': rec.ref,
            }
            patients.append(vals)
        print("patient List ---->", patients)
        data = {'status': 200, 'response': patients, 'message': 'nice success'}
        return data
