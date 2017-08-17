#Python Object Oriented Programming
class Emp:

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def fullname(self):
        return("{} {}".format(self.fname, self.lname))

    def increment(self):
        self.age = float(self.age * 1.04)

employee_one = Emp('Mike', 'Tyson', 44)

print(employee_one.fname)

employee_two = Emp('Lalo', 'Lola', 27)

print(employee_two.fname + employee_two.lname)

print('Both their ages put together is: ', employee_one.age + employee_two.age)

print(employee_two.fullname())

print("*" * 100)

print(employee_one.age)
employee_one.increment()
print(employee_one.age)
