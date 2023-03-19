

def is_cnp_valid(cnp):
    v = 0
    if len(cnp) == 13:
        if int(cnp[0]) == 6 or int(cnp[0]) == 5:
            st = cnp[3] + cnp[4]
            st2 = cnp[5]+ cnp[6]
            if 0 < int(st) < 13 and 0 < int(st2) < 32:
                return True
    else:
        raise ValueError("The imputed personal numeric code is not written correctly.")
