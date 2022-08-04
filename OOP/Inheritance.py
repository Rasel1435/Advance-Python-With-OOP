from unicodedata import name


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
        self.salary = int(self.salary * self.increment)

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


class Programmer(Employee):
    def __init__(self, fname, lname, salary, age, proglang, exp):
        super().__init__(fname, lname, salary, age)
        self.proglang = proglang
        self.exp = exp

    def increase(self):
        self.salary = int(self.salary * (self.increment + 2))


Rasel = Programmer("Rasel", "Ahmed", 120000, 27, "Python", 3)

# print(Rasel.salary)
# Rasel.increase()
# print(Rasel.salary)
# print(help(Programmer))
