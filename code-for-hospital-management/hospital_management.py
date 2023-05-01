# Defining a class for patients
class Patient:
    def __init__(self, name, age, gender, symptoms, doctor):
        self.name = name
        self.age = age
        self.gender = gender
        self.symptoms = symptoms
        self.doctor = doctor

    # Defining a magic method for string formatting
    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Symptoms: {self.symptoms}, Doctor: {self.doctor}'


# Defining a class for doctor
class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    # Defining a magic method to format string
    def __str__(self):
        return f'{self.name}, {self.specialization}'


# Defining a class for hospital
class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []

    # Defining a function to add patients
    def add_patient(self, patient):
        self.patients.append(patient)

    # Defining a function to add doctors
    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    # Defining a function to display patients
    def display_patients(self):
        for patient in self.patients:
            print(patient)

    # Defining a function to display doctors
    def display_doctors(self):
        for doctor in self.doctors:
            print(doctor)
