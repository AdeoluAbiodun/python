# Name: Adeolu T. Abiodun  ||  Date: 02/27/2025  ||  Program file: AdeoluAbiodun_lab10-1.py

# This Python program utilizes classes to accept user inputs and display patient details along with their procedure information.


from datetime import datetime

class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone, emergency_name, emergency_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.emergency_name = emergency_name
        self.emergency_phone = emergency_phone
    
    def Full_Name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
    
    def Address(self):
        return f"{self.address}, {self.city}, {self.state} {self.zip_code}"
    
    def Phone(self):
        return self.phone
    
    def Emergency_Contact(self):
        return f"{self.emergency_name} - {self.emergency_phone}"

class Procedure:
    def __init__(self, name, date, practitioner, charge):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charge = charge
    
    def Procedure_Details(self):
        return f"Procedure: {self.name}\nDate: {self.date}\nPractitioner: {self.practitioner}\nCharge: ${self.charge:.2f}\n"

# Collecting patient information
print("Enter patient details here:")
first_name = input("First Name: ")
middle_name = input("Middle Name: ")
last_name = input("Last Name: ")
address = input("Address: ")
city = input("City: ")
state = input("State: ")
zip_code = input("ZIP Code: ")
phone = input("Phone Number: ")
emergency_name = input("Emergency Contact name: ")
emergency_phone = input("Emergency Contact phone #: ")

patient = Patient(first_name, middle_name, last_name, address, city, state, zip_code, phone, emergency_name, emergency_phone)


today_date = datetime.today().strftime('%m/%d/%Y')

# Procedures along with the correct practitioner names
procedures = [
    Procedure("Physical Exam", today_date, "Dr. Irvine", 250.00),
    Procedure("X-ray", today_date, "Dr. Jamison", 500.00),
    Procedure("Blood test", today_date, "Dr. Smith", 200.00)
]

# Display patient details
print("\nBelow is the patient information")
print("================================")
print(f"Name: {patient.Full_Name()}")
print(f"Address: {patient.Address()}")
print(f"Phone: {patient.Phone()}")
print(f"Emergency Contact: {patient.Emergency_Contact()}")


# Display procedure information
print("\nHere are the procedures details")
print("===============================")
total_charges = 0
for procedure in procedures:
    print(procedure.Procedure_Details())
    total_charges += procedure.charge

print()
# Total charges
print(f"Total Charges: ${total_charges:.2f}")