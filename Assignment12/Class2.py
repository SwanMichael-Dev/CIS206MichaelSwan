class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_contact_name, emergency_contact_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_middle_name(self):
        return self.middle_name

    def set_middle_name(self, middle_name):
        self.middle_name = middle_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def get_zip_code(self):
        return self.zip_code

    def set_zip_code(self, zip_code):
        self.zip_code = zip_code

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_emergency_contact_name(self):
        return self.emergency_contact_name

    def set_emergency_contact_name(self, emergency_contact_name):
        self.emergency_contact_name = emergency_contact_name

    def get_emergency_contact_phone(self):
        return self.emergency_contact_phone

    def set_emergency_contact_phone(self, emergency_contact_phone):
        self.emergency_contact_phone = emergency_contact_phone


class Procedure:
    def __init__(self, name, date, practitioner, charges):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charges = charges

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_practitioner(self):
        return self.practitioner

    def set_practitioner(self, practitioner):
        self.practitioner = practitioner

    def get_charges(self):
        return self.charges

    def set_charges(self, charges):
        self.charges = charges


patient = Patient("John", "A", "Doe", "123 Main St", "Anytown", "CA", "12345", "555-1212", "Jane Doe", "555-5555")

procedure1 = Procedure("Physical Exam", "2024-11-17", "Dr. Irvine", 250.00)
procedure2 = Procedure("X-Ray", "2024-11-17", "Dr. Jamison", 500.00)
procedure3 = Procedure("Blood Test", "2024-11-17", "Dr. Smith", 200.00)

print("Patient Information:")
print("First Name:", patient.get_first_name())
print("Middle Name:", patient.get_middle_name())
print("Last Name:", patient.get_last_name())
print("Address:", patient.get_address())
print("City:", patient.get_city())
print("State:", patient.get_state())
print("Zip Code:", patient.get_zip_code())
print("Phone Number:", patient.get_phone_number())
print("Emergency Contact Name:", patient.get_emergency_contact_name())
print("Emergency Contact Phone:", patient.get_emergency_contact_phone())

print("\nProcedure Information:")
print("Procedure 1:")
print("Name:", procedure1.get_name())
print("Date:", procedure1.get_date())
print("Practitioner:", procedure1.get_practitioner())
print("Charges:", procedure1.get_charges())

print("\nProcedure 2:")
print("Name:", procedure2.get_name())
print("Date:", procedure2.get_date())
print("Practitioner:", procedure2.get_practitioner())
print("Charges:", procedure2.get_charges())

print("\nProcedure 3:")
print("Name:", procedure3.get_name())
print("Date:", procedure3.get_date())
print("Practitioner:", procedure3.get_practitioner())
print("Charges:", procedure3.get_charges())

total_charges = procedure1.get_charges() + procedure2.get_charges() + procedure3.get_charges()
print("\nTotal Charges:", total_charges)
