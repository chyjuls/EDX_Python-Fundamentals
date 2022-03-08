import math


def cherry_pie(song):
    if "Cherry" in song:
        print("Sheee's my cherry pie")
    else:
        print("Huh... must be an American Pie.")


cherry_pie("Black Horse and a Cherry Tree")


def should_I_go_to_Waffle_House():
    print(True)


should_I_go_to_Waffle_House()


def average_grades(num1, num2, num3, num4, num5):
    sum = num1 + num2 + num3 + num4 + num5
    average = sum / 5
    print(average)


average_grades(80, 80, 95, 86, 79)


def print_division_symbol():
    print("÷")


print_division_symbol()


def print_multiplication_symbol():
    print("×")


print_multiplication_symbol()
# Functions with return statements and parameters.


# Write a function called get_todays_date that returns
# today's date as a string, in the form year/month/day.
# For example, if today is January 15th, 2017, then it
# would return 2017/1/15.
#
# Remember, you took care of the string formatting part of
# this exercise in 2.2.9 Coding Exercise 1! Now, you're
# converting it to a function that returns the string.
#
# Note that the line below will let you access today's date
# using date.today() anywhere in your code.
from datetime import date

# Write your function here!


# If you want to test your code, you can do so by calling
# your function below. However, this is no longer required


# for grading.


import datetime


def get_todays_date():
    todays_date = date.today()
    date_string = " "
    date_string += str(todays_date.year)
    date_string += "/"
    date_string += str(todays_date.month)
    date_string += "/"
    date_string += str(todays_date.day)
    return date_string


print(get_todays_date())
print()


# Functions with parameters/ arguments when called:

# Write a function that takes in one integer parameter, the
# side length of a square, and returns the area. The function
# should be named find_area, and have one parameter:
# side_length.


# Write your function here!

def find_area(side_length):
    return side_length ** 2


find_area(side_length=4)

# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: "A square with side length 4 has an area of 16".

test_side_length = 4
print("A square with side length", test_side_length, "has an area of", find_area(test_side_length))


def introduction(name, age):
    return "My name is " + str(name) + " and I am " + str(age) + " years old."


print(introduction("Wilbert", 6))

print()


# More functions with parameters exercise:
# Helping us develop this class are a team of teaching
# assistants, often called TAs for short.
#
# Write a function called my_TAs. The function should take as
# input three strings: first_TA, second_TA, and third_TA. It
# should return as output the string, "[first_TA], [second_TA],
# and [third_TA] are awesome!", with the values replacing the
# variable names.
#
# For example, my_TAs("Sridevi", "Lucy", "Xu") would return
# the string "Sridevi, Lucy, and Xu are awesome!"
#
# Hint: Notice that because you're returning a string instead
# of printing a string, you can't use the print() statement
# -- you'll have to create the string yourself, then return
# it!


# Write your function here!

def my_TAs(first_TA, second_TA, third_TA):
    my_string = str(first_TA) + "," + str(second_TA) + " and " + str(third_TA) + " are awesome!."
    return my_string


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: "Joshua, Jackie, and Marguerite are awesome!".

test_first_TA = "Joshua"
test_second_TA = "Jackie"
test_third_TA = "Marguerite"
print(my_TAs(test_first_TA, test_second_TA, test_third_TA))

print()


# We've written the function, reverse, below. This function
# takes a string and returns the reverse of it. There are two
# scope errors somewhere in the code. Read through all the
# code below to find and fix the errors, so that the function
# produces the correct output and the result of the function
# is correctly printed. Note that you should not change the
# three lines that are already present in the function, but
# you may add lines before them, or you may change or add to
# the lines outside the function.
#
# Note that your goal here is to fix both the function itself
# and the program as a whole. So, your function should be
# able to be called on a new string, and the program when
# run should print the reverse of the string originally on
# line 29.


def reverse(a_string):
    # You may add code before the following three lines.
    rev = " "
    # Don't change these three lines.
    for i in range(len(a_string) - 1, -1, -1):
        rev = rev + a_string[i]
    return rev


# You may change or add to the following lines.
rev = reverse("This string should be reversed!")
print(rev)


# Write a function called snowed_in that will determine
# whether school is closed based on the weather and
# temperature. We'll pretend the school is in Georgia, where
# a little snow or sub-freezing temperatures are enough to
# close down schools!
#
# The function should take three parameters:
#
# - temperature, a float
# - weather, a string
# - is_celsius, a boolean
#
# The function should return True if temperature is below
# freezing (32 if is_celsius is False, 0 if is_celsius is
# True) or if weather is "snowy". Otherwise, it should
# return False.
#
# Note, however, that is_celsius should be an optional
# argument. If the function call does not supply a value for
# is_celsius, assume it is True.
#
# For example:
#
# snowed_in(15, "sunny") -> False
# is_celsius is assumed to be True, so 15 is not below
# freezing.
#
# snowed_in(15, "sunny", is_celsius = False) -> True
# is_celsius is False, so 15 is below freezing.
#
# snowed_in(15, "snowy", is_celsius = True) -> True
# The weather is "snowy", so the temperature doesn't matter.


# Write your function here!


def snowed_in(temperature, weather, is_celsius=True):
    if temperature < 0 or weather == "snowy":
        return True
    elif is_celsius == False and temperature < 32 or weather == "snowy":
        return True
    else:
        return False


