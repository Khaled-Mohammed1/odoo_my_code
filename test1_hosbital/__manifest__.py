# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hospital mangmit',
    'version': '15.0',
    'category': 'mangmint',
    'summary': 'first test of odddo ',
    'description': """ first test descraption """,
    'author': 'K_Matrix',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient.xml',
        'views/female_patient.xml',
        'views/male_patient.xml',
        'views/kids_patient.xml',
        'views/appointment_view.xml'
    ],
    'demo': [],
    'sequence': '-100',
    'application': True,
    'installable': True,
    'auto_install': False,
    'assets': {},

}
