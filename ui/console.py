from infrastructures.repositories import Patient
from infrastructures.repositories import PatientsRepository
from infrastructures.repositories import Department
from infrastructures.repositories import DepartmentRepository
from application.controller import HospitalRepository

class ui:
    def __init__(self, hr):
        self.__hr = hr

    def hey(self):
        def greet():
            print("Welcome to out program that has all the data about the hospital, here are some things you can do:")
            print("0. Close our program.")
            print("1. Operations regarding patients.")
            print("2. Operations regarding departments.")
            print("3.Sort the patients in a department by personal numerical code")
            print("4.Sort departments by the number of patients")
            print("5.Sort departments by the number of patients having the age above a given limit")
            print("6.Sort departments by the number of patients and the patients in a department alphabetically")
            print("7.Identify departments where there are patients under a given age")

        greet()
        c = 1


        while c != 0:
            c = int(input("Chose the number of your comand:"))
            if c == 1:
                print("1. Add a patient.")
                print("2. See the list of patients.")
                print("3. Update the information regarding a patient.")
                print("4. Delete a patient")
                print("5. Go in the main menu")
                c1 = int(input("Chose your comand regarding patients:"))
                if c1 == 1:
                    first_name = input("First name of the patient:")
                    last_name = input("Last name of the patient:")
                    pnc = input("Person's personal numeric code:")
                    disease = input("Person's desease:")
                    try:
                        self.__hr.create_p(first_name, last_name, pnc, disease)
                    except ValueError as ve:
                        print(ve)
                if c1 == 2:
                    self.__hr.read()
                if c1 == 3:
                    patient = input("Id of the patient:")
                    first_name = input("First name of the patient:")
                    last_name = input("Last name of the patient:")
                    pnc = int(input("Person's personal numeric code:"))
                    disease = input("Person's desease:")
                    try:
                        self.__hr.update_p(patient, first_name, last_name, pnc, disease)
                    except:
                        raise ValueError("The data is not vald.")
                if c1 == 4:
                    patient = int(input("Id fo the student:"))
                    try:
                        self.__hr.delete_p(patient)
                    except:
                        raise ValueError("The data is not vald.")
                if c1 == 5:
                    break
            if c == 2:
                print("1. Add a department.")
                print("2. See the list of departments.")
                print("3. Update the information regarding a department.")
                print("4. Delete a department")
                print("5. Go in the main menu")
                c2 = int(input("Chose your comand."))
                if c2 == 1:
                    id = int(input("Id of the department"))
                    name = input("Name of the department")
                    num_of_beds = int(input("Number fo beds in the department"))
                    patients = input("Patients in the department:")
                    try:
                        self.__hr.create_d(id, name, num_of_beds, patients)
                    except:
                        raise ValueError("The data is not vald.")
                if c2 == 2:
                    self.__hr.read()
                if c2 == 3:
                    id = int(input("Id of the department"))
                    name = input("Name of the department")
                    num_of_beds = int(input("Number fo beds in the department"))
                    patients = input("Patients in the department:")
                    try:
                        self.__hr.update_d(id, id, name, num_of_beds, patients)
                    except:
                        raise ValueError("The data is not vald.")
                if c2 == 4:
                    department = int(input("Id of the department:"))
                    try:
                        self.__hr.delete_d(department)
                    except:
                        raise ValueError("The data is not vald.")
            if c == 3:
                self.__hr.sort_patients_by_personal_num_code()
                self.__hr.read()

            if c == 4:
                self.__hr.sort_departments_by_num_patients()
                self.__hr.read()

            if c == 5:
                age = int(input("Age:"))
                self.__hr.sort_departments_by_num_patients_above_age(age)

            if c == 6:
                self.__hr.sort_departments_by_num_of_pacients_and_pacients_alphabetically()

            if c == 7:
                age_limit = int(input("Age limit:"))
                self.__hr.find_departments_with_young_patients(age_limit)

            if c == 8:
                name = input("Nme searched:")
                self.__hr.find_patients_by_name(name)

            if c == 9:
                first_name = input("First name: ")
                self.__hr.find_departments_with_patients_by_name(first_name)
