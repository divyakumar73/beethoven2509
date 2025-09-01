from salary_manager import create_salary, read_all, read_by_salary
from salary_manager import salaries, update, remove_by_salary


def menu():
    message = '''


1 - Crate Salary
2 - Read All Salaries 
3 - Read By Salary 
4 - Update 
5 - Delete 
6 - Exit/ Logout 
'''
    choice = int(input(message))
    if choice == 1:
        salary = int(input('Salary:'))
        create_salary(salary)
    elif choice == 2:
        result_salaries = read_all()
        print('salaries:')
        for salary in result_salaries:
            print(salary)
    elif choice == 3:
        salary = int(input('Search  Salary:'))
        index = read_by_salary(salary)
        if salary == -1:
            print('Salary not found')
        else:
            print(f'Salary is at index {index}')
    elif choice == 4:
        old_salary = int(input(' Salary to update:'))
        new_salary = int(input('New Salary:'))
        update(salary, new_salary)



    elif choice == 5:
        salary = int(input('Salary to delete:'))
        remove_by_salary(salary)
    return choice
def menus():
    print('Salary Mnaagement App')
    choice = menu()
    while choice != 6:
        choice = menu ()
    print('Thank You for using app')
menus()