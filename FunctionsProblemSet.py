# Write a function called lucky_sevens that takes in one
# parameter, a string variable named a_string. Your function
# should return True if there are exactly three '7's in
# a_string. If there are less than three or more than three
# '7's, the function should return False.
#
# For example:
#  - lucky_sevens("happy777bday") should return True.
#  - lucky_sevens("h7app7ybd7ay") should also return True.
#  - lucky_sevens("happy77bday") should return False.
#  - lucky_sevens("h777appy777bday") should also return False.
#
# Hint: Remember in Chapter 3.3, we covered how to use a loop
# to look at each character in a string.


# Write your function here!


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: True, True, False, False, each on their own line.
import re


def lucky_sevens(a_string):
    # function to return true if exactly 3 sevens

    counter = 0  # counts the number of times 7 occurs in the a_string

    for i in a_string:  # loops through the a_string

        if i == "7":  # if 7 occurs in the a_string

            counter = counter + 1  # counter increases by 1 every time 7 occurs

    if counter == 3:  # if 7 occurs exactly 3 times in a_string

        return True  # returns true

    else:  # 7 occurs less or more than 3 times in a_string

        return False  # returns false


# tests the function lucky_sevens with different inputs
# Another way:

# We'll start with the function header: the function is
# called lucky_sevens, and it has one parameter: a_string.

def lucky_sevens(a_string):
    # Next, we're going to want to count something. So,
    # let's create a counter:
    count = 0

    # Next, we need to go through each letter one by one:
    for letter in a_string:

        # Finally, we need to check whether each letter is
        # the character "7":
        if letter == "7":
            # And if so, add to the counter:
            count += 1

    # Then, only once we've done everything else are we
    # ready to return. Notice that this line is
    # indented once: it's inside the function, but not the
    # loop or conditional.
    #
    # count == 3 will resolve to True if count is 3, False
    # otherwise. So, we can just return it directly:

    return count == 3


print(lucky_sevens("happy777bday"))
print(lucky_sevens("h7app7ybd7ay"))
print(lucky_sevens("happy77bday"))
print(lucky_sevens("h777appy777bday"))


def poke_go(name, number_of_pokemon=0):
    if number_of_pokemon == 0:
        return "You have caught no Pokemon, " + name
    elif number_of_pokemon < 5:
        return "You are just starting out, " + name
    elif number_of_pokemon < 250:
        return "You are getting better, " + name
    else:
        return "You are the very best, like no one ever was, " + name


print(poke_go("NewGamer98"))
print(poke_go("PokeMASTER222", number_of_pokemon=100))
print(poke_go("GaryFOak", 250))

print()


# Write a function called hide_and_seek. The function should
# have no parameters and return no value; instead, when
# called, it should just print the numbers from 1 through 10,
# follow by the text "Ready or not, here I come!". Each
# number and the message at the end should be on its own
# line.
#
# Then, call the function.
#
# There should be no print statements outside the function.


# Write your function here!

def hide_and_seek():
    for i in range(11):
        print(i)
    print("Ready or not, here I come!")


hide_and_seek()


# Another method using while loop:

def HideSeek():
    i = 1
    while i <= 10:
        print(i)
        i += 1
    print("Ready or not, here I come!")


HideSeek()

print()


# Write a function called select_a_show. select_a_show
# should have one parameter, an integer representing
# how many minutes until you have to leave.
# select_a_show should return the following:
#
# - If you have 0 or fewer minutes, it should return
#   the string, "You're late!"
# - If you have 1 to 10 minutes, it should return
#   the string, "Leave now, be early!"
# - If you have 11 to 45 minutes, it should return
#   the string, "Watch a comedy!"
# - If you have 46 to 100 minutes, it should return
#   the string, "Watch a drama!"
# - If you have more than 100 minutes, it should return
#   the string, "Watch a movie!"


# Add your function here!
def select_a_show(minutes=180):
    if minutes <= 0:
        return "You're late!"
    elif minutes <= 10:
        return "Leave now, be early!"
    elif minutes <= 45:
        return "Watch a comedy!"
    elif minutes <= 100:
        return "Watch a drama!"
    else:
        return "Watch a movie!"


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# "You're late!", "Leave now, be early!", "Watch a comedy!",
# "Watch a drama!", and "Watch a movie!".
print(select_a_show(-5))
print(select_a_show(5))
print(select_a_show(34))
print(select_a_show(68))
print(select_a_show(124))

print()


