# List Comprehension, 
# Dictionary Comprehension
# And Generator Comprehension

list = [1,32,34,5,6,45,6,3,7,88,97,2,3,2,1,55,8]
divided_by_3 = []
for i in list:
    if i%3 == 0:
        divided_by_3.append(i)
print("Without using list comprehension", divided_by_3)

print("Using List comprehenshion", [i for i in list if i%3 == 0])

# Dictionary Comprehension

dict1 = {"a": 45, "b":95,"A":50}
print({k.lower():dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1.keys()})

# set comprehension
set1 = {x**2 for x in [1,2,3,4,4,4,4,5,5,5,5]}
print(set1)

# And Generator Comprehension
gen = (i for i in range(56) if i%3 == 0)
for i in gen:
    print(i)
    