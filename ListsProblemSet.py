my_2D_tuple = ((1, 2, 3),
               (4, 5, 6),
               (7, 8, 9))

for a_tuple in my_2D_tuple:
    total = 0
    for num in a_tuple:
        total += num
    print(total)
print()


# Write a function called multiply_by_index. multiply_by_index
# should have one parameter, a list; you may assume every item
# in the list will be an integer. multiply_by_index should
# return a list where each number in the original list is
# multipled by the index at which it appeared.
#
# For example:
#
# multiply_by_index([1, 2, 3, 4, 5]) -> [0, 2, 6, 12, 20]
#
# In the example above, the numbers 1, 2, 3, 4, and 5 appear
# at indices 0, 1, 2, 3, and 4. 1*0 = 0, 2 * 1 = 2, 3 * 2 = 6,
# and so on.


# Write your code here!
def multiply_by_index(myList):
    myNewList = []
    for num in range(len(myList)):
        result = myList[num] * num
        myNewList.append(result)
    return myNewList


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# [0, 2, 6, 12, 20]
# [0, 7, 14, 21, 28, 35, 42]
# [0, 7, 74, 195, 36, 0, 330]
print(multiply_by_index([1, 2, 3, 4, 5]))
print(multiply_by_index([7, 7, 7, 7, 7, 7, 7]))
print(multiply_by_index([14, 7, 37, 65, 9, 0, 55]))
print()


# Write a function, called lucky_sevens, that takes in one
# parameter, a list of integers, and returns True if the list
# has three '7's  in a row and False if the list doesn't.
#
# For example:
#
#  lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]) -> True
#  lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]) -> False
#
# Hint: As soon as you find one instance of three sevens, you
# could go ahead and return True -- you only have to find it
# once for it to be True! Then, if you get to the end of the
# function and haven't returned True yet, then you might
# want to return False.


# Write your function here!
def lucky_sevens(my_three_sevens):
    for i in range(len(my_three_sevens)):

        if my_three_sevens[i] == 7:
            count += 1
        else:
            count = 0
        if count == 3:
            return True
    return False


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: True, then False
print(lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]))
print(lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]))
print()


# Another method:

def lucky_sevens(a_list):
    # The goal of using a for loop is to give us access to the
    # indices of each item in the list. There are three
    # consecutive 7s in the list if the current item is 7, the
    # next item is 7, and the one after it is 7. So, if we use
    # a for loop, we can check all three indices.
    #
    # First, we iterate over each character in the list:

    for i in range(len(a_list) - 2):

        # Note that we stop two characters from the end. Why?
        # Well, if we haven't found three consecutive 7s by
        # the time we get to the second-to-last item, then
        # we're not going to: there can't be three straight 7s
        # in the last two items. Plus, if we try to check the
        # next item when we're already checking the last item,
        # an error will arise.
        #
        # Next, we could use an and statement, or some nested
        # conditions. Let's do the latter. First we ask, is the
        # current character a 7?

        if a_list[i] == 7:

            # If it was, is the next character a 7?

            if a_list[i + 1] == 7:

                # If it was, is the character *after* that a 7?

                if a_list[i + 2] == 7:
                    # If so, we're done! We found three straight
                    # 7s!

                    return True

    # Then, the only way we reach the line below is if we never
    # returned True above. So, if we reach the end of that loop
    # and haven't exited the function, then we didn't find three
    # straight 7s:

    return False


# What about with a for-each loop? Check out sample_answer_2.py to
# see!

print(lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]))
print(lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]))
print()


# Write a function called attendance_check. attendance_check
# should have two parameters: roster and present. Both roster
# and present will be lists of strings. Return a list (sorted
# alphabetically) of all strings in the list roster that are
# not in the list present. In other words, if roster is a
# list of students enrolled in a class and present is a list
# of students in class today, return a list of students that
# are absent.
#
# You may assume that every item in each list will be a
# string. You may also assume that every name in the list
# present will be in the list roster. If no students are
# absent, return an empty list.


# Write your function here!

