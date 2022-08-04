from typing_extensions import Self

from Classes_Objects_Constructors import Liza


class Employee:
    # Constactors
    increment = []
    no_of_employee = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.no_of_employee += 1

    def increase(self):
        self.salary = (self.salary * self.increment)

# Class Method
    @classmethod  # Decorator
    def change_increment(cls, amount):
        cls.increment = amount


# object
Rasel = Employee("Rasel", 27, 50000)
Liza = Employee("Liza", 26, 60000)

# OutPut
print(Rasel.salary)
Employee.change_increment(2)
Rasel.increase()
print(Rasel.salary)
print(Liza.salary)
