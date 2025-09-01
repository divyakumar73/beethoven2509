salaries = []
def create_salary(salary):
    global salaries
    # firstSalary=7000
    salaries.append(salary)
def read_all():
    return salaries

def read_by_salary(salary): #return first occurance index of salary
    for i in range(len(salaries)):
        if salaries[i] == salary:
            return i
    return -1


def update(old_salary, new_salary):
    global salaries
    index = read_by_salary(old_salary)
    salaries[index]= new_salary

def remove_by_salary(salary):
    global salaries 
    index = read_by_salary(salary)
    salaries.pop(index)