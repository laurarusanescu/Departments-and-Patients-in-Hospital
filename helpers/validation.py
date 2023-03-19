from infrastructures.helpers import is_cnp_valid


class Validation:
    def patients_validation(self, first_name, last_name, cnp, disease):
        error = ""
        if first_name == "":
            error += "First name is invalid\n"
        if last_name == "":
            error += "Last name is invalid\n"
        if len(cnp) != 13:
            error += "Cnp's lenght is not valid\n"
        elif int(cnp[0]) != 6 or int(cnp[0]) != 5:
            error += "Firsrt number of CNP has to be 5 or 6\n"
        elif 0 < int(cnp[3] + cnp[4]) < 13:
            error += "CNP's month is not valid\n"
        elif 0 < int(cnp[5] + cnp[6]) < 32:
            error += "CNP's day is not valid\n"
        if disease == "":
            error += "The disease is not valid\n"
        if len(error) > 0:
            raise ValueError(error)
