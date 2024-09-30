from users import Patient, Doctor
from medicalhistory import MedicalHistory

patient_list = []

def store_patients():
    global patient_list
    
    def add_patient(patient):
        patient_list.append(patient)
        return patient_list
    
    return add_patient


def create_patient():
    global patient_list 
    
    store = store_patients()
    patient_ID = len(patient_list) + 1 
    name = input("Enter Patient Name: ")
    age = input("Enter Patient Age: ")
    gender = input("Enter Patient Gender: ")
    Disease_stage = input("Enter Disease Stage level: ")
    Blood_type = input("Enter your blood type (e.g., A+, A-): ")
    contact = input("Enter Patient Contact Info: ")
    email = input("Enter Patient Email: ")
    password = input("Enter Password: ")
    
    new_patient = {
        "ID": int(patient_ID),
        "Name": name,
        "Age": (age),
        "Gender": gender,
        "Disease Stage": Disease_stage,
        "Blood type": Blood_type,
        "Contact": contact,
        "Email": email,
        "Password": password
    }
    store(new_patient)
    
    
    for patient in patient_list:
        print(patient)
    save_data(patient_list, "txtfiles/patient.txt" ) 
    # fetch_data('txtfiles/patient.txt',patient_list)  
    # delete_data('txtfiles/patient.txt',patient_list)    
    
    


doctor_list = []

def store_doctor():
    global doctor_list

    def add_doctor(doctor):
        doctor_list.append(doctor)
        return doctor_list
    
    return add_doctor

def create_doctor():
    global doctor_list

    store4 = store_doctor()
    doctor_ID = len(doctor_list) + 1
    name = input("Enter Doctor Name: ")
    age = input("Enter Doctor Age: ")
    gender = input("Enter Doctor Gender: ")
    designation = input("Enter Designation: ")
    speciality = input("Enter Speciality: ")
    contact = input("Enter Doctor Contact Information: ")
    email = input("Enter Doctor Email: ")
    password = input("Enter Password: ")
    
    doctor_obj= {
        "ID": int(doctor_ID),
        "Name": name,
        "Age": age,
        "Gender": gender,
        "designation": designation,
        "speciality": speciality,
        "Contact": contact,
        "Email": email,
        "Password": password
    }
    store4(doctor_obj) 
    for doctor in doctor_list:
        print(doctor)  
    save_data(doctor_list, "txtfiles/doctor.txt")        
  
       

medicalhistory_list = []

def store_medicalhistory():
    global medicalhistory_list

    def add_medicalhistory(medicalhistory):
        medicalhistory_list.append(medicalhistory)
        return medicalhistory_list
    return add_medicalhistory

def medicalhistory_input():
    global medicalhistory_list
 
    store1 = store_medicalhistory()
    patient_ID = len(medicalhistory_list) + 1  
    patient = input("Enter Patient Name: ")
    condition = input("Enter Patient Condition: ")
    status = input("Enter Status: ")
    start_date = input("Enter Start Date: ")
    end_date = input("Enter End Date: ")
    allergies = input("Enter Allergies if any: ")
    from medicalhistory import MedicalHistory
    medicalhistory_obj= {
        "Patient_ID": int(patient_ID),
        "Name": patient ,
        "Condition": condition,
        "status": status,
        "Start Date": start_date,
        "End Date": end_date,
        "Allergies": allergies,
       
    }
    
    # medicalhistory_obj = MedicalHistory(patient_ID, patient, condition, status, start_date, end_date, allergies)
    store1(medicalhistory_obj)
    for medical in medicalhistory_list:
        print(medical)
    save_data(medicalhistory_list, "txtfiles/medicalhistory.txt")     

  



medicine_list = []

def store_medicine():
    global medicine_list

    def add_medicine(meds):
        medicine_list.append(meds)
        return medicine_list

    return add_medicine

def input_medicine():
    global medicine_list
    global patient_list
  
    store3 = store_medicine()
    patient_ID = len(patient_list) + 1
    medicine_ID = len(medicine_list) + 1
    patient = input("Enter Patient Name: ")
    med_name = input("Enter Medicine Name: ")
    side_effects = input("Enter Side Effects (if any): ")
    expiry_date = input("Enter Expiry Date (YY-MM-DD): ")
    
    from Meds import Medicine
    medicine_obj = {
    'ID': int(medicine_ID),
    'patient_ID': patient_ID,
    'patient': patient,
    'med_name': med_name,
    'side_effects': side_effects,
    'Expiry_date': expiry_date  
}

    # medicine_obj = Medicine(medicine_ID, patient_ID, patient, med_name, side_effects, expiry_date)
    store3(medicine_obj)
    for medicine in medicine_list:
        print(medicine)
    save_data(medicine_list,"txtfiles/medicine.txt")    
       
    
 
  