def attendance_check(roster, present):
    absent = [name for name in roster if name not in present]

    return sorted(absent, reverse=False)


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# ['Ferguson', 'Winston']
test_roster = ['Jessica', 'Nick', 'Winston', 'Schmidt', 'Cece', 'Ferguson']
test_present = ['Nick', 'Cece', 'Schmidt', 'Jessica']
print(attendance_check(test_roster, test_present))
print()


# Write a function called grade_scantron. grade_scantron should
# take as input two lists: answers and key. Each list contain
# strings. Each string will be only one letter, a character
# from A to E. grade_scantron should return how many questions
# the student got "right", where a student gets a question
# right if their answer for a problem matches the answer key.
#
# In other words, if value of the first item in answers matches
# the value of the first item in key, the student gets a point.
# If it does not, the student does not get a point.
#
# If the lists do not have the same number of items, return
# -1 to indicate that the answer key did not belong to the
# same test as the student's answers.\
#
# Hint: in the past, lots of people have tried to do this using
# the index() method. That won't work! You'll need to track the
# index yourself.


# Write your function here!
def grade_scantron(answers, key):
    if not len(answers) == len(key):
        return -1

    score = 0  # like counter

    for i in range(len(answers)):

        if answers[i] == key[i]:
            score += 1

    # Then, after we're done (note the lack of indentation),
    # return the score:

    return score


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 7
test_answers = ["A", "B", "B", "A", "D", "A", "B", "A", "E"]
test_key = ["A", "B", "B", "A", "D", "E", "B", "A", "D"]
print(grade_scantron(test_answers, test_key))


def grade_scantron(answers, key):  # returns total unique matching alphabeths
    score = set(answers) & set(key)
    return len(score)


test_answers = ["A", "B", "B", "A", "D", "A", "B", "A", "E"]
test_key = ["A", "B", "B", "A", "D", "E", "B", "A", "D"]
print(grade_scantron(test_answers, test_key))
print()

# Write a function called solve_right_triangle. The function
# solve_right_triangle should have three parameters: opposite,
# adjacent, and use_degrees. opposite and adjacent will be
# floats, and use_degrees will be a boolean. use_degrees
# should be a keyword parameter, and it should have a
# default value of False.
#
# The function should return a tuple containing the
# hypotenuse and angle of the right triangle (in that order).
# If use_degrees is False, the angle should be in radians.
# If use_degrees is True, the angle should be in degrees.
#
# Remember, the formula for the hypotenuse of a right
# triangle is the square root of the sum of the squared side
# lengths. You can find arctan using math.atan(), passing in
# the quotient of the opposite and adjacent as the argument.
# By default, math.atan() returns the angle in radians; you
# can pass that angle as an argument into the math.degrees()
# method to convert it to degrees; for example:
#
# angle_in_degrees = math.degrees(angle_in_radians)

import math


# Write your function here!
def solve_right_triangle(opposite, adjacent, use_degrees=False):
    my_degrees_tuple = ()
    my_hypotenuse = math.sqrt(opposite ** 2 + adjacent ** 2)
    my_degrees = math.atan(opposite / adjacent)
    if use_degrees == False:
        my_degrees_tuple = (my_hypotenuse, my_degrees)
        return my_degrees_tuple
    else:
        my_degrees_radian = math.degrees(my_degrees)
        my_degrees_tuple_1 = (my_hypotenuse, my_degrees_radian)
        return my_degrees_tuple_1


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# (5.0, 0.6435011087932844)
# (5.0, 36.86989764584402)
print(solve_right_triangle(3.0, 4.0))
print(solve_right_triangle(3.0, 4.0, use_degrees=True))

print()


# Write a function called find_max_sales. find_max_sales will
# have one parameter: a list of tuples. Each tuple in the
# list will have two items: a string and an integer. The
# string will represent the name of a movie, and the integer
# will represent that movie's total ticket sales (in millions
# of dollars).
#
# The function should return the movie from the list that
# had the most sales. Return only the movie name, not the
# full tuple.


