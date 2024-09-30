from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, ID, name, age, gender, contact, email,password):
        self.ID = ID
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact
        self.email = email
        self.password=password

    @abstractmethod
    def __str__(self):
        pass


class Patient(Person):  
    def __init__(self, patient_ID, name, age, Blood_type, Disease_stage, gender, contact, email, password):
        super().__init__(patient_ID, name, age, gender, contact, email, password)
        self.Blood_type = Blood_type
        self.Disease_stage = Disease_stage

    def __str__(self):
        return ('{'
            f'"ID": "{self.ID}", '
            f'"Name": "{self.name}", '
            f'"Age": "{self.age}", '
            f'"Gender": "{self.gender}", '
            f'"Blood type": "{self.Blood_type}", '
            f'"Disease Stage": "{self.Disease_stage}", '            
            f'"Contact": "{self.contact}", '
            f'"Email": "{self.email}", '
            f'"Password": "{self.password}"'
            '}')
     
    


class Doctor(Person):
    def __init__(self, doctor_ID, name, age, gender,Designation,Speciality, contact, email,password):
        super().__init__(doctor_ID, name, age, gender, contact, email,password)
        self.Designation=Designation
        self.Speciality=Speciality

    def __str__(self):
       return ('{'
            f'"ID": "{self.ID}", '
            f'"Name": "{self.name}", '
            f'"Age": {self.age}, '
            f'"Designation": "{self.Designation}", '
            f'"Speciality": "{self.Speciality}", '
            f'"Gender": "{self.gender}", '
            f'"Contact": "{self.contact}", '
            f'"Email": "{self.email}", '
            f'"Password": "{self.password}"'
            '}')
