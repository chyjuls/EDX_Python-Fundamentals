principal = 5000
rate = 0.05
time = 5
goal = 7000

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Recall in problem 2.4.5 you wrote some code that calculated
# the amount of money in an account based on this formula:
#
#   amount = principal * e ^ (rate * time)
#
# Those three variables are given above again, as well as a
# fourth: goal. We want to see if the investment given by
# these values will exceed the goal. If it will, we want to
# print this message:
#
#  "You'll exceed your goal by [extra money]"
#
# If it will not, we want to print this message:
#
#  "You'll fall short of your goal by [needed money]"
#
# If the investor will meet their goal, [extra money] should
# be the final amount minus the goal. If the investor will
# not meet their goal, [needed money] will be the goal minus
# the final amount.
#
# To make the output more legible, though, we want to round
# the difference to two decimal places. If the difference is
# contained in a variable called 'difference', then we can
# do this to round it: rounded_diff = round(difference, 2)
#
# Working with new and unfamiliar functions or abilities is
# part of learning to code, so use this function in your
# answer!

import math

amount = principal * math.e ** (rate * time)
extra_money = amount - goal
extra_money = round(extra_money, 2)

difference = goal - amount
difference = round(difference, 2)

if amount > goal:
    print("You'll exceed your goal by {}".format(extra_money))
else:
    print("You'll fall short of your goal by {}".format(difference))
    print()

operation = '*'
first_number = 4
second_number = 7

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# You're doing your math homework when you realize, you can
# write a program to do all the simple operations!
#
# The five possible values for operation are:
#
# - "+": Add first_number and second_number
# - "-": Subtract second_number from first_number
# - "*": Multiply first_number by second_number
# - "/": FLoor-divide first_number by second_number (use //)
# - "%": Find the remainder of dividing first_number by
#        second_number
#
# Your calculator should print the full operation according to
# the following format:
#
# [first_number] [operation] [second_number] = [result]
#
# For example, for the initial values above, your calculator
# would print:
#
# 4 * 7 = 28
#
# Notice that for division, we're asking you to use floor
# division to avoid worrying about rounding errors.`
#
# If the operation is not one of the five listed above, print
# "That operation does not exist!"

# add = '+'
# subtract = '-'
# multiply = '*'
# divide = '/'
# remainder = '%'

if operation == '+':
    print(first_number, '+', second_number, '=', first_number + second_number)
elif operation == '-':
    print(second_number, '-', first_number, '=', second_number - first_number)
elif operation == '*':
    print(first_number, '*', second_number, '=', first_number * second_number)
