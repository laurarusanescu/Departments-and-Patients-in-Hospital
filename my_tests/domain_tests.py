import unittest
from infrastructures.repositories import Patient
from infrastructures.repositories import PatientsRepository
from infrastructures.repositories import Department
from infrastructures.repositories import DepartmentRepository
from application.controller import Hospital
from application.controller import HospitalRepository


class TestHospitalRepository(unittest.TestCase):
    def setUp(self):
        self.patient1 = Patient("John", "Doe", "5040807352591", "Flu")
        self.patient2 = Patient("Jane", "Doe", "6030204057476", "Cold")
        self.patient3 = Patient("Bob", "Smith", "5040807352591", "Cold")
        self.patient4 = Patient("Janet", "Doe", "6030204057476", "Pneumonia")
        self.department1 = Department('Surgery', 34, [self.patient1, self.patient2])
        self.department2 = Department('Internal Medicine', 40, [self.patient3, self.patient4])
        self.repo = HospitalRepository(initial_departments=[self.department1, self.department2])

    def test_sort_patients_by_personal_num_code(self):
        self.repo.sort_patients_by_personal_num_code()
        self.assertEqual(self.department1.patient[0], self.patient1)
        self.assertEqual(self.department1.patients[1], self.patient2)

    def test_sort_departments_by_num_patients(self):
        self.repo.sort_departments_by_num_patients()
        self.assertEqual(self.repo.list_of_departments[0], self.department1)
        self.assertEqual(self.repo.list_of_departments[1], self.department2)

    def test_sort_departments_by_num_patients_above_age(self):
        # This method should be changed to use patient's age instead of age limit
        self.repo.sort_departments_by_num_patients_above_age(30)
        self.assertEqual(self.repo.list_of_departments[0], self.department2)
        self.assertEqual(self.repo.list_of_departments[1], self.department1)

    def test_find_departments_with_young_patients(self):
        young_patient_departments = self.repo.find_departments_with_young_patients(30)
        self.assertEqual(young_patient_departments[0], self.department1)

    def test_find_patients_by_name(self):
        matching_patients = self.repo.find_patients_by_name('Doe')
        self.assertEqual(matching_patients[0], self.patient1)
        self.assertEqual(matching_patients[1], self.patient2)

    def test_find_departments_with_patients_by_name(self):
        matching_departments = self.repo.find_departments_with_patients_by_name('John')
        self.assertEqual(matching_departments[0], self.department1)
