from odoo import models, fields


class PatientProblem(models.Model):
    _name = 'hospital.patient.problem'
    _description = 'Patient Problem'


    # ================= PATIENT DETAILS =================

    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient',
        ondelete='cascade',
        required=True
    )

    problem_name = fields.Char(
        string='Problem',
        required=True
    )

    start_date = fields.Date(
        string='Start Date'
    )


    # ================= CLAIMS / NOTES =================

    claim_notes = fields.Text(
        string='Claims Notes'
    )


    # ================= BANK DETAILS =================

    bank_name = fields.Char(
        string='Bank Name'
    )

    account_number = fields.Char(
        string='Account Number'
    )

    ifsc_code = fields.Char(
        string='IFSC Code'
    )


    # ================= SIGNATURE =================

    doctor_sign = fields.Binary(
        string='Doctor Signature',
        attachment=True
    )