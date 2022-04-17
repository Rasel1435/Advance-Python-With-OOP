# *args and **kwargs
# *vars and **kvars

def function_1(*args):
    print(type(args))
    if(len(args) == 3):
        print(f"The name of the student is {args[0]} and age is {args[1]} and rollno is {args[2]}")

    else:
        print(f"The name of the student is {args[0]} and age is {args[1]}")

lis = ("Sheikh Rasel Ahmed",27,4245 )

def printmarsk(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)


markslist = {"Rasel : ": 75,"Rohan : ": 100, "Sumaya : ": 80}

def master(normal, *args, **kwargs):
    print(normal)
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(key, value)

master("normal args", *lis, **markslist)