# Write a function called semihemisphere. semihemisphere
# should return which semihemisphere a latitude-longitude
# coordinate pair is in: Northwest, Northeast, Southwest,
# or Southeast. A point in the Northern and Western
# hemispheres would be Northwest; in the Southern and Eastern
# hemispheres would be Southeast; etc.
#
# semihemisphere will take as input two floats: latitude
# and longitude. Latitude is a number between -90 and 90
# representing the North-South position on the globe (-90
# for the South pole, 90 for the North pole). Longitude is
# a number between -180 to 180 representing the East-West
# position on the globe (-180 is the furthest west, and 180
# is the furthest east).
#
# The Southern hemisphere is from -90° to 0° latitude. The
# Northern hemisphere is from 0° to 90° latitude. The
# Eastern hemisphere is from 0° to 180° longitude. The
# Western hemisphere is from -180° to 0° longitude.


# Add your code here!

def semihemisphere(latitude=90, longitude=180):
    if latitude < 0 and longitude < 0:
        return "Southwest"
    elif latitude > 0 and longitude < 0:
        return "Northwest"
    elif latitude > 0 and longitude > 0:
        return "Northeast"
    else:
        return "Southeast"


# Below are some lines of code that will test your function.


# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print Northwest, Southeast, Northeast, Southwest
print(semihemisphere(33.7, -84.4))
print(semihemisphere(-71.1, 86.3))
print(semihemisphere(67.1, 12.1))
print(semihemisphere(-11.6, -62.3))

print()


# In the previous coding problem, you created a function
# called hide_and_seek that printed the numbers from 1 to 10.
# Now, however, we want to extend that. What if we want to
# count to 20? 30?
#
# Modify your previous function so that it takes as input one
# parameter: count. Then, instead of printing the numbers from
# 1 to 10, it should print the numbers from 1 to the value of
# count. Then, end with "Ready or not, here I come!"


# Write your function here!
def hide_and_seek(count):
    for i in range(1, count + 1):
        print(i)
    print("Ready or not, here I come!")


# The function call below will test your function. We'll delete
# and overwrite this with other calls to hide_and_seek with
# different numbers during grading:
hide_and_seek(36)

print()


# A year is considered a leap year if it abides by the
# following rules:
#
#  - Every 4th year IS a leap year, EXCEPT...
#  - Every 100th year is NOT a leap year, EXCEPT...
#  - Every 400th year IS a leap year.
#
# This starts at year 0. For example:
#
#  - 1993 is not a leap year because it is not a multiple of 4.
#  - 1996 is a leap year because it is a multiple of 4.
#  - 1900 is not a leap year because it is a multiple of 100,
#    even though it is a multiple of 4.
#  - 2000 is a leap year because it is a multiple of 400,
#    even though it is a multiple of 100.
#
# Write a function called is_leap_year. is_leap_year should
# take one parameter: year, an integer. It should return the
# boolean True if that year is a leap year, the boolean False
# if it is not.


# Write your function here!

def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print False, True, False, and True, each preceded by the
# label "[year] is a leap year:".
print("1993 is a leap year:", is_leap_year(1993))
print("1996 is a leap year:", is_leap_year(1996))
print("1900 is a leap year:", is_leap_year(1900))
print("2000 is a leap year:", is_leap_year(2000))

print()


# In chemistry, the ideal gas law states:

# pressure * volume = # of moles * gas constant * temperature
#
# This is usually abbreviated to:
#
# PV = nRT
#
# We can solve this for any of these five variables, but let's
# solve it for Pressure. In terms of Pressure, the ideal gas
# law states:
#
# P = (nRT) / V
#
# Write a function called find_pressure that takes as input
# three variables: number of moles, temperature, and volume.
# You can call these variables in the function whatever you
# want, but they must be specified in that order: moles, then
# temperature, then volume. You should assume all three are
# floats. Then, return as output your calculation for
# pressure. For the gas constant, you should use the value
# 0.082057.
#
# Hint: Python's rounding errors can change based on the
# order of the multipliers. If you're having difficulty with
# your answer being off by tiny fractions, change the order
# of the numbers to match the order in the formula above.


# Write your function here!
def find_pressure(num_of_moles, temp, volume):
    result = (num_of_moles * 0.082057 * temp) / volume
    return result


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: "Result: 48.905972000000006". The extra zeroes and
# the 6 are rounding errors by Python.
test_n = 10
test_T = 298
test_V = 5
print("Result:", find_pressure(test_n, test_T, test_V))
print()


