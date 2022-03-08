# TUPLES ARE IMMUTABLE, THAT IS CAN NOT BE CHANGED.

# Write a function called string_length. string_length should
# have one parameter, a string. It should return a 2-tuple:
# the first item in the 2-tuple should be the string itself,
# and the second item should be the length of the string as
# given by the len() function.


# Write your function here!


def string_length(num_string):
    my_tuple = (num_string, len(num_string))
    return my_tuple


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# ('Hello, world!', 13)
# ('CS1301', 6)
# ("Some people pronounce it 'toople'. Others pronounce it 'tuhple'. Either is correct.", 83)
print(string_length("Hello, world!"))
print(string_length("CS1301"))
print(string_length("Some people pronounce it 'toople'. Others pronounce it 'tuhple'. Either is correct."))
print()


# Write a function called unpack_and_reverse that will
# accept one parameter, a tuple with at least three items.
# The function should return a new tuple with only the first
# three items, but listed in reverse order.
#
# For example:
#
# a_tuple = ("a", "b", "c", "d", "e")
# unpack_and_reverse(a_tuple) -> ("c", "b", "a")
#
# However, to do this, you should not access any value in
# the tuple directly (e.g. with a_tuple[1]). Instead, you
# should use tuple unpacking to unpack them into variables.
# You also should not touch any items past the third item
# in the tuple: use tuple slicing instead to only access
# the first three.


# Write your function here!
def unpack_and_reverse(myTuple_1):
    (str1, str2, str3) = myTuple_1[:3]
    new_tuple = (str3, str2, str1)
    return new_tuple


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# ('c', 'b', 'a')
# ('h', 'g', 'f')
# ('k', 'j', 'i')
print(unpack_and_reverse(("a", "b", "c", "d", "e")))
print(unpack_and_reverse(("f", "g", "h")))
print(unpack_and_reverse(("i", "j", "k", "l", "m", "n", "o", "p", "q", "r")))
print()


# Remember asciitable.com from an earlier exercise? We're
# going to use it again. Remember, ordinal values for
# characters are given in the 'Dec' column of asciitable.com.
#
# Write a function called character_info. character_info will
# take as input a string with only one character. It should
# return a 3-tuple with three pieces of information:
#
# - In the first spot, the character itself.
# - In the second spot, the ordinal value of the character,
#   obtained using the ord() function (e.g. ord("a") -> 97).
# - In the third spot, what type of character it is: either
#   "letter", "number", or "punctuation".
#
# You may assume that anything that is not a letter (either
# upper or lower case) or a number is punctuation. You may
# also assume the ordinal will be between 32 (" ") and 126
# ("~").


# Write your function here!
def character_info(a_string):
    my_new_tuple = ()
    ch_type = "number" if ord(a_string) in range(48, 58) else "letter" if ord(a_string) in range(65, 91) or ord(
        a_string) in range(97, 123) else "punctuation"
    my_new_tuple = (a_string, ord(a_string), ch_type)
    return my_new_tuple


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# ('q', 113, 'letter')
# ('7', 55, 'number')
# ('`', 96, 'punctuation')
print(character_info("q"))
print(character_info("7"))
print(character_info("`"))
print()

my_list = ["A", "B", "C", "D", "E"]
my_list[2] = my_list[4]
my_list[4] = "Z"
print(my_list)
print()
my_list1 = [1, 2, 3, -2, 0]
my_list2 = [-4, -7, -6]
my_list1.extend(my_list2)
print(my_list1)
print()


# Write a function called modify_list. modify_list will
# take one parameter, a list. It should then modify the
# list in the following ways, in this order:
#
# - Sort the list (using the default sort method).
# - Reverse the order of the list.
# - Delete the last three items of the list.
# - Removes one instance the integer 7 from the list, if
#   it's present.
# - Double the values of the first and third items in
#   the list.
#
# It should then return the resulting list. You may assume
# the list will start with at least six items.
#
# Hint: Remember Python is 0-indexed. The second item
# does not have an index of 2.
#
# Hint 2: Remember, the list.remove() function removes items
# by value, not by index. Note also that if the item you're
# trying to remove is not found in the list, remove() will
# throw an error: so, you'll want to avoid that one way or
# another!


# Write your code here!

def modify_list(myList):
    myList.sort()
    myList.reverse()
    # myList = [x * 2 for x in myList]
    del myList[-3:]
    try:
        myList.remove(7)
    except:
        ValueError
    myList[0] *= 2
    myList[2] *= 2
    return myList


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# [178, 81, 75.0, 4, 3.141592653589793, 3]
import math

print(modify_list([7, 4, 3, 2.0, 81, 37.5, 89, math.pi, -2, math.e]))

print()


def modify_list(my_list):
    my_list.sort()
    my_list.reverse()
    del my_list[-3:]
    try:
        my_list.remove(7)
    except:
        ValueError
    my_list[0] *= 2
    my_list[2] *= 2
    return my_list


import math

print(modify_list([7, 4, 3, 2.0, 81, 37.5, 89, math.pi, -2, math.e]))
print()


# Write a function called multiply_strings. Multiply
# strings should have one parameter, a list of strings.
# It should return a modified list according to the
# following changes:
#
# - Every string stored at an even index should be
#   doubled.
# - Every string stored at an index that is a multiple
#   of 3 should be tripled.
# - Every other string should remain unchanged.
#
# These changes should "stack": the string stored at index
# 6 should be duplicated six times (2 * 3).
#
# Then, return the new list. You may assume that 0 is a
# multiple of 2 and 3.
#
# Hint: To do this, you need to modify the values of the
# list using their indices, e.g. a_list[1]. If you're not
# using their indices, your answer won't work!


# Write your function here!
def multiply_strings(a_list):
    for a_string in range(0, len(a_list)):
        if a_string % 2 == 0:
            a_list[a_string] *= 2
        if a_string % 3 == 0:
            a_list[a_string] *= 3

    return a_list


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# ['AAAAAA', 'B', 'CC', 'DDD', 'EE', 'F', 'GGGGGG']
test_list = ["A", "B", "C", "D", "E", "F", "G"]
print(multiply_strings(test_list))
print()

myList = [[3, 4, 5],
          [4, 5, 6],
          [5, 6, 7]]


def mystery(a2DList):
    result = []
    for alist in a2DList:
        value = 0
        for item in alist:
            value += item

        value *= 2

        result.append(value)
    return result


print(mystery(myList))
print()


# Write a function called sum_lists. sum_lists should take
# one parameter, which will be a list of lists of integers.
# sum_lists should return the sum of adding every number from
# every list.
#
# For example:
#
# list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# sum_list(list_of_lists) -> 67


# Add your code here!
def sum_lists(a2Dlist):
    sum = 0
    for a_list in a2Dlist:
        for num in a_list:
            sum += num
    return sum
    # result = sum([sum(i) for i in a2Dlist])
    # return result


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 78
list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(sum_lists(list_of_lists))

print()
new_list = [10, 20, 30, 40, 50]
sum = 0
for v in new_list:
    sum = sum + v
print(sum / len(new_list))

a = 8
b = 3
c = 2
myTuple = a, b, c
print(myTuple)

print()


