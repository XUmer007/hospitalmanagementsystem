from users import Patient
class Medicine(Patient):
    def __init__(self, medicine_ID, patient_ID, patient, med_name, sideEffects, expiry_date):
        self.patient_ID=patient_ID 
        self.medicine_ID = medicine_ID
        self.patient = patient
        self.med_name = med_name
        self.sideEffects = sideEffects
        self.expiry_date = expiry_date

    def __str__(self):
        return (f'  {{  "Medicine ID": {self.medicine_ID},  "Patient": "{self.patient}", '
                           f'  "Name": "{self.med_name}",  "Side Effects": "{self.sideEffects}", '
                           f'  "Expiry Date": {self.expiry_date}  }}')