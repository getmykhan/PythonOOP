#Python Object Oriented Programming

class Emp:

    age_tracker = 0
    age_increase = 1
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

        if self.age > 30:
            Emp.age_tracker += 1

    def fullname(self):
        return("{} {}".format(self.fname, self.lname))

    def increment(self):
        self.age = int(self.age + self.age_increase)

employee_one = Emp('Mike', 'Tyson', 44)

Emp.increment(employee_one)


employee_two = Emp('Lalo', 'Lola', 27)


print(employee_two.__dict__)

employee_two.increment()

employee_one.age_increase = 2
print(employee_one.age_increase)
Emp.age_increase = 3
print(employee_one.age_increase)


print('*' * 100)
print('*' * 100)
print('*' * 100)


print(Emp.age_tracker)
