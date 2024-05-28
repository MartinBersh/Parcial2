from AppManager.AppointmentManager import AppointmentManager
from AppManager.MedicationReminderManager import MedicationReminderManager
from AppManager.MessageManager import MessageManager


def main():
    appointment_manager = AppointmentManager()
    medication_reminder_manager = MedicationReminderManager()
    message_manager = MessageManager()

    while True:
        print("\nSistema de Gestión de Salud")
        print("1. Reservar Cita")
        print("2. Cancelar Cita")
        print("3. Reprogramar Cita")
        print("4. Ver Registro Médico")
        print("5. Agregar Recordatorio de Medicación")
        print("8. Ver Recordatorios de Medicación")
        print("9. Enviar Mensaje")
        print("10. Ver Mensajes")
        print("11. Salir")
        choice = input("Ingrese su opción: ")

        if choice == '1':
            patient_name = input("Ingrese el nombre del paciente: ")
            doctor_name = input("Ingrese el nombre del doctor: ")
            appointment_date = input("Ingrese la fecha de la cita (YYYY-MM-DD HH:MM:SS): ")
            appointment = appointment_manager.book_appointment(patient_name, doctor_name, appointment_date)
            print(f"Cita reservada: {appointment}")

        elif choice == '2':
            appointment_id = int(input("Ingrese el ID de la cita: "))
            appointment = appointment_manager.cancel_appointment(appointment_id)
            if appointment:
                print(f"Cita cancelada: {appointment}")
            else:
                print("Cita no encontrada.")

        elif choice == '3':
            appointment_id = int(input("Ingrese el ID de la cita: "))
            new_date = input("Ingrese la nueva fecha de la cita (YYYY-MM-DD HH:MM:SS): ")
            appointment = appointment_manager.rebook_appointment(appointment_id, new_date)
            if appointment:
                print(f"Cita reprogramada: {appointment}")
            else:
                print("Cita no encontrada.")

        elif choice == '4':
            patient_name = input("Ingrese el nombre del paciente: ")
            doctor_name = input("Ingrese el nombre del doctor: ")
            visit_date = input("Ingrese la fecha de la visita (YYYY-MM-DD HH:MM:SS): ")
            notes = input("Ingrese las notas: ")
            record = medical_record_manager.add_medical_record(patient_name, doctor_name, visit_date, notes)
            print(f"Registro médico agregado: {record}")


        elif choice == '5':

            user_name = input("Ingrese su nombre: ")
            appointments = appointment_manager.list_appointments(user_name)
            if appointments:
                print("Citas:")
                for appointment in appointments:
                    print(appointment)

        elif choice == '6':
            patient_name = input("Ingrese el nombre del paciente: ")
            medication_name = input("Ingrese el nombre de la medicación: ")
            reminder_time = input("Ingrese la hora del recordatorio (YYYY-MM-DD HH:MM:SS): ")
            reminder = medication_reminder_manager.add_medication_reminder(patient_name, medication_name, reminder_time)
            print(f"Recordatorio de medicación agregado: {reminder}")

        elif choice == '7':
            patient_name = input("Ingrese el nombre del paciente: ")
            reminders = medication_reminder_manager.get_reminders(patient_name)
            for reminder in reminders:
                print(reminder)


        elif choice == '8':

            sender = input("Ingrese su nombre (paciente o doctor): ")
            recipient = input("Ingrese el nombre del destinatario (paciente o doctor): ")
            message = input("Ingrese el mensaje: ")
            message_manager.send_message(sender, recipient, message)
            print("Mensaje enviado.")


        elif choice == '9':

            user = input("Ingrese su nombre (paciente o doctor): ")
            messages = message_manager.get_messages(user)

            if messages:
                print("Mensajes recibidos:")
                for message in messages:
                    print(f"De: {message['sender']} Para: {message['recipient']} - {message['message']}")
            else:
                print("No hay mensajes.")


        elif choice == '10':
            break


        else:
            print("Opción inválida")

if __name__ == "__main__":
 main()