# Write your function here!
def find_max_sales(movie_list):
    movie_name = ""
    movie_tickets = -1  # starts from the very first right?
    for movie_tuple in movie_list:  # for tuple in lists
        if movie_tuple[1] > movie_tickets:  # index movie tuple greater than -1
            movie_tickets = movie_tuple[1]
            movie_name = movie_tuple[0]
    return movie_name


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: Rogue One
movie_list = [("Finding Dory", 486), ("Captain America: Civil War", 408), ("Deadpool", 363), ("Zootopia", 341),
              ("Rogue One", 529), ("The Secret Life of Pets", 368), ("Batman v Superman", 330), ("Sing", 268),
              ("Suicide Squad", 325), ("The Jungle Book", 364)]
print(find_max_sales(movie_list))
print()


# Write a function called wish_list. wish_list should have
# four parameters, in this order:
#
# - a list of strings, representing a list of items on a
#   wish list
# - a string, representing a particular item
# - a float, representing the cost of this item
# - a float, representing your budget
#
# If the item is on the list and you can afford it (cost is
# less than or equal to budget), return the string,
# "You should buy a [item name]!", replacing [item name]
# with the string.
#
# If the item is on the list but you can't afford it,
# return the string, "You should save up for a [item name]!",
# replacing [item name] with the string.
#
# If the item is not on the list, you should return the
# string "You probably don't want to buy a [item name].",
# replacing [item name] with the string.
#
# HINT: You do not need a loop to solve this. You can use
# one, but you don't need one.


# Add your function here!

def wish_list(my_item_list, item, item_cost, my_budget):
    if item_cost <= my_budget and item in my_item_list:
        answer_string = "You should buy a {}!".format(item)
        return answer_string
    elif item_cost > my_budget and item in my_item_list:
        answer_string_2 = "You should save up for a {}!".format(item)
        return answer_string_2
    else:
        return "You probably don't want to buy a {}.".format(item)


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: "You should save up for a bugle!"

wish_list_items = ["bugle", "trumpet", "banjo", "tuba"]
selected_item = "bugle"
item_cost = 199.99
budget = 150.00
print(wish_list(wish_list_items, selected_item, item_cost, budget))
print()


# Imagine you're writing some code for an exercise tracker.
# The tracker measures heart rate, and should display the
# average heart rate from an exercise session.
#
# However, the tracker doesn't automatically know when the
# exercise session began. It assumes the session starts the
# first time it sees a heart rate of 100 or more, and ends
# the first time it sees one under 100.
#
# Write a function called average_heart_rate.
# average_heart_rate should have one parameter, a list of
# integers. These integers represent heart rate measurements
# taken 30 seconds apart. average_heart_rate should return
# the average of all heart rates between the first 100+
# heart rate and the last one. Return this as an integer
# (use floor division when calculating the average).
#
# You may assume that the list will only cross the 100 beats
# per minute threshold once: once it goes above 100 and below
# again, it will not go back above.


