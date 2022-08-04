class Employee:
    # Constructors
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary


# Objects
Rasel = Employee("Sheikh Rasel", "Ahmed", 1000000)
Liza = Employee("Adv", "Liza", 90000)

# Output
print(Rasel.fname, Liza.fname)

# Documentaions:
# def mean function and
# __init__ mean Constructors keep in mind