# Below are some lines of code that will test your function.


# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print False, True, and True, each on their own line.

print(snowed_in(15, "sunny"))  # Should print False
print(snowed_in(15, "sunny", is_celsius=False))  # Should print True
print(snowed_in(15, "snowy", is_celsius=True))  # Should print True


# Another method: Copied...
def snowed_in(temperature, weather, is_celsius=True):
    #  First we'll check if it's snowing and return True if it is regardless of the temperature
    if weather == "snowy":
        return True
    # Then we'll check if the temperature is below freezing for each of is_celsius
    elif is_celsius and temperature < 0:
        return True
    elif not is_celsius and temperature < 32:
        return True
    # If none of the above are true, better get to school you slackers!
    else:
        return False


print()


# Yet another way:

# We're working on the same function, so our function
# declaration will remain the same:

def snowed_in(temperature, weather, is_celsius=True):
    # Note that we could accomplish this entire function
    # in only one line. Here's the line:

    return weather == "snowy" or temperature < 0 or (temperature < 32 and not is_celsius)

    # How does that line work? It's one long boolean statement.
    # At the top level, the logical operators are all 'or'. So,
    # only one of the three parts needs to be True for the
    # statement as a whole to be True:
    #
    # - If weather is snowy, then the statement is True.
    # - If temperature is less than 0, then it doesn't matter
    #   if we're in Celsius or Fahrenheit: both are freezing,
    #   so the statement is True.
    # - If temperature is less than 32 and we're in Fahrenheit,
    #   then the statement is True.
    #
    # If all of those things are False, the statement is False.
    # So, we just return the result of that expression.


snowed_in(15, "sunny")  # Should print False
snowed_in(15, "sunny", is_celsius=False)  # Should print True
snowed_in(15, "snowy", is_celsius=True)  # Should print True


def happy():
    print("smile")


happy()


def say_good_night():
    name = "Jack"
    return "Good Night, " + name + " and "


print(say_good_night(), end="")
print("Jill")

print()


def yay_TAs(ta1, ta2, ta3):
    result = ta3 + ", " + ta2 + ", and " + ta1 + " are awesome!"
    return result


my_string = yay_TAs("Jackie", "Joshua", "Marguerite")
print(my_string)

print(1, 2, 3, sep="")
print(4, 5, 6, end="$")
print()
print(7, 8, 9, 0, sep="!")
print()

print(1, 2, 3, sep="")
print(4, 5, 6, end="$")
print()
print(7, 8, 9, sep="!", end="!")
print(0)


# Write a function called what_season. what_season should
# have two parameters: the first a string representing
# a month, and the second an integer representing a day.
#
# what_season should return "Spring" if the date is in
# Spring, "Summer" if it's in Summer, "Fall" if it's in
# Fall, and "Winter" if it's in Winter.
#
# For this problem, we define those seasons as follows:
#
# - Spring starts March 20.
# - Summer starts June 21.
# - Fall starts September 22.
# - Winter starts December 21.
#
# So, March 20 to June 20 would be Spring; June 21 to
# September 21 would be Summer; September 22 to December
# 20 would be Fall; and December 21 to March 19 would be
# Winter.


# Add your code here!
def what_season(month, day):
    if month == "June" and day >= 21 or month == "July" and day <= 31 or month == "August" and day <= 31 or month == "September" and day <= 21:
        return "Summer"



    elif month == "March" and day >= 20 or month == "April" and day <= 31 or month == "May" and day <= 31 or month == "June" and day <= 20:
        return "Spring"

    elif month == "September" and day >= 21 or month == "October" and day <= 31 or month == "November" and day <= 31 or month == "December" and day <= 20:
        return "Fall"
    else:
        return "Winter"


# Below are some lines of code that will test your function.
# you can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print Winter, Spring, Summer, and Fall in that order.
print(what_season("December", 25))
print(what_season("June", 15))
print(what_season("June", 23))
print(what_season("September", 27))

print()


# calling a function within a function....# Not nested functions!!
#
# def calculate_damage(stab, type_2, critical, other, random, level, attack, defense, base):

# def calculate_modifier(stab, type_2, critical, other, random):

# modifier = (stab * type_2 * critical * other * random)

# return modifier

##calculate_modifier(stab, type_2, critical, other, random)

# damage = ((2 * Level + 10) / 250 * (attack / defense) * base + 2) * calculate_modifier(STAB, Type, Critical, Other,
# Random)
# return damage


def calculate_modifier(STAB, Type, Critical, Other, Random):
    return STAB * Type * Critical * Other * Random


def calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base):
    modifier = calculate_modifier(STAB, Type, Critical, Other, Random)
    return (((2 * Level + 10) / 250) * (Attack / Defense) * Base + 2) * modifier


# Below are some lines of code that will test your function.


# You can change the value of the variable to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 16.0

STAB = 1
Type = 0.25
Critical = 2
Other = 1
Random = 1
Level = 50
Attack = 125
Defense = 110
Base = 60

print(calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base))
print()


def has_a_vowel(a_str):
    for letter in a_str:
        if letter in "aeiou":
            return True
        else:
            return False


has_a_vowel("atlanta")


def numCombinations(n, r):
    result = math.comb(n, r)
    return result


print(numCombinations(52, 2))
print(numCombinations(10, 5))
print(numCombinations(4, 1))
