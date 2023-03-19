from domain.patients import Patient, Department


class PatientsRepository:
    def __init__(self, initial_patients=None):
        """
        Initialize a PatientsRepository object with an optional list of initial patients.
        :param initial_patients: A list of Patient objects to initialize the repository with.
        """
        self.list_of_patients = []
        if initial_patients is not None:
            for patient in initial_patients:
                self.list_of_patients.append(patient)

    def create_patient(self, first_n, last_n, pnc, disease):
        """
        Create a new Patient object and add it to the repository.
        :param first_n: The patient's first name.
        :param last_n: The patient's last name.
        :param pnc: The patient's personal numeric code.
        :param disease: The patient's disease.
        """
        p = Patient(first_n, last_n, pnc, disease)
        self.list_of_patients.append(p)

    def read(self):
        """
        Get the list of patients in the repository.
        :return: The list of patients in the repository.
        """
        return self.list_of_patients

    def update(self, patient, first_n_u, last_n_u, pnc_u, disease_u):
        """
        Update the attributes of a patient in the repository.
        :param patient: The patient to update.
        :param first_n_u: The new first name.
        :param last_n_u: The new last name
        :param pnc_u: The new personal numeric code.
        :param disease_u: The new disease.
        """
        self.list_of_patients[patient].set_first_name(first_n_u)
        self.list_of_patients[patient].set_last_name(last_n_u)
        self.list_of_patients[patient].set_personal_num_code(pnc_u)
        self.list_of_patients[patient].set_disease(disease_u)

    def delete(self, patient_del):
        """
        Remove a patient from the repository.
        :param patient_del: The patient to remove.
        """
        del self.list_of_patients[patient_del]


class DepartmentRepository:
    def __init__(self, initial_departments=None):
        """
        Initialize a DepartmentsRepository object with an optional list of initial departments.
        :param initial_departments: A list of Department objects to initialize the repository with.
        """
        self.list_of_departments = []
        if initial_departments is not None:
            for department in initial_departments:
                self.list_of_departments.append(department)

    def create_department(self, id2, name, num_b, list_p):
        """
        Create a new Department object and add it to the repository.
        :param id2: The department's unique identifier.
        :param name: The department's name.
        :param num_b: The number of beds in the department.
        :param list_p: A list of Patient objects assigned to the department.
        """
        p = Department(id2, name, num_b, list_p)
        self.list_of_departments.append(p)

    def read(self):
        """
        Get the list of departments in the repository.
        :return: The list of departments in the repository.
        """
        return self.list_of_departments

    def update(self, department1, id_u, name_u, num_b_u, list_p_u):
        """
        Update the attributes of a department in the repository.
        :param department1: The department to update.
        :param id_u: The new unique identifier.
        :param name_u: The new name
        :param num_b_u: The new number of beds.
        :param list_p_u: The new list of patients.
        """
        self.list_of_departments[department1].set_id(id_u)
        self.list_of_departments[department1].set_name(name_u)
        self.list_of_departments[department1].set_num_of_beds(num_b_u)
        self.list_of_departments[department1].set_list_of_p(list_p_u)

    def delete(self, department):
        """
        Remove a department from the repository.
        :param department: The department to remove.
        """
        del self.list_of_departments[department]
