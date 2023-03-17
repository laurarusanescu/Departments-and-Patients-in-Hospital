from infrastructures.repositories import Patient
from infrastructures.repositories import PatientsRepository
from infrastructures.repositories import Department
from infrastructures.repositories import DepartmentRepository
from application.controller import Hospital
from application.controller import HospitalRepository

def DataExamplesPatients():
    patient1 = Patient("John", "Doe", "6050819363231", "Influenza")
    patient2 = Patient("Jane", "Doe", "6030204057476", "Pneumonia")
    patient3 = Patient("James", "Smith", "5040807352591", "Cancer")

    print(patient1.first_name_p)  # Output: "John"
    print(patient2.last_name_p)  # Output: "Doe"
    print(patient3.personal_num_code_p)  # Output: "5040807352591"
    print(patient1.disease_p)  # Output: "Influenza"
    print(patient2.age ())  # Output: 41.6

    patient1.set_first_name("Jack")
    patient1.set_last_name("Smith")
    print(patient1.first_name_p)  # Output: "Jack"
    print(patient1.last_name_p)  # Output: "Smith"

def DataExamplesPatientRepo():
    repository = PatientsRepository()
    repository.create_patient("John", "Doe", "6050819363231", "Flu")
    repository.create_patient("Jane", "Doe", "6030204057476", "Bronchitis")
    repository.create_patient("Bob", "Smith", "5040807352591", "Cold")
    print(repository.read())
    repository.update(1, "Janet", "Doe", "6030204057476", "Pneumonia")
    print(repository.read())
    repository.delete(0)
    print(repository.read())

def DataExamplesDepartments():
    department = Department(1, "Cardiology", 10, ["Patient1", "Patient2", "Patient3"])

    print(department.get_id())
    print(department.get_name())
    print(department.get_num_of_beds())
    print(department.get_list_of_p())

    department.set_id(2)
    department.set_name("Neurology")
    department.set_num_of_beds(15)
    department.set_list_of_p(["Patient4", "Patient5", "Patient6"])
    print(department.id_p)
    print(department.name_p)
    print(department.num_of_beds_p)
    print(department.list_of_p_p)

def DataExamplesDepartmentsRepo():
    repository = DepartmentRepository()

    repository.create_department(1, "Cardiology", 10, ["Patient1", "Patient2", "Patient3"])
    repository.create_department(2, "Neurology", 15, ["Patient4", "Patient5", "Patient6"])
    repository.create_department(3, "Surgery", 20, ["Patient7", "Patient8", "Patient9"])
    print(repository.read())

    repository.update(1, 2, "Oncology", 20, ["Patient10", "Patient11", "Patient12"])
    print(repository.read())

    repository.delete(0)
    print (repository.read())

