from distutils.command.config import LANG_EXT
from fnmatch import fnmatch


class Employee:
    increment = []
    no_of_employee = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.laname = lname
        self.salary = salary
        Employee.no_of_employee += 1

    def increase(self):
        self.salary = (self.salary * self.increment)

    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount

    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)


Rasel = Employee("Rasel", "Ahmed", 70000)
Love = Employee.from_str("Love-chiled-150000")
Liza = Employee("Adv", "Liza", 80000)

print(Love.salary)
# print(Rasel.salary)
# Employee.change_increment(2)
# Rasel.increase()
# print(Rasel.salary)
# print(Liza.salary)
