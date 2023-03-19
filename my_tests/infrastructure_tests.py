import unittest
from infrastructures.repositories import PatientsRepository
from infrastructures.repositories import DepartmentRepository


class TestPatientsRepository(unittest.TestCase):
    def setUp(self):
        self.patients_repo = PatientsRepository()

    def test_create_patient(self):
        self.patients_repo.create_patient("John", "Doe", "6030204057476", "Flu")
        self.assertEqual(len(self.patients_repo.read()), 1)
        self.assertEqual(self.patients_repo.read()[0].first_name, "John")
        self.assertEqual(self.patients_repo.read()[0].last_name, "Doe")
        self.assertEqual(self.patients_repo.read()[0].personal_num_code, "6030204057476")
        self.assertEqual(self.patients_repo.read()[0].disease, "Flu")

    def test_update(self):
        self.patients_repo.create_patient("John", "Doe", "5040807352591", "Flu")
        self.patients_repo.update(0, "Jane", "Doe", "6030204057476", "Cold")
        self.assertEqual(len(self.patients_repo.read()), 1)
        self.assertEqual(self.patients_repo.read()[0].first_name, "Jane")
        self.assertEqual(self.patients_repo.read()[0].last_name, "Doe")
        self.assertEqual(self.patients_repo.read()[0].personal_num_code, "6030204057476")
        self.assertEqual(self.patients_repo.read()[0].disease, "Cold")

    def test_delete(self):
        self.patients_repo.create_patient("John", "Doe", "5040807352591", "Flu")
        self.patients_repo.delete(0)
        self.assertEqual(len(self.patients_repo.read()), 0)


class TestDepartmentRepository(unittest.TestCase):
    def setUp(self):
        self.department_repo = DepartmentRepository()

    def test_create_department(self):
        self.department_repo.create_department("123", "Department A", 10, [])
        self.assertEqual(len(self.department_repo.read()), 1)
        self.assertEqual(self.department_repo.read()[0].id, "123")
        self.assertEqual(self.department_repo.read()[0].name, "Department A")
        self.assertEqual(self.department_repo.read()[0].num_of_beds, 10)
        self.assertEqual(self.department_repo.read()[0].list_of_p, [])

    def test_update(self):
        self.department_repo.create_department("123", "Department A", 10, [])
        self.department_repo.update(0, "456", "Department B", 15, [])
        self.assertEqual(len(self.department_repo.read()), 1)
        self.assertEqual(self.department_repo.read()[0].id, "456")
        self.assertEqual(self.department_repo.read()[0].name, "Department B")
        self.assertEqual(self.department_repo.read()[0].num_of_beds, 15)
        self.assertEqual(self.department_repo.read()[0].list_of_p, [])

    def test_delete(self):
        self.department_repo.list_of_departments = []
        self.department_repo.create_department("123", "Department A", 10, [])
        self.department_repo.delete(0)
        self.assertEqual(len(self.department_repo.read()), 0)


if __name__ == '__main__':
    unittest.main()
