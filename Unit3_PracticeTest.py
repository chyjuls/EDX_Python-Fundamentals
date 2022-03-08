age = 52
born_in_the_us = False
time_since_citizenship = 7

if age > 34 and born_in_the_us:
    print("You can run for President in the US!")
if age > 24 and time_since_citizenship > 6:
    print("You can run for Representative in the US!")
if age > 29 and time_since_citizenship > 8:
    print("You can run for Senator in the US!")

print()
cash_on_hand = 25
atm_nearby = False
cashback_nearby = False

if cash_on_hand < 20 and (atm_nearby or cashback_nearby):

    print("Get some cash!")

else:
    print("Go home!")

    print()

cost = 7500
out_of_network = False

if out_of_network and cost > 1000:
    print("The maximum out-of-network cost is $1000.")
elif not out_of_network and cost > 5000:
    print("The maximum in-network cost is $5000.")
else:
    print("Expense approved!")
print()
is_breakfasttime = False
cash = 2

if is_breakfasttime:

    if cash > 10:
        print("Go to Egg Harbor!")
    elif cash > 5:
        print("Go to Waffle House!")
    elif cash > 1:
        print("Go to McDonald's!")
else:
    if cash > 20:
        print("Go to Atwood's!")
    elif cash > 10:
        print("Go to Cypress!")
    else:
        print("Go to Waffle House!")

print()

for i in range(5, 10 + 1):
    print(i)

list_of_numbers = [5, 10, 15, 20, 25, 30]
for some_number in list_of_numbers:
    print(some_number)

i = 0
while i < 10:
    i += 1
    print(i)
print()

i = 1
j = 100
while i < j:
    print(i)
    i *= 2
print()

i = 10
j = 0
while i >= j:
    print(i)
    i -= 2

print()

i = 20
j = 10
for num in range(i, j, -2):
    print(num)
print()

i = 5
j = 5
for num_1 in range(1, i):
    for num_2 in range(1, j):
        print(num_1 * num_2)

print()


def product_4(num_1, num_2, num_3, num_4):
    return num_1 * num_2 * num_3 * num_4


print(product_4(2, 2, 3, 3, ))


def merge_strings(a_string, b_string, reverse=False, Capitalize=True):
    if reverse:
        return b_string + a_string
    elif Capitalize:
        return a_string.isupper() + b_string.isupper()
    else:
        return a_string + b_string


print(merge_strings("onion", "raisin"))
print()


def my_q(num, den, rec=False, neg=False):
    if rec:
        if neg:
            return den / -num
        else:
            return den / num
    else:
        return num / den


result = my_q(2.0, 1.0, neg=True) * my_q(2.0, 1.0, rec=True)

print(result)
a_string = "!"

if "!!!" in a_string:
    print("You're really excited!")
elif "!!" in a_string:
    print("You're pretty excited!")
elif "!" in a_string:
    print("You're excited!")
else:
    print("Are you bored?")

print()
start = 0
finish = 10

for i in range(start, finish + 1, 2):
    print(i)
print()

while start <= finish:
    print(start)
    start += 2

print()


def is_a_factor(number, potential_factor):
    if potential_factor % number == 0:
        return True
    else:
        return False


# The function is_a_factor should return True if potential_factor is a factor of number
# , False if it is not.
# potential_factor is a factor of number i
# f potential_factor goes into number evenly (no remainder).
print()


def average_evens(start, end):
    sum = 0
    count = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            sum += i
            count += 1

    return sum / count


print(average_evens(1, 10))

print()

period = "AM"
hour = 12

if period == "AM" and hour <= 4:
    print("It's early!")
elif period == "AM":
    print("Good morning!")
elif hour <= 5:
    print("Good afternoon!")
elif hour <= 8:
    print("Good evening!")
else:
    print("Good night!")

if hour <= 5:
    print("Good afternoon!")
elif hour <= 8:
    print("Good evening!")
elif period == "AM" and hour <= 4:
    print("It's early!")
elif period == "AM":
    print("Good morning!")
else:
    print("Good night!")

print()

if period == "PM":
    if hour <= 5:
        print("Good afternoon!")
    elif hour <= 8:
        print("Good evening!")
    else:
        print("Good night!")
