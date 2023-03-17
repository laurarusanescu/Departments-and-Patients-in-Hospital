from infrastructures.repositories import Patient
from infrastructures.repositories import PatientsRepository
from infrastructures.repositories import DepartmentRepository



class HospitalRepository:
    def __init__(self, pr, dr, Validation):
        """
        Initialise a HospitalRepository object with an optional list of departments.
        :param pr:
        :param dr:
        :param initial_departments:
        """
        self.list_of_departments = []
        self.__pr = pr
        self.__dr = dr
        self.__validation = Validation


    def create_p(self, first_name, last_name, pnc, disease):
        self.__validation.patients_validation(first_name, last_name, pnc, disease)
        self.__pr.create_patient(first_name, last_name, pnc, disease)

    def update_p(self, name, first_name_update, last_name_update, pnc_update, disease_update):
        self.__pr.update_patient(name, first_name_update, last_name_update, pnc_update, disease_update)

    def delele_p(self, name):
        self.__pr.delete(name)

    def create_d(self, id2, name, num_b, list_p):
        self.__dr.create_department(id2, name, num_b, list_p)

    def update_d(self, department1, id_u, name_u, num_b_u, list_p_u):
        self.__dr.update_department( department1, id_u, name_u, num_b_u, list_p_u)

    def delete_d(self, name):
        self.__dr.delete(name)

    def read(self):
        """
        Return the list of departments.
        :return:
        """
        return self.list_of_departments

    def sort_patients_by_personal_num_code(self):
        """
        Sort the patients in the department by personal numerical code.
        """
        self.list_of_departments.sort(key=lambda p: p.personal_num_code)

    def sort_departments_by_num_patients(self):
        """
        Sort departments by the number of patients.
        """
        self.list_of_departments.sort(key=lambda d: len(d.patients))

    def sort_departments_by_num_patients_above_age(self, age):
        """
        Sort departments by the number of patients having the age above a given limit.
        :param age: Age limit
        """
        self.list_of_departments.sort(key=lambda d: len([p for p in d.patients if p.age() > age]))

    def sort_departments_by_num_of_pacients_and_pacients_alphabetically(self, departments, patients):
        """
        Sort departments by number of patients and patients alphabetically.
        :param departments:
        :param patients:
        :return:
        """
        departments.sort(key=lambda d: len(d.patients))
        patients.sort(key=lambda p: (p.first_name, p.last_name))

    def find_departments_with_young_patients(self, age_limit):
        """
        Identify departments where there are patients under a given age.
        :param age_limit: The age maximum age.
        :return:
        """
        young_patient_departments = []
        for department in self.list_of_departments:
            for patient in department:
                if patient.age < age_limit:
                    young_patient_departments.append(department)
                    break
        return young_patient_departments

    def find_patients_by_name(self, name_string):
        """
        Identify patients from a given department for which the first name or last name contain a given string.
        :param name_string: Name that is searched.
        :return:
        """
        matching_patients = []
        for department in self.list_of_departments:
            for patient in department:
                if name_string in patient.first_name or name_string in patient.last_name:
                    matching_patients.append(patient)
        return matching_patients

    def find_departments_with_patients_by_name(self, first_name):
        """
        Identify department/departments where there are patients with a given first name.
        :param first_name: First name that is going to be searched for.
        :return:
        """
        matching_departments = []
        for department in self.list_of_departments:
            for patient in department:
                if patient.first_name == first_name:
                    matching_departments.append(department)
                    break
        return matching_departments
