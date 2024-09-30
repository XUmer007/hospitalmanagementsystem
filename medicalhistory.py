from users import Patient

class MedicalHistory(Patient):
    def __init__(self, patient_ID,patient, condition, status, start_date, end_date, allergies):
        self.patient_ID=patient_ID
        self.patient = patient
        self.condition = condition
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.allergies = allergies

    
    def __str__(self):
     return ('{'
            f'"Patient_ID": "{self.patient_ID}", '
            f'"Patient": "{self.patient}", '
            f'"Condition": "{self.condition}", '
            f'"Status": "{self.status}", '
            f'"Start Date": "{self.start_date}", '
            f'"End Date": "{self.end_date}", '
            f'"Allergies": "{self.allergies}"'
            '}')









