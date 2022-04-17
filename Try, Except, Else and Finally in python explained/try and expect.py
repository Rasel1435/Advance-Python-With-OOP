try:
    print("Hey There")
except Exception as e:
    print(e)
else:
    print("There is no exception")

############

try:
    file = open("this.txt", "r")
except EOFError as e:
    print("eof error")
except IOError as e:
    print("we can handle this error")
finally:
    print("This will be printed irrespective of the expception occurrence")
