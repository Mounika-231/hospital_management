from odoo import models, fields


class PatientReportWizard(models.TransientModel):
    _name = 'patient.report.wizard'
    _description = 'Patient Report Wizard'

    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient'
    )

    report_file = fields.Binary(
        string='Upload PDF'
    )

    file_name = fields.Char(
        string='File Name'
    )

    def action_submit_report(self):

        self.env['ir.attachment'].create({
            'name': self.file_name,
            'type': 'binary',
            'datas': self.report_file,
            'res_model': 'hospital.patient',
            'res_id': self.patient_id.id,
            'mimetype': 'application/pdf',
        })