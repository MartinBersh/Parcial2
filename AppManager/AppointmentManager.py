class AppointmentManager:
    def __init__(self):
        self.appointments = []

    def book_appointment(self, patient_name, doctor_name, appointment_date):
        appointment = {
            'id': len(self.appointments) + 1,
            'patient_name': patient_name,
            'doctor_name': doctor_name,
            'appointment_date': appointment_date,
            'status': 'scheduled'
        }
        self.appointments.append(appointment)
        return appointment

    def cancel_appointment(self, appointment_id):
        for appointment in self.appointments:
            if appointment['id'] == appointment_id:
                appointment['status'] = 'cancelled'
                return appointment
        return None

    def rebook_appointment(self, appointment_id, new_date):
        for appointment in self.appointments:
            if appointment['id'] == appointment_id:
                appointment['appointment_date'] = new_date
                return appointment
        return None

    def list_appointments(self, user_name):
        return [appointment for appointment in self.appointments if
                appointment['patient_name'] == user_name or appointment['doctor_name'] == user_name]