else:
    if hour <= 4:
        print("It's early!")
    else:
        print("Good morning!")

print()

days_since_release = 14
original_price = 60
greatest_hits = True

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Write a conditional that determines the price of a
# newly-released game, movie, or album based on the time since
# it was released.
#
# Assume that a new release loses $2 off its price for every
# full week since it was released. So, two full weeks (14 days)
# after a $60 game is released, it will cost $56.
#
# However, if the release is considered a "greatest hit", it
# loses value half as fast: after two weeks, it will be $58
# instead of $56.
#
# No release will ever fall to below $20, however, no matter
# how fast it loses value or whether it's a greatest hit.
#
# Add some code below to print the current price of the release.
# For example, with the values above, it would print $58.


# Add your code here! Make sure to print the dollar sign, too.

# if days_since_release == 14 and not greatest_hits:
# current_price = original_price - 4
# print("$" + str(current_price))

# elif days_since_release == 14 and greatest_hits:
# current_price = original_price - 2
# print("$" + str(current_price))
# elif days_since_release > 14 and greatest_hits:
# current_price = original_price <= 20
# print(current_price)
# else:
# print(original_price)

# This code is copied...

dollars_off = 0

if greatest_hits:
    if days_since_release < 7:
        new_total = original_price - dollars_off
    else:
        dollars_off = days_since_release // 7
        new_total = original_price - dollars_off