# Write a function called sum_of_primes. sum_of_primes should
# take as input a single integer, and then it should sum all
# the prime numbers up to and including that integer (if it is
# prime. Note that 1 is not considered a prime number.
#
# For example, sum_of_primes(6) would return 10: 2 + 3 + 5 = 10.
# 1, 4 and 6 are not prime; 2, 3, and 5 are.
#
# Other examples include:
#
# sum_of_primes(7)  -> 17 (2 + 3 + 5 + 7 = 17)
# sum_of_primes(8)  -> 17 (2 + 3 + 5 + 7 = 17)
# sum_of_primes(11) -> 28 (2 + 3 + 5 + 7 + 11 = 28)
#
# To help you with this, we have supplied you with a function
# to find if a single number is prime. You do not need to know
# how this program works; only that it works. You may use this
# function, but you do not have to. Here is the function:

def is_prime(n):
    from itertools import count, islice
    return n > 1 and all(n % i for i in islice(count(2), int(n ** 0.5) - 1))


# Add your function here!

def sum_of_primes(num):
    sum = 0

    for i in range(1, num + 1):

        # Check for prime
        check_Prime = is_prime(i)

        if check_Prime:
            # Sum the prime number
            sum += i

    return sum


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print 10, 17, 17, and 28.
print(sum_of_primes(6))
print(sum_of_primes(7))
print(sum_of_primes(8))
print(sum_of_primes(11))

print()


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
    import datetime
    month_number = datetime.datetime.strptime(month, '%B').month
    if datetime.date(2020, month_number, day) >= datetime.date(2020, 12, 21) or datetime.date(2020, month_number,
                                                                                              day) < datetime.date(2020,
                                                                                                                   3,
                                                                                                                   20):
        return "Winter"
    elif datetime.date(2020, month_number, day) >= datetime.date(2020, 3, 20) and datetime.date(2020, month_number,
                                                                                                day) < datetime.date(
        2020, 6, 21):
        return "Spring"
    elif datetime.date(2020, month_number, day) >= datetime.date(2020, 6, 21) and datetime.date(2020, month_number,
                                                                                                day) < datetime.date(
        2020, 9, 22):
        return "Summer"
    elif datetime.date(2020, month_number, day) >= datetime.date(2020, 9, 22) and datetime.date(2020, month_number,
                                                                                                day) < datetime.date(
        2020, 12, 21):
        return "Fall"


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print Winter, Spring, Summer, and Fall in that order.
print(what_season("December", 25))
print(what_season("June", 1))
print(what_season("June", 23))
print(what_season("September", 27))


# Another way:
def what_season(month, day):
    if month == "June" and day >= 21 or month == "July" and day <= 31 or month == "August" and day <= 31 or month == "September" and day <= 21:
        return "Summer"



    elif month == "March" and day >= 20 or month == "April" and day <= 31 or month == "May" and day <= 31 or month == "June" and day <= 20:
        return "Spring"

    elif month == "September" and day >= 21 or month == "October" and day <= 31 or month == "November" and day <= 31 or month == "December" and day <= 20:
        return "Fall"
    else:
        return "Winter"


print(what_season("December", 25))
print(what_season("June", 1))
print(what_season("June", 23))
print(what_season("September", 27))

print()


# Basketball coach Phil Jackson says that in order for an NBA
# team to be a contender for a championship, they need to win
# 40 games before they lose 20 games.
#
# Write a function called is_a_contender that will take three
# parameters: a team name (a string), a number of wins (an
# integer), and a number of losses (an integer).
#
# Based on these parameters, the function should return one
# of three strings:
#
# - If the team is a contender (at least 40 wins and fewer
#   than 20 losses), return "The [team name] are a contender!"
# - If the team is not a contender (less than 40 wins and at least
#   20 losses), return "The [team name] are not a contender!"
# - If it cannot be determined (both values are higher or both
#   values are lower), return "The [team name] might be a contender!"


# Add your code here!

def is_a_contender(team_name, num_of_wins, num_of_losses):
    if num_of_wins >= 40 and num_of_losses < 20:
        return "The {} are a contender!".format(team_name)
    elif num_of_wins < 40 and num_of_losses >= 20:
        return "The {} are not a contender!".format(team_name)
    else:
        return "The {} might be a contender!".format(team_name)


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: "The Hawks are not a contender!".

test_team_name = "Hawks"
test_wins = 18
test_losses = 40

print(is_a_contender(test_team_name, test_wins, test_losses))

print()


# Consult this blood pressures chart: http://bit.ly/2CloACs
#
# Write a function called check_blood_pressure that takes two
# parameters: a systolic blood pressure and a diastolic blood
# pressure, in that order. Your function should return "Low",
# "Ideal", "Pre-high", or "High" -- whichever corresponds to
# the given systolic and diastolic blood pressure.
#
# You should assume that if a combined blood pressure is on the
# line between two categories (e.g. 80 and 60, or 120 and 70),
# the result should be the higher category (e.g. Ideal and
# Pre-high for those two combinations).
#
# HINT: Don't overcomplicate this! Think carefully about in
# what order you should check the different categories. This
# problem could be easy or extremely hard depending on the
# order you change and whether you use returns or elifs wisely.


