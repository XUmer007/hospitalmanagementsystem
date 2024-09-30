from functions import patient_list, doctor_list, medicalhistory_list, medicine_list,encounter_list,appointment_list,start_encounter,create_appointment


def login_system():
    print("Welcome to the Login System")
    
    while True:
        print("1. Patient Login")
        print("2. Doctor Login")
        print("3. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            email = input("Enter Patient Email: ")
            password = input("Enter Password: ")
            
            patient_found = None
            for patient in patient_list:
                if patient.email == email and patient.password == password:
                    patient_found = patient
                    break
            
            if patient_found:
                print(f"Welcome, {patient_found.name}!")
                patient_menu(patient_found)
            else:
                print("Invalid email or password. Please try again.")

        elif choice == "2":
            email = input("Enter Doctor Email: ")
            password = input("Enter Password: ")
            
            doctor_found = None
            for doctor in doctor_list:
                if doctor.email == email and doctor.password == password:
                    doctor_found = doctor
                    break
            
            if doctor_found:
                print(f"Welcome, Dr. {doctor_found.name}!")
                doctor_menu(doctor_found)
            else:
                print("Invalid email or password. Please try again.")

        elif choice == "3":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

def patient_menu(patient):
    while True:
        print(f"\nPatient Menu - {patient.name}")
        print("1. View Medical History")
        print("2. View Medicine")
        print("3. Book Appointment")
        print("4. Logout")
    
def doctor_menu(doctor):
    while True:
        print(f"\nDoctor Menu - Dr. {doctor.name}")
        print("1. Manage Appointments")
        print("2. Start Encounter")
        print("3. View Medical History")
        print("4. Logout")