appointment_list = []

def store_appointments():
    global appointment_list

    def add_appointment(appointment):
        appointment_list.append(appointment)
        return appointment_list
    return add_appointment

def create_appointment():
    global appointment_list
    global patient_list
    global doctor_list
  
      
    store2 = store_appointments()

    appointment_id = len(appointment_list) + 1
    patient = input("Enter Patient Name: ")
    doctor = input("Enter Doctor Name: ")
    date = input("Enter Date: ")
    reason = input("Enter Reason for Appointment: ")
    status = input("Enter Status: ")

    patient_ID = len(patient_list) + 1
    doctor_ID = len(doctor_list) + 1

    from appointment import Appointment
    appointment_obj = {
    "Appointment_ID": appointment_id,
    "Patient_ID": patient_ID,
    "Patient": patient,
    "Doctor_ID": doctor_ID,
    "Doctor": doctor,
    "Date": date,
    "Reason": reason,
    "Status": status
}

    # appointment_obj = Appointment(
    #    patient_ID, doctor_ID, patient, doctor, appointment_id, date, reason, status)
    store2(appointment_obj)
    for appointment in appointment_list:
        print(appointment)
    save_data(appointment_list, "txtfiles/appointment.txt")      
    
    


encounter_list=[]


def menu():
    while True:
        print("MENU")
        print("Choice 1: Patient")
        print("Choice 2: Doctor")
        print("Choice 3: Medical History")
        print("Choice 4: Medicine")
        print("Choice 5: Appointment")
        print("Choice 6: Encounter")
        print("Choice 7: Exit")
        
        choice = input("Enter choice: ")

        if choice == "1":
            print("Patient Menu:")
            while True:
                print("Enter 1 to add patient")
                print("enter 2 to print all patients")
                print("Enter 3 to update Patient ID  ")
                print("Enter 4 to Delete Patient ID")
                print("'exit' to return to the main menu:")
                sub_choice = input("Enter Choice: ")
                
                if sub_choice == "1":
                    create_patient()
                
                elif sub_choice == "2":
                    print(patient_list[:])
                
                elif sub_choice == "3":
                    update_patient()
                
                elif sub_choice == "4":
                    delete_patient()    
                
                elif sub_choice.lower() == "exit":
                    break 
                
                else:
                    print("Invalid sub-choice. Please try again.")

        elif choice == "2":
            print("Doctor Menu:")
            while True:
                print("Enter 1 to add doctor")
                print("2 to print all doctors")
                print("Enter 3 to update Doctor ID ")
                print("Enter 4 to Delete Doctor ID")
                print("'exit' to return to the main menu:")
                sub_choice = input("Enter Choice: ")
                
                if sub_choice == "1":
                    create_doctor()
                
                elif sub_choice == "2":
                    print(doctor_list) 
                
                
                elif sub_choice == "3":
                    update_doctor()
                       
                
                elif sub_choice == "4" :
                    delete_doctor() 
                
                
                elif sub_choice.lower() == "exit":
                    break
                
                else:
                    print("Invalid sub-choice. Please try again.")

        elif choice == "3":
            print("Medical History Menu:")
            while True:
                print("Enter 1 to add medical history")
                print("2 to print all medical histories")
                print("'exit' to return to the main menu:")
                sub_choice = input("Enter Choice: ")
                
                if sub_choice == "1":
                    medicalhistory_input()
                
                elif sub_choice == "2":
                    print(medicalhistory_list)
                
                elif sub_choice.lower() == "exit":
                    break
                
                else:
                    print("Invalid sub-choice. Please try again.")

        elif choice == "4":
            print("Medicine Menu:")
            while True:
                print("Enter 1 to add medicine:")
                print("Enter 2 to show all medicines:")
                print("Enter 3 to update Medicine ID:")
                print("Enter 4 to Delete Medicine ID")
                print("'exit' to return to the main menu:")
                sub_choice = input("Enter Choice: ")
                
                if sub_choice == "1":
                    input_medicine()
                
                elif sub_choice == "2":
                    print(medicine_list)
                
                elif sub_choice == "3" :
                    update_medicine()

                
                elif sub_choice == "4":
                    delete_medicine()       

                elif sub_choice.lower() == "exit":
                    break
                
                else:
                    print("Invalid sub-choice. Please try again.")

        elif choice == "5":
            print("Appointment Menu:")
            while True:
                print("Enter 1 to add appointment")
                print("2 to print all appointments")
                print("Enter 3 to cancel appointment:")
                print("'exit' to return to the main menu:")
                sub_choice = input("Enter Choice: ")
                
                if sub_choice == "1":
                    create_appointment()
                
                elif sub_choice == "2":
                    print(appointment_list)  

                elif sub_choice == "3":
                    cancel_appointment()    
                
                elif sub_choice.lower() == "exit":
                    break
                
                else:
                    print("Invalid sub-choice. Please try again.")

        elif choice == "6":
            print("Encounter Menu:")
            while True:
                print("Enter 1 to Start encounter")
                print("'exit' to return to the main menu:")
                sub_choice = input("Enter Choice: ")

                if sub_choice == "1":
                    start_encounter()    
                
                elif sub_choice.lower() == "exit":
                    break
                
                else:
                    print("Invalid sub-choice. Please try again.")

                    

        elif choice == "7":
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")




