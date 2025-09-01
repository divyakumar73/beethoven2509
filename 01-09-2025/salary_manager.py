salaries = []
# CRUD - create, read all, read by ID, update, delete, read by salary
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



create_salary(100)
create_salary(8899)
create_salary(88999)

result_salaries = read_all()
for salary in result_salaries:
    print(salary)

print(read_by_salary(8899))
print(read_by_salary(88999))
print(read_by_salary(100))

update(8899, 96666)
print(read_all())
remove_by_salary(100)
print(read_all())
