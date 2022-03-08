i = 1
while i < 11:
    print(i)
    i += 1

my_counter = 5

print()
while my_counter > 0:
    my_counter -= 1
    print(my_counter)

print()

mystery_value = 87

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Write a while loop that continues to add 9 to mystery_value
# until mystery_value is greater than 100. Each time 9 is
# added, print the *new* value of mystery_value. For example,
# with mystery_value = 87, your code should print 96 and 105.


# Add your code here!

while mystery_value <= 100:
    mystery_value += 9
    print(mystery_value)
print()

mystery_int_1 = 3
mystery_int_2 = 4
mystery_int_3 = 5

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Above are three values. Run a while loop until all three
# values are less than or equal to 0. Every time you change
# the value of the three variables, print out their new values
# all on the same line, separated by single spaces. For
# example, if their values were 3, 4, and 5 respectively, your
# code would print:
#
# 2 3 4
# 1 2 3
# 0 1 2
# -1 0 1
# -2 -1 0


# Add your code here!

while not (mystery_int_1 <= 0 and mystery_int_2 <= 0 and mystery_int_3 <= 0):
    mystery_int_1 -= 1
    mystery_int_2 -= 1
    mystery_int_3 -= 1
    print(mystery_int_1, mystery_int_2, mystery_int_3)
# another method:
print()
while mystery_int_1 > 0 or mystery_int_2 > 0 or mystery_int_3 > 0:
    mystery_int_1 -= 1
    mystery_int_2 -= 1
    mystery_int_3 -= 1
    print(mystery_int_1, mystery_int_2, mystery_int_3)

# mystery_values = [mystery_int_1, mystery_int_2, mystery_int_3]
# i = -3

# while i not in mystery_values:
# print(*mystery_values, sep=" ")
# mystery_values[0] -= 1
# mystery_values[1] -= 1
# mystery_values[2] -= 1
print()
num = 5
result = 1
for i in range(num):
    result *= i
print(result)

print()

num = 5
result = 1
for i in range(num):
    i += 1
    result *= i

print(result)
print()

count = 0
for x in range(3):
    for x in range(3):
        count = count + x
print(count)

list1 = ["Alison", "Mina", "Leticia", "Elaine", "Sonny", "Benito"]
list2 = ["Yuri", "Andrew", "Mina", "Elaine", "Charles", "Alison"]
for name1 in list1:
    for name2 in list2:
        if name1 == name2:
            print(name1)
print()

# find factorial using while loop:

num = 6


def Fact(num):
    fact = i = 1
    while i <= num:
        fact = i * fact
        i += 1
    return fact


print(Fact(num))
