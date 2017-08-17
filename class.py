class Emp:

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age


employee_one = Emp('Mike', 'Tyson', 44)

print(employee_one.fname)
