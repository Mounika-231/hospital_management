{
    'name': 'Hospital Management',
    'version': '1.0',
    'summary': 'Basic Hospital System',
    'license': 'LGPL-3',

    'depends': ['base', 'mail'],

    'data': [

        'security/security.xml',
        'security/ir.model.access.csv',

        'views/menu.xml',

        'views/patient_views.xml',
        'views/doctor_views.xml',

        'reports/report_action.xml',
        'reports/appointment_report.xml',
        'data/sequence.xml',
        'views/appointment_views.xml',

        'views/patient_report_wizard.xml',
        'data/email_template.xml',
        'data/cron.xml',

    ],

    'application': True,
    'installable': True,
}