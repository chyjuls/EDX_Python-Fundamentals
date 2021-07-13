# Using number range as lists in python and combining it with for and if.

for x in range(100):
    print(x)

Even_Numbers = [x for x in range(50) if x % 2 == 0]
print(Even_Numbers)

Odd_Numbers = [x for x in range(50) if x % 2 == 1]
print(Odd_Numbers)

