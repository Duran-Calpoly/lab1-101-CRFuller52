def check_multiple(number):
    if ((number%3==0) and (number%5==0)):
        return True
    else:
        return False
def check_password(input_string):
    if input_string== "football":
        return ("access granted")
    elif input_string!="football":
        return ("access denied")
def calculate_federal_tax(salary):
    if salary<=11000:
        return (salary*.10)
    elif salary>11000 and salary<=44725:
        return (salary*.12)
    elif salary>44725 and salary<=95375:
        return (salary*.22)
    else:
        return (salary*.24)

        