{
    'name': 'Hospital Management',
    'version': '1.0',
    'summary': 'Basic Hospital System',
    'license': 'LGPL-3',

    'depends': ['base', 'mail'],

    'data': [

        # ================= SECURITY =================
        'security/security.xml',
        'security/ir.model.access.csv',

        # ================= VIEWS =================
        'views/menu.xml',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/appointment_views.xml',
        'views/patient_problem_views.xml',

        # ================= REPORT TEMPLATES =================
        'reports/appointment_report.xml',
        'reports/patient_contract_template.xml',

        # ================= REPORT ACTIONS =================
        'reports/report_action.xml',

        # ================= DATA FILES =================
        'data/sequence.xml',
        'data/email_template.xml',
        'data/cron.xml',
    ],

    'application': True,
    'installable': True,
}