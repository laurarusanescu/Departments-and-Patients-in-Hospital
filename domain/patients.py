import datetime

from infrastructures.helpers import is_cnp_valid


class Patient:
    def __init__(self, first_name, last_name, personal_num_code, disease):
        """

        :param first_name:
        :param last_name:
        :param personal_num_code:
        :param disease:
        """
        self.patients = []
        self.__first_name1 = first_name
        self.__last_name1 = last_name
        self.__personal_num_code1 = personal_num_code
        self.__disease1 = disease

    def get_first_name(self):
        return self.__first_name1

    def get_last_name(self):
        return self.__last_name1

    def get_personal_code(self):
        return self.__personal_num_code1

    def get_disease(self):
        return self.__disease1

    @property
    def first_name_p(self):
        return self.__first_name1

    @property
    def last_name_p(self):
        return self.__last_name1

    @property
    def personal_num_code_p(self):
        return self.__personal_num_code1

    @property
    def disease_p(self):
        return self.__disease1

    def set_first_name(self, new_first_name):
        self.__first_name1 = new_first_name

    def set_last_name(self, new_last_name):
        self.__last_name1 = new_last_name

    def set_personal_num_code(self, new_pnc):
        self.__personal_num_code1 = new_pnc

    def set_disease(self, new_disease):
        self.__disease1 = new_disease

    def age(self):
        birth_year = int(self.__personal_num_code1([1, 3]))

        birth_month = int(self.__personal_num_code1([3, 5]))
        birth_dat = int(self.__personal_num_code1([5, 7]))
        if birth_year > 22:
            birth_date = datetime.datetime(1900+birth_year, birth_month, birth_dat)
        else:
            birth_date = datetime.datetime(2000+birth_year, birth_month, birth_dat)
        date = datetime.datetime.now()
        diff = date - birth_date
        age = diff/365.25
        return age

class Department:
    def __init__(self, id, name, num_of_beds, patients=None):
        """
        Initialize a Department object with an id, name, number of beds and an optional list of patients.
        :param id: The department's unique identifier.
        :param name: The department's name.
        :param num_of_beds: The number of beds in the department.
        :param patients: A list of Patient objects assigned to the department.
        """
        self.departments = []
        self.id1 = id
        self.name1 = name
        self.num_of_beds1 = num_of_beds
        if self.num_of_beds1 > len(self.patients1):
            self.patients1 = patients
        else:
            raise ValueError("The capacity of theis department has been reached.")

    def get_id(self):
        return self.id1

    def get_name(self):
        return self.name1

    def get_num_of_beds(self):
        return self.num_of_beds1

    def get_list_of_p(self):
        return self.patients1

    @property
    def id_p(self):
        return self.id1

    @property
    def name_p(self):
        return self.name1

    @property
    def num_of_beds_p(self):
        return self.num_of_beds1

    @property
    def list_of_p_p(self):
        return self.patients1

    def set_id(self, new_id):
        self.id1 = new_id

    def set_name(self, new_name):
        self.name1 = new_name

    def set_num_of_beds(self, new_num_of_beds):
        self.num_of_beds1 = new_num_of_beds

    def set_list_of_p(self, new_list_of_p):
        self.patients1 = new_list_of_p

