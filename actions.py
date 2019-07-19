from models import Employee
from typing import List
from datetime import date


def str_to_date(date_as_str):
    year = int(date_as_str.split('-')[0])
    month = int(date_as_str.split('-')[1])
    day = int(date_as_str.split('-')[2])
    return date(year=year, month=month, day=day)


def transform_in_line(employee: Employee):
    return '{id};{name};{gender};{salary};{date_birth};\n'.format(
        id=employee.id,
        name=employee.name,
        gender=employee.gender,
        salary=employee.salary,
        date_birth=employee.date_birth
    )


def transform_in_employee(line: str) -> Employee:
    keys = ['id', 'name', 'gender', 'salary', 'date_birth']
    columns = line.split(';')
    employee_as_dict = dict(zip(keys, columns))
    return Employee(**employee_as_dict)


def add_employee(path_file, employee: Employee):
    reference_file = open(path_file, 'a')
    reference_file.write(transform_in_line(employee=employee))
    reference_file.close()


def obtains_employees(path_file) -> List['Employee']:
    employees = []
    reference_file = open(path_file, 'r')
    lines = reference_file.readlines()
    for line in lines:
        employees.append(transform_in_employee(line=line))
    return employees