# Add your code here!
def check_blood_pressure(systolic, diastolic):
    if (systolic > 70 and systolic < 90) and diastolic < 60:
        return "Low"

    elif (systolic >= 90 and systolic < 120) and (diastolic > 40 and diastolic <= 80):
        return "Ideal"

    elif (systolic >= 120 and systolic < 140) and (diastolic > 40 and diastolic < 90):
        return "Pre-high"

    else:
        return "High"


# A better way ..quite simplified:
# First, we define the function. It has two parameters:
# systolic and diastolic.
def check_blood_pressure(systolic, diastolic):
    # Low blood pressure is easy: systolic must be under 90
    # and diastolic must be under 60.
    if systolic < 90 and diastolic < 60:
        return "Low"

    # For Ideal, we know that systolic must be less than 120
    # and less than 80. However, how do we handle making sure
    # it's Ideal and not Low? For example, if systolic is 80,
    # then diastolic needs to be above 60, but if systolic is
    # 100, then diastolic just needs to be above 40.
    #
    # But we don't need to worry about that! If it was Low,
    # then the function would have already ended based on the
    # conditional above. So, if we reach this line, we *know*
    # that it isn't low. So, we just check if it's Ideal:
    elif systolic < 120 and diastolic < 80:
        return "Ideal"

    # By that same logic, if we reach the next conditional,
    # we know it's neither Low nor Ideal: so, we just check
    # if it's Pre-high:
    elif systolic < 140 and diastolic < 90:
        return "Pre-high"

    # If it's not Low, Ideal, or Pre-high, it must be High:
    else:
        return "High"


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: Ideal
test_systolic = 110
test_diastolic = 70

print(check_blood_pressure(test_systolic, test_diastolic))

print()
# cannot find my pokemon code so I copied this:

STAB = 1
Type = 0.25
Critical = 2
Other = 1
Random = 1
Level = 50
Attack = 125
Defense = 110
Base = 60

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.
# In the Pokemon game franchise, damage is calculated using this formula:
# https://studio.edx.org/asset-v1:GTx+CS1301+1T2017+type@asset+block@DamageCalc.png
#
# In that formula, the variable Modifier is calculated using this formula:
# https://studio.edx.org/asset-v1:GTx+CS1301+1T2017+type@asset+block@ModifierCalc.png
#
# Add code below such that the program prints the total damage
# caused based on the STAB, Type, Critical, Other, Random,
# Level, Attack, Defense, and Base given above.
#
# Hint: Don't try to do all these calculations at once! Break
# the complicated formual down into bite-sized little chunks.
# Add your code here!
import math

modifier = STAB * Type * Critical * Other * Random
print(modifier)
damage = ((2 * Level + 10) / 250 * (Attack / Defense) * Base + 2) * modifier
print(damage)

print()


# Recall Coding Problem 2.4.4. In that problem, you calculated
# the damage done by an attack based on several parameters.
#
# Convert your code from there into two functions, one called
# calculate_damage and one called calculate_modifier.
#
# Your function for calculate_damage must call calculate_modifier;
# it may not calculate the modifier separately. As such,
# calculate_damage should accept all ten parameters: STAB,
# Type, Critical, Other, Random, Level, Attack, Defense, and
# Base. You'll need to pass STAB, Type, Critical, Other, and
# Random to calculate_modifier.
#
# Make sure the parameters to each function follow the order
# shown above.
#
# As a reminder, damage is calculated using this formula:
# courses.edx.org/asset-v1:GTx+CS1301xII+1T2018+type@asset+block@DamageCalc.png
#
# Modifier is calculated using this formula:
# https://studio.edx.org/asset-v1:GTx+CS1301+1T2017+type@asset+block@ModifierCalc.png


# Add your code here!

def calculate_modifier(STAB, Type, Critical, Other, Random):
    return STAB * Type * Critical * Other * Random


def calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base):
    modifier = calculate_modifier(STAB, Type, Critical, Other, Random)
    return ((2 * Level + 10) / 250 * (Attack / Defense) * Base + 2) * modifier


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


