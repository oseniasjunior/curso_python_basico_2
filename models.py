from datetime import datetime
import actions


class Employee:
    def __init__(self, id, name, gender, salary, date_birth):
        self.id = id
        self.name = name
        self.gender = gender
        self.salary = salary
        self.date_birth = date_birth

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)

    @property
    def age(self):
        now = datetime.now().date()
        diff = now - actions.str_to_date(self.date_birth)
        return (diff / 365).days
