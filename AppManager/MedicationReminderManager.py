class MedicationReminderManager:
    def __init__(self):
        self.medication_reminders = []

    def add_medication_reminder(self, patient_name, medication_name, reminder_time):
        reminder = {
            'id': len(self.medication_reminders) + 1,
            'patient_name': patient_name,
            'medication_name': medication_name,
            'reminder_time': reminder_time,
            'status': 'pending'
        }
        self.medication_reminders.append(reminder)
        return reminder

    def get_reminders(self, patient_name):
        return [reminder for reminder in self.medication_reminders if reminder['patient_name'] == patient_name]
