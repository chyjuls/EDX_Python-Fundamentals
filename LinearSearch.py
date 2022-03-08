# Write a function called linear() that takes two parameters
# - a list of strings and a string. Write this function so
# that it returns the first index at which the string is
# found within the list if the string is found, or False if
# it is not found. You do not need to worry about searching
# for the search string inside the individual strings within
# the list: for example, linear(["bobby", "fred"], "bob")
# should return False, but linear(["bob", "fred"], "bob")
# should return 0.
#
# Use a linear search algorithm (not as scary as it sounds).
# Do not use the list method index -- in this exercise,
# you're actually implementing the way the index method
# works!


# Write your code here!
def linear(a_list, a_string):
    for i in range(len(a_list)):
        if a_list[i] == a_string:
            return i
    return False


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 3
a_list = [5, 1, 3, 6, 7, 3, 1, 6, 7, 8, 3, 6]
print(linear(a_list, 6))
print()


# Write a function called search_for_string() that takes two
# parameters, a list of strings, and a string. This function
# should return a list of all the indices at which the
# string is found within the list.
#
# You may assume that you do not need to search inside the
# items in the list; for examples:
#
#  search_for_string(["bob", "burgers", "tina", "bob"], "bob")
#      -> [0,3]
#  search_for_string(["bob", "burgers", "tina", "bob"], "bae")
#      -> []
#  search_for_string(["bob", "bobby", "bob"])
#      -> [0, 2]
#
# Use a linear search algorithm to achieve this. Do not
# use the list method index.
#
# Recall also that one benefit of Python's general leniency
# with types is that algorithms written for integers easily
# work for strings. In writing search_for_string(), make sure
# it will work on integers as well -- we'll test it on
# both.


# Write your code here!
def search_for_string(a_list, a_string):
    new_list = []
    for i in range(len(a_list)):
        if a_list[i] == a_string:
            new_list.append(i)
    return new_list


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: [1, 4, 5]
sample_list = ["artichoke", "turnip", "tomato", "potato", "turnip", "turnip", "artichoke"]
print(search_for_string(sample_list, "turnip"))
