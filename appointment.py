from  users import Patient,Doctor

class Appointment(Patient, Doctor):
    def __init__(self, patient_ID, doctor_ID, patient, doctor, appointment_id, date, reason, status):
        self.patient_ID = patient_ID  
        self.doctor_ID = doctor_ID  
        self.patient = patient
        self.doctor = doctor
        self.appointment_id = appointment_id
        self.date = date
        self.reason = reason
        self.status = status

    
    def __str__(self):
      return ('{'
            f'"Appointment_ID": "{self.appointment_id}", '
            f'"Patient_ID": "{self.patient_ID}", '
            f'"Doctor_ID": "{self.doctor_ID}", '
            f'"Patient Name": "{self.patient}", '
            f'"Doctor Name": "{self.doctor}", '
            f'"Date": "{self.date}", '
            f'"Reason": "{self.reason}", '
            f'"Status": "{self.status}"'
            '}')



class Encounter(Appointment, Patient):
    def __init__(self, patient, doctor, appointment_id, date, prescribed_med, recommended_test, patient_ID, doctor_ID, reason, status, notes):
        Appointment.__init__(self, patient_ID, doctor_ID, patient, doctor, appointment_id, date, reason, status)

        self.prescribed_med = prescribed_med
        self.recommended_test = recommended_test
        self.notes = notes


    def __str__(self):
      return ('{'
            f'"Appointment_ID": "{self.appointment_id}", '
            f'"Patient": "{self.patient}", '
            f'"Doctor": "{self.doctor}", '
            f'"Date": "{self.date}", '
            f'"Status": "{self.status}", '
            f'"Prescribed Med": "{self.prescribed_med}", '
            f'"Recommended Test": "{self.recommended_test}", '
            f'"Notes": "{self.notes}"'
            '}')


