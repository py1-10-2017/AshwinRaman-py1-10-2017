class Patient(object):
    def __init__(self, id_number, name, allergies, bed_number):
        self.name = name
        self.allergies = allergies
        self.id_number = id_number
        self.bed_number = "None"

class Hospital(object):
    def __init__(self, hospital_name, capacity, current):
        self.patients = []
        self.hospital_name = hospital_name
        self.capacity = capacity
        self.current = current

    def admit(self, patient):
        if self.current < self.capacity:
            self.current = self.current + 1
            self.patients.append(patient)
            for patient in self.patients:
                patient.bed_number = self.current
                print "Patient Admitted"
                print "Bed Number: " + str(patient.bed_number)
                return self
        else:
            print "Capacity Reached"
            return self

    def discharge(self, patient):
        self.current = self.current - 1
        self.patients.pop(0)
        self.bed_number = "None"
        print "Discharged Patient"
        print "Bed Number: None"
        print "Amount of beds in use: " + str(self.current)
        return self

Patient1 = Patient("34", "Ashwin", "None", 0)

Hospital1 = Hospital("Northwestern", 400, 376)

Hospital1.admit(Patient1).discharge(Patient1).admit(Patient1)
