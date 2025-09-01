from salary_manager import create_salary, read_all, read_by_salary
from  salary_manager import salaries, update, remove_by_salary
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
