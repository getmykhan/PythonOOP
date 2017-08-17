#Python Object Oriented Programming

class Emp:

    age_increase = 1
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def fullname(self):
        return("{} {}".format(self.fname, self.lname))

    def increment(self):
        self.age = int(self.age + self.age_increase)

employee_one = Emp('Mike', 'Tyson', 44)

print(employee_one.age)
Emp.increment(employee_one)
print(employee_one.age)

employee_two = Emp('Lalo', 'Lola', 27)

print('*' * 100)
print('*' * 100)
print('*' * 100)

print(employee_two.age_increase + employee_two.age_increase)
print(employee_two.__dict__)


employee_two.increment()

print(employee_two.age)