# -----------------------------------------------------------
# In this problem, you should write three functions:
# word_count, letter_count, and average_word_length.
#
# word_count should take as input a string. It should return
# the number of words in the string. You may assume that the
# number of words in the string will be one more than the
# number of spaces in the string.
#
# letter_count should take as input a string. It should return
# the number of letters in the string. You may assume that
# the string is only letters and spaces: no punctuation or
# numbers.
#
# average_word_length should take as input a string. It should
# return the average length of the words in the string. You
# can find the average length by dividing the number of letters
# by the number of words.
#
# Your implementation for average_word_length *must* call
# word_count and letter_count.


# Add your code here!

# Define a function and count number of words in a_string, using the for loop:
# you can also use the split()
# Include spaces

def word_count(a_string):
    count = 1
    for i in range(len(a_string)):
        if a_string[i] == ' ' or a_string == '/n' or a_string == '\t':
            count += 1
    return count


# define another function and count the number of characters in the string.
# This time DO NOT COUNT the spaces.

def letter_count(a_string):
    count_2 = 0
    for k in a_string:
        if k != " ":
            count_2 += 1
    return count_2


# Create another function and call previous functions within the third function
# To calculate average word length.

def average_word_length(a_string):
    word_num = word_count(a_string)
    letter_num = letter_count(a_string)
    average = letter_num / word_num
    return average


# Below are some lines of code that will test your function.
# You can change the value of the variable to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 3.5
a_string = "Up with the white and gold"

print(average_word_length(a_string))
print()


# There are a lot of use cases where we want to check to see
# if a string has any invalid characters in it. For example,
# when asking for a credit card number, we want to make sure
# there are no non-numerals (although we might accept dashes
# or spaces). When asking for a name, we want to make sure
# all the characters are letters, spaces, or the occasional
# punctuation mark.
#
# Write a function called is_valid. is_valid should take two
# parameters: a string to check, and a string of all valid
# characters.
#
# is_valid should return the boolean True if all the
# characters in the string to check are present in the string
# of valid characters. It should return False if any character
# in the checked string does not appear.


# Add your code here!


# Took me two hours to solve this, using the set/issubset method....pheew!!

def is_valid(valid_string, valid_character):
    valid_string = set(valid_string)
    if valid_string.issubset(valid_character):
        return True
    else:
        return False


print()


# Another method:
def is_valid_2(valid_string, valid_character):
    for character in valid_string:
        if not character in valid_character:
            return False
    return True


sample_valid_string = "1234-5678-9011-1111"
sample_invalid_string = "1234!5678.9011?1111"
valid_characters = "0123456789-"

print(is_valid(sample_valid_string, valid_characters))
print(is_valid(sample_invalid_string, valid_characters))

# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print True, then False

sample_valid_string = "1234-5678-9011-1111"
sample_invalid_string = "1234!5678.9011?1111"
valid_characters = "0123456789-"

print(is_valid(sample_valid_string, valid_characters))
print(is_valid(sample_invalid_string, valid_characters))

print()


# In this problem, your goal is to write a function that can
# either count all the vowels in a string or all the consonants
# in a string.
#
# Call this function count_letters. It should have two
# parameters: the string in which to search, and a boolean
# called find_consonants. If find_consonants is True, then the
# function should count consonants. If it's False, then it
# should instead count vowels.
#
# Return the number of vowels or consonants in the string
# depending on the value of find_consonants. Do not count
# any characters that are neither vowels nor consonants (e.g.
# punctuation, spaces, numbers).
#
# You may assume the string will be all lower-case letters
# (no capital letters).


# Add your code here!
# First create a function count_letters:
# Put vowels in a list
# variables to store your if expressions in
# create a condition for boolean value, if find_consonants
# return value of count, by using the len function
# Do not forget to convert a_string to lower case, upper case vowels are counted differently.

def count_letters(a_string, find_consonants):
    a_string = a_string.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    non_final = [each for each in a_string if each not in vowels and each != " "]
    final = [each for each in a_string if each in vowels]
    if find_consonants:
        return len(non_final)
    else:
        return len(final)


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print 14, then 7.

a_string = "up with the white and gold"

print(count_letters(a_string, True))
print(count_letters(a_string, False))

print()


# Another method:

def count_vowels(a_string):
    count = 0
    for character in a_string:
        if character in "aeiou":
            count += 1
    return count


def count_consonants(a_string):
    count = 0
    for character in a_string:
        if character in "bcdfghjklmnpqrstvwxyz":
            count += 1
    return count


# If we have those, writing count_letters itself becomes
# easy. We just have it look at find_consonants to see
# which of those other two functions it should call:

def count_letters(a_string, find_consonants):
    if find_consonants:
        return count_consonants(a_string)
    else:
        return count_vowels(a_string)


a_string = "up with the white and gold"

print(count_letters(a_string, True))
print(count_letters(a_string, False))
