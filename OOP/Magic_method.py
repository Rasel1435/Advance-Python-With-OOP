class Employee:
    increment = []
    no_of_employee = 0

    def __init__(self, fname, lname, salary, age):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.age = age
        Employee.no_of_employee += 1

    def increase(self):
        self.salary = (self.salary * self.increment)

    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount

    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salay, age = emp_string.split("-")
        return cls(fname, lname, salay, age)

    @staticmethod
    def is_off(day):
        if day == "Friday":
            return True
        else:
            return False

    # __add__ this is the Magic method or dunder method which is __add__,__mull__,__div__,__sub__ work with two object string
    def __add__(self, other):
        return self.salary + other.salary
    # This magic method will show our all info

    def __repr__(self):
        return 'Employee ({}, {}, {}, {})'.format(self.fname, self.lname, self.salary, self.age)

    def __str__(self):
        return "The Name of Employee Is {}".format(self.fname)


Rasel = Employee("Rasel", "Ahmed", 120000, 27)
Liza = Employee("Rasel", "Ahmed", 10, 26)

# print(Rasel + Liza)
print(str(Rasel))
