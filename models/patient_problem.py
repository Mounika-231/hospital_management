from odoo import models, fields


class PatientProblem(models.Model):
    _name = 'hospital.patient.problem'
    _description = 'Patient Problem'

    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient',
        ondelete='cascade'
    )

    problem_name = fields.Char(
        string='Problem'
    )

    start_date = fields.Date(
        string='Start Date'
    )