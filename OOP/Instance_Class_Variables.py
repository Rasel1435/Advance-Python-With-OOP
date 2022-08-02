from numpy import number


class Employee:
    # Constructors
    increment = 1.5  # Class instance variables
    no_of_employee = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 1.4  # this is instance variables
        # if there is * self.increment function then it will call first then if there is not then it will call class instance variables
        Employee.no_of_employee += 1

    def increase(self):
        self.salary = int(self.salary * self.increment)


# Objects
print(Employee.no_of_employee)
Rasel = Employee("Sheikh Rasel", "Ahmed", 100)
print(Employee.no_of_employee)
Liza = Employee("Adv", "Liza", 90000)
print(Employee.no_of_employee)

# Output
print(Rasel.salary)
Rasel.increase()
print(Rasel.salary)

# if we want to see our all variables
print(Rasel.__dict__)
# print(Employee.__dict__)
# print(Rasel.fname, Liza.fname)
