from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    # CHATTER + ACTIVITIES
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string="Patient Name",
        required=True,
        tracking=True
    )

    age = fields.Integer(
        string="Age",
        tracking=True
    )

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ],
        string="Gender",
        tracking=True
    )

    phone = fields.Char(
        string="Phone",
        tracking=True
    )

    email = fields.Char(
        string="Email",
        tracking=True
    )

    problem_ids = fields.One2many(
        'hospital.patient.problem',
        'patient_id',
        string='Patient Problems'
    )

    attachment_ids = fields.One2many(
        'ir.attachment',
        'res_id',
        string='Reports',
        domain=[('res_model', '=', 'hospital.patient')]
    )

    appointment_count = fields.Integer(
        string="Appointments",
        compute="_compute_appointment_count"
    )

    def _compute_appointment_count(self):
        for record in self:
            record.appointment_count = self.env['hospital.appointment'].search_count([
                ('patient_id', '=', record.id)
            ])

    def action_view_appointments(self):
        return {
            'name': 'Appointments',
            'type': 'ir.actions.act_window',
            'res_model': 'hospital.appointment',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.id)],
            'target': 'current',
        }

    def action_open_report_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Upload Report',
            'res_model': 'patient.report.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_patient_id': self.id
            }
        }

    # BASIC VALIDATION
    @api.constrains('age')
    def _check_age(self):
        for record in self:
            if record.age and record.age < 0:
                raise ValidationError("Age cannot be negative.")

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email and '@' not in record.email:
                raise ValidationError("Please enter a valid email address.")