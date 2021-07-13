mystery_int = 5

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# In math, factorial is a mathematical operation where an
# integer is multipled by every number between itself and 1.
# For example, 5 factorial is 5 * 4 * 3 * 2 * 1, or 120.
# Factorial is represented by an exclamation point: 5!
#
# Use a for loop to calculate the factorial of the number
# given by mystery_int above. Then, print the result.
#
# Hint: Running a loop from 1 to mystery_int will give you
# all the integers you need to multiply together. You'll need
# to track the total product using a variable declared before
# starting the loop, though!


# Add your code here!


factorial = 1
if mystery_int >= 1:
    for i in range(1, mystery_int + 1):
        factorial = factorial * i
    print(factorial)
a_string = "Indices! Yay!"
a_character = a_string[3]
print("The character is", a_character)

some_range = range(5, 10)
print(some_range[0])
print(some_range[4])

some_string = "Georgia Tech"
print(some_string[0])
print(some_string[8])
print()

some_list = ["I", "like", "shorts", "they're", "comfy", "and", "easy", "to", "wear"]
print(some_list[0])
print(some_list[4])
print()
for i in range(5, 9):
    print("Index", i)
print()

some_string = "Georgia Tech"
for i in range(0, len(some_string)):
    print(i, some_string[i])
print()

some_list = ["I", "like", "shorts", "they're", "comfy", "and", "easy", "to", "wear"]
for i in range(0, len(some_list)):
    print(i, some_list[i])
print()
sum = 0
new_list = [23, 67, 98, 45, 32, 48, 90,]
for new_number in new_list:
    sum += new_number
print(sum / len(new_list))
print()

for i in range(0, len(new_list)):
    new_number = new_list[i]
    print(new_number)
    sum *= new_number
print(sum / len(new_list))
print()

num_spaces = 0
my_word_list = "This is my name"
for word in my_word_list:
    if word == " ":
        num_spaces += 1
print("There are are " + str(num_spaces + 1) + " spaces in the string")

mystery_string = "CS1301"

# Write a for-each loop that lists each character in
# mystery_string with its index. For example, if the string
# was "David", the output would be:
# 0 D
# 1 a
# 2 v
# 3 i
# 4 d
#
# Note that the first item is #0, the second is #1, and so
# on! We'll talk about why that is in Unit 4.
#
# Hint: You'll need a separate variable to keep track of how
# many letters you've printed! You may not use the range
# function on this problem.


# Add your code here!
num = -2

for letter in mystery_string:
    if letter >= "":
        num += 1
    print (str(num + 1), letter)
# or

num = 0
for letter in mystery_string:
    num +=1
print(num, letter)
print()

