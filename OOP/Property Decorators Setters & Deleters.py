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

    @property  # When we use this decorator no need to call function with object like email()
    def email(self):
        if self.fname == None:
            return 'Email Not Set'
        else:
            return self.fname + '.' + self.lname + '@gmail.com'

    @email.setter
    def email(self, given_email):
        name_list = given_email.split('@')[0].split('.')
        # print(name_list)
        self.fname = [0]
        self.lname = [1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

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


if __name__ == '__main__':

    Rasel = Employee("Rasel", "Ahmed", 120000, 27)
    Liza = Employee("Adv", "Liza", 10, 26)

    print(Rasel.email, Liza.email)
    Rasel.lname = "Sheikh"
    print(Rasel.email)
    Rasel.email = 'sheikhrase@gmail.com'
    print(Rasel.email)
    del Rasel.email
    print(Rasel.email)
