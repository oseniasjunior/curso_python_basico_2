from actions import add_employee, obtains_employees
from models import Employee

DATABASE = '/tmp/employees.txt'


def main():
    option = 1

    while option != 0:
        print('1 - Add Employee')
        print('2 - List Employee')
        print('0 - Exit')
        option = int(input('Input your choice: '))

        if option == 1:
            employee = Employee(
                id=int(input('Id: ')),
                name=input('Name: '),
                gender=input('Gender: '),
                salary=input('Salary: '),
                date_birth=input('Date birth: ')
            )
            add_employee(path_file=DATABASE, employee=employee)
        elif option == 2:
            employees = obtains_employees(DATABASE)
            for e in employees:
                print('Employee: {}'.format(e))
                print("""
                    Id: {}
                    Name: {}
                    Gender: {}
                    Salary: {}
                    Date birth: {}
                    Age: {}
                    ---------------------------
               """.format(e.id, e.name, e.gender, e.salary, e.date_birth, e.age))


main()