else:
    if days_since_release < 7:
        new_total = original_price - dollars_off
    else:
        dollars_off = (days_since_release // 7) * 2
        new_total = original_price - dollars_off
if new_total < 20:
    new_total = 20
print("$" + str(new_total))

# A shorter method:
# calculating the amount of loss if greatest hits is True or False

if greatest_hits:
    loss = days_since_release // 7
else:
    loss = days_since_release // 7 * 2

price = original_price - loss

if price > 20:
    print("$" + str(price))
else:
    print("$20")
print()

minimum = 5
maximum = 14
even = True

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.
#
# Write a loop (we suggest a for loop) that prints the numbers
# from minimum to maximum, including minimum and maximum
# themselves. If even is True, print only the even numbers.
# If even is False, print only the odd numbers. You may assume
# minimum will always be less than maximum.
#
# With the initial values for minimum, maximum, and even above,
# this should print 6, 8, 10, 12, 14 -- each number would be on
# its own line, no commas.


# Add your code here!
if even:

    for i in range(minimum, maximum + 1):
        if i % 2 == 0:
            print(i)
else:
    for i in range(minimum, maximum + 1):
        if i % 2 == 1:
            print(i)

print()

for num in range(minimum, maximum + 1):
    if even:
        if num % 2 == 0:
            print(num)
    else:
        if num % 2 == 1:
            print(num)
print()


# Write a function called num_factors. num_factors should
# have one parameter, an integer. num_factors should count
# how many factors the number has and return that count as
# an integer
#
# A number is a factor of another number if it divides
# evenly into that number. For example, 3 is a factor of 6,
# but 4 is not. As such, all factors will be less than the
# number itself.
#
# Do not count 1 or the number itself in your factor count.
# For example, 6 should have 2 factors: 2 and 3. Do not
# count 1 and 6. You may assume the number will be less than
# 1000.


# Add your code here!

def num_factors(number):
    crt = 0
    for i in range(2, number):  # start from 2 instead of 1
        if number % i == 0:
            crt += 1

    return crt


# simple method.... for i in range(2, num):
#         if num % i == 0:
#             count += 1
#     return count

# Ridiculous..spent an hour trying this simple code...I think it is time for me to sleep!!

# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 0, 2, 0, 6, 6, each on their own line.
print(num_factors(5))
print(num_factors(6))
print(num_factors(97))
print(num_factors(105))
print(num_factors(999))

print()


# coding test (Pokemon Experience):

# Imagine you're playing a game in which every action you
# take grants you some number of experience points. There is
# an item called a Lucky Egg that, when used, doubles the
# number of experience points you earn. The company behind
# the game also runs occasional events where they increase
# how many experience points you earn for each action by 50%,
# 100%, or even 200%.
#
# Write a function called find_total_exp. find_total_exp
# should have one positional parameter, a base number of
# experience points. It should also have two keyword
# parameters: lucky_egg, whose default value is False, and
# event_mulitplier, whose default value is 1.
#
# The function should return the number of experience
# points earned based on these two variables. The base number
# of experience points should always be multiplied by the
# event multiplier, and then doubled if lucky_egg is True.
#
# You should convert the final result from a float to an
# integer before returning it. This will automatically round
# down.


# Add your code here!


def find_total_exp(base_number, lucky_egg=False, multiplier=1):
    if not lucky_egg:
        total_exp = base_number * multiplier
        return int(total_exp)
    else:
        total_exp = (base_number * multiplier) * 2
        return int(total_exp)


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# 100
# 200
# 150
# 300
print(find_total_exp(100))
print(find_total_exp(100, lucky_egg=True))
print(find_total_exp(100, multiplier=1.5))
print(find_total_exp(100, lucky_egg=True, multiplier=1.5))

print()

# Coding unit test (UpperCase):

the_string = "I'm a Ramblin' Wreck"

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.
#
# Write some code that will capitalize and print the value of
# the_string. For example, for the initial value of the_string
# above, it should print "I'M A RAMBLIN' WRECK".
#
# You can capitalize a string by calling the_string.upper().
# This will return a capitalized version of the string. (Note
# that this will _not_ modified the_string, but rather just
# return the result if it were to be capitalized.)
#
# However, the_string might not actually be a string! It might
# be an integer, a float, or something else. If that happens,
# then calling the_string.upper() will cause an AttributeError
# to occur. Catch this error and print "The variable was not
# a string!"
#
# Note that you may not use any conditionals in your answer.
# Note also that you should not assume that every error that
# occurs is an Attribute Error! Any other errors should
# not be caught.


# Add your code here!


try:

    print(the_string.upper())
except AttributeError:
    print("The variable was not a string!")

print()


# Coding Unit Test(Remove capital letters):

# Write a function called remove_capitals. remove_capitals
# should accept one parameter, a string. It should return a
# string containing the original string with all the capital
# letters removed. Everything else should be in the same
# place and order as before.
#
# For example:
#
# remove_capitals("A1B2C3D") -> "123"
# remove_capitals("WHAT") -> ""
# remove_capitals("what") -> "what"
#
# Remember, capital letters have ordinal numbers between 65
# ("A") and 90 ("Z"). You may use the ord() function to get
# a letter's ordinal number.
#
# Your function should be able to handle strings with no
# capitals (return the original string) and strings with all
# capitals (return an empty string). You may assume we'll
# only use regular characters (no emojis, formatting
# characters, etc.).


# Write your function here!

def remove_capitals(a_string):
    lower_letters = ""

    for letter in a_string:
        if ord(letter) not in range(65, 91):
            lower_letters += letter
    return lower_letters


print(remove_capitals("A1B2C3D"))
print(remove_capitals("Georgia Institute of Technology"))

# coding Unit Test (Release date):

from datetime import date


def valid_release_date(date, string):
    day = date.weekday()

    if day == 0 and string == "Album":
        return True
    elif day == 1 and string == "Game":
        return True
    elif (day == 2 or day == 6) and string == "Show":
        return True
    elif day == 4 and string == "Movie":
        return True
    elif day == 5 and string == "Play":
        return True
    else:
        return False


print(valid_release_date(date(2018, 7, 11), "Show"))
print(valid_release_date(date(2018, 7, 11), "Movie"))
print(valid_release_date(date(2018, 7, 11), "Pancake"))
print()


# Unit Test :(The  Joyner conjecture):

# The Joyner Conjecture is a not-at-all famous mathematical
# series inspired by the Collatz Conjecture for use in this
# class.
#
# The Joyner Conjecture proceeds as follows:
#
# Start with any number. If the number is divisible by 3,
# divide it by 3. Otherwise, add 2 to the number. Eventually,
# no matter what number you begin with, this series will run
# into 1 or 2. If it runs into 1, it will repeat 1-3 forever.
# If it runs into 2, it will repeat 2-4-6 forever.
#
# For example, imagine we started with the number 5:
# 5 is not divisible by 3, so 5 + 2 = 7
# 7 is not divisible by 3, so 7 + 2 = 9
# 9 is divisible by 3, so 9 / 3 = 3
# 3 is divisible by 3, so 3 / 3 = 1
#
# Start with 5, this sequence converges on 1 in 4 iterations:
# 5 -> 7, 7 -> 9, 9 -> 3, 3 -> 1.
#
# Write a function called joyner. joyner should have one
# parameter, an integer. It should return the number of
# iterations required to reach either 1 or 2 for the first
# time.


# Add your code here!


def joyner(num):
    count = 0

    while num > 2:
        if num % 3 == 0:
            num = num // 3
            count += 1
        elif num % 3 != 0:
            num = num + 2
            count += 1

    return count


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 4, 5, and 10, each on their own lines.
print(joyner(5))
print(joyner(15))
print(joyner(29))

print()


# Coding Unit Test (Valid product code):

# Imagine you're writing the software for an inventory system for
# a store. Part of the software needs to check to see if inputted
# product codes are valid.
#
# A product code is valid if all of the following conditions are
# true:
#
# - The length of the product code is a multiple of 4. It could
#   be 4, 8, 12, 16, 20, etc. characters long.
# - Every character in the product code is either an uppercase
#   character or a numeral. No lowercase letters or punctuation
#   marks are permitted.
# - The character sequence "A1" appears somewhere in the
#   product code.
#
# Write a function called valid_product_code. valid_product_code
# should have one parameter, a string. It should return True if
# the string is a valid product code, and False if it is not.


# Add your code here!

def valid_product_code(valid_string):
    if len(valid_string) % 4 == 0:
        if "A1" in valid_string:
            for char in valid_string:
                if char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                    return False
            return True

        return False
    return False


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: True, True, False, False, False
print(valid_product_code("A12B44BP"))
print(valid_product_code("BFDSAUSA98932RWEFOEWA9FEAA1DSFSF"))
print(valid_product_code("A1BBD5"))
print(valid_product_code("BDD5664S"))
print(valid_product_code("66aBSaA1fdsv"))


# Another method pay attention

# As always, we start by writing the function name and parameters:

def valid_product_code(String):
    # The first thing we want to check is the length of the String. If it is
    # not a multiple of 4, there is not reason for us to do anything as we
    # can simply return False.

    if len(String) % 4 != 0:
        return False
    found = False

    # We create a boolean “found” which will later be used in the code
    #
    # If the String length is a multiple of 4, then we have to iterate through
    # the String and check for two things. Rather than having two for-loops
    # we can check both conditions at the same time. Having two for-loops
    # makes your code inefficient, which is something you do NOT want.
    #
    # We write a for-loop because we know how many times we want to
    # iterate, and notice that our range is from 0 to len(String - 1).
    #
    # Note when you have:
    # in range(0, len(String - 1)) we end at the second last index.

    for index in range(0, len(String) - 1):

        # Now we need.a conditional that will catch any character within the String
        # that is not an uppercase or number.

        if (String[index] < '0') or (String[index] > '9' and String[index] < 'A') or (String[index] > 'Z'):
            return False

        # Notice that there is an and statement when comparing to see if it is greater
        # than ‘9’ but less than ‘A’. This is because of the order of the ASCII table. If
        # we had an “or” instead, the conditional would trigger the String[index] > 9
        # even if the letter was a lowercase.
        #
        # The second conditional is where we look to see if “A1” exists. Since the
        # way we set our for loop allows us to access the appropriate index, we
        # check to see if the current String[index] and String[index] add up to “A1”.
        # If it does, then we set our found variable to be True.
        # The reason why we have a found variable rather than have that condition
        # return True is because f we were to have a product code of “A1btT” it
        # would return True even though it is not a correct product code since the
        # second condition is triggered. Thus, we store the boolean value in found
        # and return that value at the end.
        # We have to initially store the boolean value as False because we have not
        # found “A1” yet. However, when we do, we CAN return True if the product
        # code does not have any lower or non numbers which is checked by
        # our first condition.

        if String[index] + String[index + 1] == "A1":
            found = True

    return found


print(valid_product_code("A12B44BP"))
print(valid_product_code("BFDSAUSA98932RWEFOEWA9FEAA1DSFSF"))
print(valid_product_code("A1BBD5"))
print(valid_product_code("BDD5664S"))
print(valid_product_code("66aBSaA1fdsv"))