def delete_patient():
    global patient_list 
    print("Current Patient list:")

    for patient in patient_list:
        print(patient)
    ID = int(input("Enter the correct ID you want to delete:"))

    
    patient_found = False
    for patient in patient_list:
        if int(patient['ID']) == ID:
            patient_list.remove(patient)
            patient_found = True
            print(f"Patient with ID : {ID} has been deleted.")
            break

    if not patient_found:
        print(f"No patient found with ID : {ID}.")

    print("Updated Patient list:")
    for patient in patient_list:
       print(patient)
    save_data(patient_list, "txtfiles/patient.txt" )   

   

def delete_doctor():
    global doctor_list
    
    print("Current Doctor List:\n")
    for doctor in doctor_list:
        print(doctor)   
    ID1=int(input("Enter the doctor Id you want to delete:"))
    doctor_found=False 
    for doctor in doctor_list:
        if int(doctor['ID']) == ID1:   
            doctor_list.remove(doctor)
            doctor_found=True
            print(f"Doctor With ID:{ID1} has been Deleted")
            break
    if not doctor_found:
        print(f"There is no Doctor with this ID:{ID1}.")  
   
    print("Updated Doctor List:") 
    for doctor in doctor_list:
        print(doctor)
    save_data(doctor_list, "txtfiles/doctor.txt")  

    
   

def delete_medicine():
    global medicine_list
    print("Current Medicine List:")
    for medicine in medicine_list:
        print(medicine)

    ID = int(input("Enter ID to Delete:"))    
    medicine_found = False   

    for medicine in medicine_list:
        if int(medicine['ID']) == ID: 
            medicine_list.remove(medicine)
            medicine_found = True
            break 

    if not medicine_found:
        print(f"No medicine found with ID : {ID}")    
    else:
        print("Medicine deleted successfully.")

    print("Updated Medicine List:") 
    for medicine in medicine_list:
        print(medicine)
    save_data(medicine_list, "txtfiles/medicine.txt")    
   


def update_patient():
    global patient_list
    print("Current Patient list:")
    for patient in patient_list:
        print(patient)

    ID = int(input("Enter Patient ID you want to change data:"))
    patient_found = False

    for patient in patient_list:
        if int(patient['ID']) == ID:
            new_name = input("Enter new name: ")
            new_age = input("Enter new age: ")
            new_gender = input("Enter Patient Gender: ")
            new_contact = input("Enter Patient Contact Info: ")
            new_Blood_type = input("Enter Blood Type: ")
            new_Disease_stage = input("Enter Disease Stage Level: ")
            new_email = input("Enter Patient Email: ")
            new_password = input("Enter Password: ")

            patient['Name'] = new_name
            patient['Age'] = new_age
            patient['Gender'] = new_gender
            patient['Contact'] = new_contact
            patient['Blood type'] = new_Blood_type
            patient['Disease Stage'] = new_Disease_stage
            patient['Email'] = new_email
            patient['Password'] = new_password

            patient_found = True
            break



    if not patient_found:
        print(f"No Patient found with ID: {ID}")
       
    print("Updated List data:")
    for patient in patient_list:
        print(patient)
    save_data(patient_list, "txtfiles/patient.txt" )     

 
        
def update_doctor():
    global doctor_list
    print("Current Doctor List:")
    for doctor in doctor_list:
        print(doctor)
    ID=int(input("Enter the Doctor ID you want to update:"))
    doctor_found=False
    for doctor in doctor_list:
        if int(doctor['ID']):
             new_name = (input("Enter Doctor Name: "))
             new_age =  (input("Enter Doctor Age: "))
             new_gender = input("Enter Doctor Gender: ")
             new_contact = input("Enter Doctor Contact Information: ")
             new_Designation=input("Enter the Designation: ")
             new_Speciality=input("Enter Speciality of doctor:")
             new_email = input("Enter Doctor Email: ")
             new_password=input("Enter Password:")

             
             doctor['name']=new_name
             doctor['age']=new_age
             doctor['gender']=new_gender
             doctor['contact']=new_contact
             doctor['designation'] =new_Designation
             doctor['speciality'] =new_Speciality
             doctor['Email'] =new_email
             doctor['Password'] =new_password
             doctor_found=True
             break
      

    if not doctor_found:
        print(f"Invalid  Doctor ID : {ID}")
    save_data(doctor_list, "txtfiles/doctor.txt")     

  

