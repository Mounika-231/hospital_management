from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'

    name = fields.Char(
        string='Appointment No',
        required=True,
        copy=False,
        readonly=True,
        default='New'
    )

    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient',
        required=True
    )

    doctor_id = fields.Many2one(
        'hospital.doctor',
        string='Doctor',
        required=True
    )

    appointment_date = fields.Datetime(
        string='Appointment Date',
        required=True
    )

    notes = fields.Text(
        string='Symptoms / Notes'
    )

    token_number = fields.Char(
        string='Token Number'
    )

    # AUTO SEQUENCE NUMBER
    @api.model
    def create(self, vals):

        if vals.get('name', 'New') == 'New':

            vals['name'] = self.env['ir.sequence'].next_by_code(
                'hospital.appointment'
            ) or 'New'

        return super(HospitalAppointment, self).create(vals)

    # BASIC VALIDATION
    @api.constrains('appointment_date')
    def _check_appointment_date(self):

        for record in self:

            if (
                record.appointment_date and
                record.appointment_date < fields.Datetime.now()
            ):

                raise ValidationError(
                    "Appointment date cannot be in the past."
                )

    @api.constrains('token_number')
    def _check_token_number(self):

        for record in self:

            if record.token_number:

                existing_token = self.search([
                    ('token_number', '=', record.token_number),
                    ('id', '!=', record.id)
                ])

                if existing_token:
                    raise ValidationError(
                        "Token Number must be unique."
                    )

    # EMAIL REMINDER
    def send_appointment_reminder(self):

        appointments = self.search([])

        template = self.env.ref(
            'hospital_management.email_template_appointment_reminder'
        )

        for appointment in appointments:

            if appointment.patient_id.email:

                template.send_mail(
                    appointment.id,
                    force_send=True
                )