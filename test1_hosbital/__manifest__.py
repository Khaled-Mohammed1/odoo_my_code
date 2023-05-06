# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hospital mangmit',
    'version': '15.0',
    'category': 'mangmint',
    'summary': 'first test of odddo ',
    # ده وصف المشروع
    'description': """ first test description """,
    # هنا بنقول ان المشروع ملك K_MATRIX
    'author': 'K_Matrix',
    # هنا بنقول ان المشروع معتمد علي مديول ال mail وال  product
    'depends': ['mail', 'product'],
    'data': [
        # الترتيب مهم لازم يبقا بالشكل ده
        'security/ir.model.access.csv',
        'data/patient_tags_data.xml',
        'data/patient.tags.csv',
        'data/sequence_data.xml',
        'wizard/cancel_appointment_view.xml',
        'views/menu.xml',
        'views/patient_tags.xml',
        'views/patient.xml',
        'views/female_patient.xml',
        'views/male_patient.xml',
        'views/kids_patient.xml',
        'views/appointment_view.xml',
    ],
    'demo': [],
    'sequence': '-100',
    'application': True,
    'installable': True,
    'auto_install': False,
    'assets': {},

}
