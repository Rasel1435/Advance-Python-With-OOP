class Employee:
    increment = []
    no_of_employee = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employee += 1

    def increase(self):
        self.increment = (self.salary * self.increment)

    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount

    @classmethod
    def from_str(cls, cmp_string):
        fname, lname, salary = cmp_string.split("-")
        return cls(fname, lname, salary)

    @staticmethod  # when Class variable or instance variable doesnt work that moment we use static function
    def is_open(day):
        if day == "Sunday":
            # return True
            print("Office Day")
        else:
            print('Off day')


Nirob = Employee("Nirob", "Ahmed", 85000)
print(Nirob.is_open("Sunday"))


# Rasel = Employee("Rasel", "Ahmed", 70000)
# Love = Employee.from_str("Love-chiled-150000")
# Liza = Employee("Adv", "Liza", 80000)
# print(Love.salary)
# print(Rasel.salary)
# Employee.change_increment(2)
# Rasel.increase()
# print(Rasel.salary)
# print(Liza.salary)
