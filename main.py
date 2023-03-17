from heplers.validation import Validation
from ui.console import ui
from infrastructures.repositories import PatientsRepository, DepartmentRepository
from application.controller import HospitalRepository

if __name__ == '__main__':
    pr = PatientsRepository()
    dr = DepartmentRepository()
    v = Validation()
    hr = HospitalRepository(pr, dr, v)

    run = ui(hr)

run.hey()