# Add your function here!
def average_heart_rate(beats_measurement):
    beats_hundred = [i for i in beats_measurement if i >= 100]
    average_beats = sum(beats_hundred) // len(beats_hundred)
    return average_beats


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print 114 (because there are 14 measurements from 102 to
# 101, their sum is 1609, and 1609 // 14 is 114).
beats = [72, 77, 79, 95, 102, 105, 112, 115, 120, 121, 121,
         125, 125, 123, 119, 115, 105, 101, 96, 92, 90, 85]
print(average_heart_rate(beats))
print()


# Write a function called inside_search. inside_search should
# have two parameters: a list of strings and a string to search
# for. inside_search should return a list of all the indices at
# which the string in the list contains the search string. Note
# that the string at that index does not need to BE the search
# string, but rather must just contain it.
#
# For example:
#
# a_list = ["cat", "cats", "dog", "dogs", "catsup"]
# search_term = "cat"
# inside_search(a_list, search_term) -> [0, 1, 4]
#
# Note that the strings "cat", "cats", and "catsup" all contain
# the search string "cat", and thus the result is their indices:
# [0, 1, 4].
#
# Make sure the list you return is sorted from lowest index to
# highest.


# Add your code here!

def inside_search(a_list, search_string):
    # using list comprehension and enumerate
    new_list = [i for i, s in enumerate(a_list) if search_string in s]
    return new_list


# Below are some lines of code that will test your function.


# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# [0, 1, 4]
# [2, 3]
# [1, 4]
# [4]
# []
cats_and_dogs_list = ["cat", "cats", "dog", "dogs", "catsup"]
print(inside_search(cats_and_dogs_list, "cat"))
print(inside_search(cats_and_dogs_list, "dog"))
print(inside_search(cats_and_dogs_list, "cats"))
print(inside_search(cats_and_dogs_list, "sup"))
print(inside_search(cats_and_dogs_list, "aardvark"))
print()


# You've been sent a list of names. Unfortunately, the names
# come in two different formats:
#
# First Middle Last
# Last, First Middle
#
# You want the entire list to be the same. For this problem,
# we'll say you want the entire list to be Last, First Middle.
#
# Write a function called name_refixer. name_refixer should take
# as input the list of strings. You may assume that every string
# will match one of the two formats above: either First Middle Last
# or Last, First Middle.
#
# name_fixer should return a list of names all structured as
# Last, First Middle. If the name was already structured as
# Last, First Middle, it should remain unchanged. If it was
# structured as First Middle Last, then Last should be moved
# to the beginning and a comma should be added after it.
#
# The names should appear in the same order as the original list.
#
# For example:
#
# name_list = ["David Andrew Joyner", "Hart, Melissa Joan", "Cyrus, Billy Ray"]
# name_fixer(name_list) -> ["Joyner, David Andrew", "Hart, Melissa Joan", "Cyrus, Billy Ray"]


# Add your code here!

def name_refixer(name_list):
    list_2 = []
    for names in name_list:
        if "," not in names:
            my_name = names
            my_name = my_name + ","
            my_name = my_name.split()
            my_name.insert(0, my_name[2])
            # print(my_name)
            my_name.pop()
            # print(my_name)
            new_name = " "
            my_name = new_name.join(my_name)
            # print(my_name)

            list_2.append(my_name)
        elif "," in names:
            list_2.append(names)
    return list_2


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# ["Joyner, David Andrew", "Hart, Melissa Joan", "Cyrus, Billy Ray"]
name_list = ["David Andrew Joyner", "Hart, Melissa Joan", "Cyrus, Billy Ray"]
print(name_refixer(name_list))
print()


# You've been sent a list of names. Unfortunately, the names
# come in two different formats:
#
# First Middle Last
# Last, First Middle
#
# You want the entire list to be the same. For this problem,
# we'll say you want the entire list to be First Middle Last.
#
# Write a function called name_fixer. name_fixer should take
# as input the list of strings. You may assume that every string
# will match one of the two formats above: either First Middle Last
# or Last, First Middle.
#
# name_fixer should return a list of names all structured as
# First Middle Last. If the name was already structured as
# First Middle Last, it should remain unchanged. If it was
# structured as Last, First Middle, then Last should be moved
# to the end after a space and the comma removed.
#
# The names should appear in the same order as the original list.
#
# For example:
#
# name_list = ["David Andrew Joyner", "Hart, Melissa Joan", "Cyrus, Billy Ray"]
# name_fixer(name_list) -> ["David Andrew Joyner", "Melissa Joan Hart", "Billy Ray Cyrus"]


# Add your code here!

def name_fixer(nameList):
    nameList_2 = []
    for name in nameList:

        if "," not in name:
            nameList_2.append(name)
        else:
            name = name.replace(",", "")
            name = name.split(" ")  # split function converts string to a list

            # convert the list back to strings and rearrange using the indices
            name = str(name[1] + " " + name[2] + " " + name[0])

            nameList_2.append(name)
    print (nameList_2)


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# ["David Andrew Joyner", "Melissa Joan Hart", "Billy Ray Cyrus"]
name_list = ["David Andrew Joyner", "Hart, Melissa Joan", "Cyrus, Billy Ray"]
print(name_fixer(name_list))
print()


# Write a function called string_splitter that replicates the
# function of the string type's split() method, assuming that
# we're splitting at spaces. string_splitter should take as
# input a string, and return as output a list of the
# individual words from the string, assuming that words were
# divided by spaces. The spaces themselves should not be in
# the list that your function returns.
#
# You may assume that there will never be more than one space
# in a row, and that the string will neither start nor end
# with a space. However, you should not assume there will
# always be a space.
#
# You may not use Python's built-in split() method.
#
# For example:
#
#  string_splitter("Hello world") -> ['Hello', 'world']


# Write your function here!
def string_splitter(split_string):
    new_string = []
    temp = ''
    for c in split_string:
        if c == ' ':  # if there is space
            new_string.append(temp)
            temp = ''
        else:
            temp += c
    if temp:
        new_string.append(temp)
        return new_string


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: ['Hello', 'world']
print(string_splitter("Hello world"))
print()
# A significant part of introductory physics is calculating
# the net force on an object based on several different
# magnitudes and directions. If you're unfamiliar with how
# this works, we recommend checking out this WikiHow article:
# https://www.wikihow.com/Find-Net-Force
#
# Each force acting on the object is defined by its angle and
# magnitude. The process for calculating net force is:
#
# - For each force, break the force into its horizontal and
#   vertical components. The horizontal component can be
#   calculated as magnitude * cos(angle), and the vertical
#   component can be calculated as magnitude * sin(angle).
# - Sum all the horizontal components to find the total
#   horizontal force, and sum the vertical components to find
#   the total vertical force.
# - Use the Pythagorean theorem to calculate the total
#   magnitude: sqrt(total_horizontal ^ 2 + total_vertical ^ 2)
# - Use inverse tangent to calculate the angle:
#   atan2(total_vertical, total_horizontal)
#
# Write a function called find_net_force. find_net_force should
# take one parameter as input: a list of 2-tuples. Each 2-tuple
# in the list is a (magnitude, angle) pair. angle will be in
# degrees between -180 and 180.
#
# Return a 2-tuple containing the final magnitude and angle of
# all the forces. angle should again be in degrees. You should
# round both magnitude and angle to one decimal place, which
# you can do using round(magnitude, 1) and round(angle, 1).
#
# To do this, you'll need to use a few functions from the math
# module in Python. The line below will import these:
from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt


# sin, cos, and tan are the trigonometric functions for sine,
# cosine, and tangent. Each takes one argument, an angle in
# radians, and returns its sine, cosine, or tangent.
#
# asin, acos, and atan2 are their inverse functions. Each
# takes two arguments, a vertical component and a horizontal
# component (in that order), and returns the corresponding
# angle in radians.
#
# Note that sin, cos, and tan all assume the angle is in
# radians, and asin, acos, and atan2 will all return an
# angle in radians. So, you'll need to convert your angles to
# radians before or after using these functions, using things
# like this: angle_in_radians = radians(angle)
#           angle_in_degrees = degrees(angle_in_radians)

# sqrt will find the square root of a number, e.g. sqrt(4) = 2.
# Note that you should only need sin, cos, atan2, degrees,
# radians, and sqrt: we've imported the others just in case you
# want to use them.


# Add your function here!
def find_net_force(forces):
    h_force = sum(
        [
            force[0] *
            cos(radians(force[1])) for force in forces
        ]
    )
    v_force = sum(
        [
            force[0] *
            sin(radians(force[1])) for force in forces
        ]
    )

    r_force = round(sqrt((h_force ** 2) + (v_force ** 2)), 1)
    r_angle = round(degrees(atan2(v_force, h_force)), 1)

    return r_force, r_angle


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: (87.0, 54.4)

forces = [(10, 90), (10, -90), (100, 45), (20, 180)]
print(find_net_force(forces))
print()


# Write a function called one_dimensional_booleans.
# one_dimensional_booleans should have two parameters:
# a list of booleans called bool_list and a boolean called
# use_and. You may assume that bool_list will be a list
# where every value is a boolean (True or False).
#
# The function should perform as follows:
#
# - If use_and is True, the function should return True if
#   every item in the list is True (simulating the and
#   operator).
# - If use_and is False, the function should return True if
#   any item in the list is True (simulating the or
#   operator).


# Write your function here!

def one_dimensional_booleans(bool_list, use_and):
    if not use_and:
        return True in bool_list
    else:
        return not False in bool_list


# Below are some lines of code that will test your function.


# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: True, False, True, False.
print(one_dimensional_booleans([True, True, True], True))
print(one_dimensional_booleans([True, False, True], True))
print(one_dimensional_booleans([True, False, True], False))
print(one_dimensional_booleans([False, False, False], False))
print()


# Another method(a long and windy road)* copied:

def one_dimensional_booleans(bool_list, use_and):
    while use_and == True:
        for item in bool_list:
            if item == True:
                b = True

            else:
                b = False
                break
        return b
    while use_and == False:
        for item in bool_list:
            if item == False:
                b = False

            else:
                b = True
                break
        return b


print(one_dimensional_booleans([True, True, True], True))
print(one_dimensional_booleans([True, False, True], True))
print(one_dimensional_booleans([True, False, True], False))
print(one_dimensional_booleans([False, False, False], False))
print()


# Last exercise, you wrote a function called
# one_dimensional_booleans that performed some reasoning
# over a one-dimensional list of boolean values. Now,
# let's extend that.
#
# Imagine you have a two-dimensional list of booleans,
# like this one:
# [[True, True, True], [True, False, True], [False, False, False]]
#
# Notice the two sets of brackets: this is a list of lists.
# We'll call the big list the superlist and each smaller
# list a sublist.
#
# Write a function called two_dimensional_booleans that
# does the same thing as one_dimensonal_booleans. It should
# look at each sublist in the superlist, test it for the
# given operator, and then return a list of the results.
#
# For example, if the list above was called a_superlist,
# then we'd see these results:
#
# two_dimensional_booleans(a_superlist, True) -> [True, False, False]
# two_dimensional_booleans(a_superlist, False) -> [True, True, False]
#
# When use_and is True, then only the first sublist gets
# a value of True. When use_and is False, then the first
# and second sublists get values of True in the final
# list.
#
# Hint: This problem can be extremely difficult or
# extremely simple. Try to use your answer or our
# code from the sample answer in the previous problem --
# it can make your work a lot easier! You may even want
# to use multiple functions.


# Write your function here!
def two_dimensional_booleans(bool_superlist, use_and):
    result = []
    for sublist in bool_superlist:
        if not use_and:
            result.append(True in sublist)
        else:
            result.append(not False in sublist)
    return result


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# [True, False, False]
# [True, True, False]
bool_superlist = [[True, True, True], [True, False, True], [False, False, False]]
print(two_dimensional_booleans(bool_superlist, True))
print(two_dimensional_booleans(bool_superlist, False))
print()


# Another method is to call the function of one dimensional lists:
def one_dimensional_booleans(bool_list, use_and):
    if not use_and:
        return True in bool_list
    else:
        return not False in bool_list


# Calling one dimensional function:
def two_dimensional_booleans(bool_superlist, use_and):
    result = []  # create an empty list to append

    for sublist in bool_superlist:  # iterate through each sublist
        result.append(one_dimensional_booleans(sublist, use_and))  # do not return here
    return result  # return here


bool_superlist = [[True, True, True], [True, False, True], [False, False, False]]
print(two_dimensional_booleans(bool_superlist, True))
print(two_dimensional_booleans(bool_superlist, False))
print()


# Yet another method:
def two_dimensional_booleans(bool_superlist, use_and):
    listOne = []
    listTwo = []
    while use_and == True:
        for sublist in bool_superlist:
            for item in sublist:
                if item == True:
                    b = True
                else:
                    b = False
                    break
            listOne.append(b)
        return listOne
    while use_and == False:
        for sublist in bool_superlist:
            for item in sublist:
                if item == False:
                    b = False
                else:
                    b = True
                    break
            listTwo.append(b)
        return listTwo


bool_superlist = [[True, True, True], [True, False, True], [False, False, False]]
print(two_dimensional_booleans(bool_superlist, True))
print(two_dimensional_booleans(bool_superlist, False))
print()
