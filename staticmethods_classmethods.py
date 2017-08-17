#Python Object Oriented Programming
import datetime
class Emp:

    age_tracker = 0
    age_increase = 1
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

        Emp.age_tracker += 1

    def fullname(self):
        return("{} {}".format(self.fname, self.lname))

    def increment(self):
        self.age = int(self.age + self.age_increase)

    @classmethod

    def self_age_increase(cls, age_to_increase_by):
        cls.age_increase = age_to_increase_by

    @classmethod
    def employee_string(cls, emp_str):
        first, last, age = emp_str.split('-')
        return cls(first, last, age)

    @staticmethod
    def _isworkdat(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True

employee_one = Emp('Mike', 'Tyson', 44)
employee_two = Emp('Lalo', 'Lola', 27)

Emp.self_age_increase(5)

Employee_details = input("Enter the Employee details seperated by a -")

new_Employee_details = Emp.employee_string(Employee_details)

print(new_Employee_details.age)
my_date = datetime.date(2016, 7, 12)

print(Emp._isworkdat(my_date))
