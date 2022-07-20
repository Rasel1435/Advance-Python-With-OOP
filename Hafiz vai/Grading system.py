## Grading System
# Take input of Marks
# Calculate average
# AA(90-100), A+(80-89), A(60-79), B(45-59), C(30-44), D(0-29)


result = int(input("Enter Your Number: "))


if result >= 90 and result <= 100:
    print("AA")
elif result >= 80 and result <= 89:
    print("A+")
elif result >= 60 and result <= 79:
    print("A")
elif result >= 45 and result <= 59:
    print("B")
elif result >= 30 and result <= 44:
    print("C")
elif result >= 0 and result <= 29:
    print("D")
else:
    print("Invalid Number")