def update_medicine():
    print("Current Medicine List:")
    for medicine in medicine_list:
        print(medicine)

    ID = int(input("Enter Medicine ID you want to update: "))
    medicine_found = False

    for medicine in medicine_list:
        if int(medicine['ID']) == ID: 
            new_patient = input("Enter Patient Name: ")
            new_med_name = input("Enter Medicine Name: ")
            new_side_effects = input("Enter Side Effects (if any): ")
            new_expiry_date = input("Enter expiry date (YY-MM-DD): ")

            
            medicine['patient'] = new_patient
            medicine['med_name'] = new_med_name
            medicine['side_effects'] = new_side_effects
            medicine['expiry_date'] = new_expiry_date
            medicine_found = True
            break



    if not medicine_found:
        print(f"Invalid Medicine ID: {ID}")

    print("Updated Medicine List:")
    for medicine in medicine_list:
        print(medicine) 
    save_data(medicine_list, "txtfiles/medicine.txt")  



  
   
 

   

def cancel_appointment():
    global appointment_list  
    print("Current Appointments:")
    for appointment in appointment_list:
        print(f"ID: {appointment['Appointment_ID']}, Status: {appointment['Status']}")
    Appointment_ID = int(input("Enter Appointment ID to cancel: "))
    Appointment_found = False
    for appointment in appointment_list:
        if int(appointment['Appointment_ID']) == Appointment_ID: 
            appointment_list.remove(appointment) 
            appointment['Status'] = 'Cancelled' 
            Appointment_found = True
            print(f"Appointment {Appointment_ID} has been cancelled.")
            break
    
    if not Appointment_found:
        print(f"No Appointment found with ID : {Appointment_ID}.")

       

    print("Updated Appointmens: ") 
    for appointment in appointment_list:
        print(appointment)
    save_data(appointment_list, "txtfiles/appointment.txt")    



def start_encounter():
    global appointment_list
    global encounter_list

    print("Current Appointments:")
    for appointment in appointment_list:
        print(f"ID: {appointment['Appointment_ID']}, Status: {appointment['Status']}")

    Id = int(input("Enter the appointment ID: "))
    found_appointment = None

    for appointment in appointment_list:
        if int(appointment['Appointment_ID']) == Id:
            found_appointment = appointment
            break

    if found_appointment:
        patient = found_appointment['Patient']
        doctor = found_appointment['Doctor']
        date = found_appointment['Date']
        prescribed_med = input("Enter prescribed medications: ")
        recommended_test = input("Enter recommended tests: ")
        patient_ID = found_appointment['Patient_ID']
        doctor_ID = found_appointment['Doctor_ID']
        reason = input("Enter the reason for encounter: ")
        status = 'completed'
        notes = input("Enter any additional notes: ")


        from appointment import Encounter
        encounter_obj = Encounter(
            patient=patient,
            doctor=doctor,
            appointment_id=Id,
            date=date,
            prescribed_med=prescribed_med,
            recommended_test=recommended_test,
            patient_ID=patient_ID,
            doctor_ID=doctor_ID,
            reason=reason,
            status=status,  
            notes=notes
        )

        encounter_list.append(encounter_obj)
        found_appointment['Status'] = 'completed'


        print(f"Encounter created for appointment {Id} and status set to 'completed'.")
    else:
        print(f"No appointment found with ID: {Id}")
    save_data(encounter_list, "txtfiles/encounter.txt")    

           
    
   




def save_data(obj_list, file_path):
    with open(file_path, 'w') as file:  
        for obj in obj_list:
            file.write(f"{obj}\n")



save_data(patient_list, "txtfiles/patient.txt" )
save_data(doctor_list, "txtfiles/doctor.txt") 
save_data(medicalhistory_list, "txtfiles/medicalhistory.txt" )
save_data(medicine_list, "txtfiles/medicine.txt")
save_data(appointment_list, "txtfiles/appointment.txt")
save_data(encounter_list, "txtfiles/encounter.txt")



           



def fetch_data(filepath, list_name):
 with open(filepath, 'r') as file:
        for line in file:
            list_name.append(line.strip())

fetch_data('txtfiles/patient.txt',patient_list) 
fetch_data('txtfiles/doctor.txt',doctor_list)   
fetch_data('txtfiles/medicalhistory.txt',medicalhistory_list) 
fetch_data('txtfiles/medicine.txt',medicine_list)
fetch_data('txtfiles/appointment.txt',appointment_list)

        
     


menu() 



    