elif operation == '/':
    print(first_number, '/', second_number, '=', first_number // second_number)
elif operation == '%':
    print(first_number, '+', second_number, '=', first_number % second_number)
else:
    print("That operation does not exist!")

print()

grade = 45
curve = 8
total_grade = grade + curve

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Professor Burdell is grading final exams. Based on the
# class average, he has established a curve, whose value is
# given in the variable curve above.
#
# Then, for each individual student, he wants to send a
# personal message based on their grade. Their grade is the
# sum of the value of grade and the value of curve, but it
# cannot be greater than 100; if the curve takes them above
# 100, their grade is 100.
#
# Prof. Burdell then wants to send one of the following
# messages, depending on the student's final grade:
#
# - If the total grade 90 to 100, the message would state:
#   "Congratulations! Your final grade is [their grade], an A."
# - If the total grade is 80 to 89, the message would state:
#   "Good job! Your final grade is [their grade], a B."
# - If the total grade is 70 to 79, the message would state:
#   "Not bad! Your final grade is [their grade], a C."
# - If the total grade is 60 to 69, the message would state:
#   "You passed! Your final grade is [their grade], a D."
# - If the total grade is under 60, the message would state:
#   "It's just one grade. Your final grade is [their grade], an F."
#
# [their grade] should be the result of adding grade and curve,
# but should not be greater than 100.

if total_grade > 100:
    print("Congratulations! Your final grade is 100, an A.")
if total_grade <= 100:
    if total_grade >= 90:
        print("Congratulations! Your final grade is {}, an A.".format(total_grade))
if total_grade <= 89:
    if total_grade > 80:
        print("Good job! Your final grade is {}, a B.".format(total_grade))
if total_grade <= 79:
    if total_grade >= 70:
        print("Not bad! Your final grade is {}, a C.".format(total_grade))
if total_grade <= 69:
    if total_grade >= 60:
        print("You passed! Your final grade is {}, a D.".format(total_grade))
if total_grade < 60:
    print("It's just one grade. Your final grade is {}, an F.".format(total_grade))

print()

egg = True
milk = True
butter = True
flour = True

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Imagine you're deciding what you want to cook. The boolean
# variables above state whether or not you have each of those
# four ingredients.
#
# Here are the dishes you know how to cook and their
# ingredients:
#
# 1. pancakes: egg, milk, butter, flour
# 2. omelette: egg, milk, butter
# 3. custard: egg, milk
# 4. poached eggs: egg
#
# The list above is also a priority list. If you have the
# ingredients for pancakes, you'll make pancakes instead of
# any of the other dishes. If you're missing flour but have
# the other ingredients, you'll make an omlette. You'll only
# make poached eggs if the only ingredient you have is eggs.
#
# Complete the program below such that it prints which dish
# you'll make based on the ingredients you have handy. All
# the dishes should appear exactly as shown above: all lower
# case, spelled the same way. If you do not have the
# ingredients to make any of these dishes, then print the
# text "Go to the store!"


# Add your code here!

pancakes = egg, milk, butter, flour
omelette = egg, milk, butter
custard = egg, milk
poached_eggs = egg

if egg and milk and butter and flour:
    print("pancakes")
elif egg and milk and butter:
    print("omelette")
elif egg and milk:
    print("custard")
elif egg:
    print("poached eggs")
else:
    print("Go to the store!")

print()

print()

cut = "Oval"
clarity = "SI"
color = "E"
carat = 3.3
budget = 706
preferred_cuts = ["Princess", "Marquise", "Heart", "Round"]

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Diamonds are typically evaluated according to four aspects:
# - Cut: The way the diamond is cut
# - Clarity: How clear or flawless the diamond is, rated
#   as F (the best), IF, VVS, VS, SI, or I (the worst)
# - Color: How colorless the diamond is, rated from "D" (the
#   best) to "Z" (the worst)
# - Carat: How large the diamond is, weighed in carats
#
# Cut is usually a matter of personal preference. Clarity,
# color, and carat are matters of value: the clearer, more
# colorless, and larger a diamond is, the greater its value.
#
# Imagine you're shopping for a diamond. You have your
# preferred cuts, and you have a budget in mind. You're shown
# a diamond whose characteristics are represented by the cut,
# color, clarity, and carat variables above. You'll buy the
# diamond if its cost is less than your budget, and if its
# cut is one of your preferred cuts.
#
# At this store, every diamond has a base cost of 100.
#
# For every color rating worse than "D", the cost decreases by
# 2%. An "F" color diamond would be worth 0.96 * the diamond
# cost otherwise because "F" is two colors worse than "D".
#
# A diamond's value is doubled for every level of clarity above
# I. A "VVS"-clarity diamond is worth 8 * the diamond cost
# otherwise because "VVS" is three levels higher than I, and
# doubling its value three times raises its value by 8x total.
#
# After finding its price based on color and clarity, its price
# is multiplied by its weight in carats.
#
# Your program should print "I'll take it!" if you will buy the
# diamond, "No thanks" if you will not. To purchase it, its price
# must be less than your budget and its cut must be one of your
# preferred cuts.
#
# HINT: You can find the number of characters between two
# characters by using the ord() function. ord("E") - ord("D")
# is 1; ord("Z") - ord("D") is 22.
#
# HINT 2: We haven't covered lists, but we did cover how to
# see if an item is present in a list using the 'in' operator
# in chapter 2.3.


# Add your code here!

color_value = ord(color) - ord("D")
color_value_difference = 1 - (color_value * 0.02)

diamond_cost = (100 * color_value_difference)

if clarity == "I":
    diamond_cost += 1
elif clarity == "SI":
    diamond_cost *= 2
elif clarity == "VS":
    diamond_cost *= 4
elif clarity == "VVS":
    diamond_cost *= 8
elif clarity == "IF":
    diamond_cost *= 16
elif clarity == "F":
    diamond_cost *= 32
final_diamond_cost = diamond_cost * carat

if final_diamond_cost <= budget and cut in preferred_cuts:
    print("I'll take it!")
else:
    print("No thanks")

print()

phase = "Full"
distance = 228000
date = 30
eclipse = True

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# There are (at least) three special types of full moons:
#
# - Super Moon: the full moon occurs when the moon is at its
#   closest approach to earth (less than 230,000km away).
# - Blue Moon: the second full moon in a calendar month. In
#   other words, any full moon on the 29th, 30th, or 31st of
#   a month.
# - Blood Moon: a lunar eclipse during a full moon.
#
# Write a program that will print out the type of moon --
# "Full Moon", "Super Moon", "Blue Moon", "Blood Moon", based
# on the values of the variables above. Note that for the moon
# to be any of these special kinds of moons, it must also be
# full.
#
# Note, though, that multiple modifiers can be true at the same
# time. We could have a Super Blue Moon, a Blue Blood Moon, or
# even a Super Blue Blood Moon.
#
# Always print those modifiers in that order. If any of these
# special modifiers is present, do not include the word "Full".
# If none of them are present, but the moon is Full, then print
# "Full Moon". If none of them are present at all, print "Moon".


# Add your code here!

# full_moon = phase == "Full" and (distance > 230000 and date < 29 or date < 30 or date < 31)
# super_blood_blue_moon = phase == "Full" and distance < 230000 and (date == 29 or date == 30 or date == 31) and eclipse

# super_blood_moon = phase == "Full" and distance < 230000 and eclipse

# super_blue_moon = phase == "Full" and distance < 230000 and (date == 29 or date == 30 or date == 31)

# blue_blood_moon = phase == "Full" and distance > 230000 and date == 29 or date == 30 or date == 31 and eclipse

# blue_moon = phase == "Full" and distance > 230000 and date == 29 or date == 30 or date == 31

# blood_moon = phase == "Full" and (distance > 230000 and eclipse)

# if super_blood_blue_moon:
# print("Super Blue Blood Moon")
# elif super_blood_moon:
# print("Super Blood Moon")
# elif blue_blood_moon:
# print("Blue Blood Moon")
# elif blue_moon:
# print("Blue Moon")
# elif blood_moon:
# print("Blood Moon")
# elif full_moon:
# print("Full Moon")
# else:
# print("Moon")
# print()

# This code is copied:

if phase == "Full":
    if distance < 230000:
        if date in [29, 30, 31]:
            if eclipse:
                print("Super Blue Blood Moon")
            else:
                print("Super Blue Moon")
        elif eclipse:
            print("Super Blood Moon")
        else:
            print("Super Moon")
    elif distance >= 230000:
        if date in [29, 30, 31]:
            if eclipse:
                print("Blue Blood Moon")
            else:
                print("Blue Moon")
        elif eclipse:
            print("Blood Moon")
        else:
            print("Full Moon")
else:
    print("Moon")
    print()
# Another method:

result = "Moon"

if eclipse:
    result = "Blood " + result
if date >= 29:
    result = "Blue " + result
if distance < 230000:
    result = "Super " + result

if not (eclipse or date >= 29 or distance < 230000):
    result = "Full Moon"
print(result)
print()
print()

car_value = 10000
purchase_year = 2011
car_age = 8
driver_age = 23
electric = True
emissions_passed = True

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# You're writing some code to determine how much it will cost
# to renew the tag on your license plate. Why? Because I just
# had to pay my tag renewal, and if I have to deal with this
# mess, so do you. 😛
#
# Georgia's tag renewal policies are unnecessarily
# complicated. I've simplified them to make this problem even
# doable. They are:
#
# - Everyone pays $20.
# - If you purchased your car before 2013 (in 2012 or earlier),
#   you also pay 1% of its current value in additional tax.
# - If the car is electric, you pay an additional $200 fee.
#   (This is real.)
# - To renew, you must have passed an annual emissions check,
#   unless your car is electric, or if you're 65 or over and
#   the car's age is 10 years or older.
#
# Your code should print one of two messages. If the person
# needs to pass an emissions test in order to renew their tag,
# it should print, "You must pass an emissions test first."
# This would be the message to print if emissions_passed is
# False and if they are not eligible for either exemption
# mentioned above.
#
# If the person is eligible to renew their tag, the code should
# print: "Your renewal fee is $__.", where __ is the renewal
# cost. Round the renewal fee to the nearest integer. This will
# be $20, plus $200 if the car is electric, plus 1% of car_value
# if the purchase_year is less than or equal to 2012.

fee = 20

if purchase_year < 2013:
    fee += round(0.01 * car_value)
if electric:
    fee += 200
if not emissions_passed:
    if not electric:
        if not (driver_age >= 65 and car_age >= 10):
            print("You must pass an emissions test first.")
        else:
            print("Your renewal fee is ${}.".format(fee))
    else:
        print("Your renewal fee is ${}.".format(fee))
else:
    print("Your renewal fee is ${}.".format(fee))

print()

story = "B"
text = "D"
role = "D"
director = "C"
cast = "D"

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.
#
# In Bryan Cranston's autobiography, he describes how after
# his success on Breaking Bad, he developed a scoring system
# for evaluating new scripts that he received.
#
# First, he would assign the script a grade -- A, B, C, D, or
# F -- in each of five categories: Story, Text, Role, Director,
# and Cast.
#
# Then, he would tally those grades into a total score for the
# script, according to the following chart:
#
#            A   B   C   D   F
# Story     +6  +5  +4  +2  +0
# Text      +5  +4  +3  +1  +0
# Role      +4  +3  +2  +1  +0
# Director  +3  +2  +1  +0  +0
# Cast/Misc +2  +1  +0  +0  +0
#
# For example: an A story, B text, C role, D directory, and
# F cast would get a score of 12: +6 for the story, +4 for the
# text, +2 for the role, +0 for the director, and +0 for the
# cast.
#
# Then, based on that score, the script would be assigned a
# category (note these are slightly different from the image
# because we've excluded the time variable):
#
# 20: Perfect score
# 17 to 19: Must do
# 14 to 16: Seriously consider
# 12 to 13: On the bubble
# 11 or below: Pass
#
# The variables above give the letter grades assigned to each
# of the five components. Write a program that calculates the
# total score he would assign to the script represented by
# these variables. Then on the next line, print the category
# he would assign to that script. For example, for the values
# above, this program would print:
#
# 12
# On the bubble
#
# HINT: This is a *long* program. It's not particularly
# complex -- you're doing the same thing over and over, However,
# that 'same thing' required 4-8 lines each time you do it. Our
# answer is 46 lines long! So, don't think you're off-track just
# because you're writing a lot of lines.


# Add your code here!
#              A   B   C   D   F
# # Story     +6  +5  +4  +2  +0
# # Text      +5  +4  +3  +1  +0
# # Role      +4  +3  +2  +1  +0
# # Director  +3  +2  +1  +0  +0
# # Cast/Misc +2  +1  +0  +0  +0

score = 0

if story == "A":
    score += 6
elif story == "B":
    score += 5
elif story == "C":
    score += 4
elif story == "D":
    score += 2

if text == "A":
    score += 5
elif text == "B":
    score += 4
elif text == "C":
    score += 3
elif text == "D":
    score += 1

if role == "A":
    score += 4
elif role == "B":
    score += 3
elif role == "C":
    score += 2
elif role == "D":
    score += 1

if director == "A":
    score += 3
elif director == "B":
    score += 2
elif director == "C":
    score += 1

if cast == "A":
    score += 2
elif cast == "B":
    score += 1
print(score)

if score == 20:
    print('Perfect score')
elif score >= 17:
    print('Must do')
elif score >= 14:
    print('Seriously consider')
elif score >= 12:
    print('On the bubble')
else:
    print('Pass')
