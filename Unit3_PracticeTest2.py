have_food = True
have_drinks = True
having_a_party = False

if not (have_food or have_drinks) or having_a_party:
    print("Go grocery shopping!")
else:
    print("Stay home!")
print()

age = 48
born_in_the_us = False
time_since_citizenship = 9

if age > 34 and born_in_the_us:
    print("You can run for President in the US!")
if age > 24 and time_since_citizenship > 6:
    print("You can run for Representative in the US!")
if age > 29 and time_since_citizenship > 8:
    print("You can run for Senator in the US!")

    print()

like_dogs = False
like_cats = False
if like_dogs:
    print("Get a dog!")
elif like_cats:
    print("Get a cat!")

print()

for i in range(1, 21):
    print(i)

print()
some_string = "Applegate"

for c in some_string:
    print(c)

i = 10
while i >= 1:
    print(i)
    i -= 1

i = 1
j = 100
while i < j:
    i *= 3
    print(i)
print()

i = 0
j = 12
while i < j:
    print(i)
    i += 3
print()

i = 1
j = 20
for num in range(i, j, 4):
    print(num)

print()
i = 5
j = 3
for num_1 in range(1, i):
    for num_2 in range(0, j):
        print(num_1)
print()


def sum_3(a_num_1, a_num_2, a_num_3):
    return a_num_1 + a_num_2 + a_num_3


print(sum_3(7, 4, 4))

print()


def merge_strings(a_string, b_string, reverse=False, Capitalize=True):
    if reverse:
        return b_string + a_string
    elif Capitalize:
        return a_string.isupper() + b_string.isupper()
    else:
        return a_string + b_string


print(merge_strings("cat", "dog"))
print(merge_strings("sheep", "wolf", reverse=True))
print(merge_strings("cow", "goat", reverse=False, Capitalize=False))

print()


def my_q(num, den, rec=False, neg=False):
    if rec:
        if neg:
            return den / -num
        else:
            return den / num
    else:
        if neg:
            return num / -den
        else:
            return num / den


print(my_q(20.0, 10.0, neg=True))
print(my_q(20.0, 10.0, rec=True))

print()


def my_q(num, den, rec=False, neg=False):
    if neg:
        den *= -1
    if rec:
        return den / num
    else:
        return num / den


result = my_q(2.0, 1.0, neg=True) * my_q(2.0, 1.0, rec=True)
print(result)
print()

start = 0
finish = 10

for i in range(start, finish + 1):
    if i % 2 == 0:
        print(i)

print()

days_late = 15
in_demand = True

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Write a conditional that decides the amount of a library fine
# based on an overdue book. The fine is 1 dollar per day late
# for the first 10 days, and 2 dollars per day for every day
# after that. If the book is considered an "in demand" book,
# the fine is doubled.
#
# Print the cost of the library fine, including a dollar sign.
# If the book is not late, print $0.
#
# Under the original values above, this should print $40:
# $10 for the first 10 days late, $10 for the next 5 days late,
# and doubled because the book is in demand.


# Add your code here! Make sure to print the dollar sign, too.

dollar_fine = 0

if days_late == 10:
    dollar_fine = 10 * 1
elif days_late > 10:
    dollar_fine = (dollar_fine * 2)
elif in_demand:
    dollar_fine = dollar_fine * 2
else:
    print(dollar_fine)

print()

minimum = 5
maximum = 14

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.
#
# Write a loop (we suggest a for loop) that prints all the
# even numbers from minimum to maximum. Each number should be
# printed on its own line, and you should print both minimum
# and maxmimum themselves if they are even. You may assume
# minimum will always be less than maximum.
#
# With the initial values for minimum and maximum above, this
# should print 6, 8, 10, 12, 14 -- each number would be on its
# own line, no commas.


# Add your code here!

for i in range(minimum, maximum + 1):
    if i % 2 == 0:
        print(i)

print()


# Write a function called is_prime. is_primse should take
# as input one integer. It should return True if the integer
# is prime, False if the integer is not prime. You may
# assume the integer will be greater than 2 and less than
# 1000.
#
# Remember, a prime number is one into which no number is
# divisible besides 1 and itself. For example, 6 is not
# prime because it is divisible by 2 and 3. 7 is prime
# because it is only divisible by 1 and itself.
#
# HINT: Remember, once you find a _single_ factor of the
# number, you can return False: it only takes one factor
# to make the number not prime.


# Add your code here!


def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        else:
            return True


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: True, False, True, False, True, False
print(is_prime(5))
print(is_prime(6))
print(is_prime(97))
print(is_prime(105))
print(is_prime(997))
print(is_prime(999))

print()


# Write a function called find_final_price. find_final_price
# should have two positional parameters: a price and a sales
# tax rate. It should also have a keyword parameter called
# coupon_code, with a default value of 0.
#
# find_final_price should return the final price of the item,
# which is the initial price plus the sales tax (price times
# tax rate) minus the coupon code.
#
# Round the final answer to two decimal places. You can do
# that with final_price = round(previous_price, 2).


# Add your code here!
def find_final_price(price, sales_tax_rate, coupon_code=0):
    initial_price = price + (price * sales_tax_rate)
    final_price = initial_price - coupon_code
    final_price = round(final_price, 2)
    return final_price


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# 10.70
# 5.70
print(find_final_price(10.0, 0.07))
print(find_final_price(10.0, 0.07, coupon_code=5.0))

print()

the_string = "wreck"

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.
#
# The string class has a method called islower which returns
# True if a string is all lower case, false if it is not.
# For example, if the_string = "Ramblin", then calling the
# method the_string.islower() would return False. If instead
# the_string was "wreck", the_string.islower() would return
# True.
#
# Write some code that uses islower to print True if
# the_string is all lower case, False if it is not. However,
# if the_string isn't actually a string, this would instead
# cause an AttributeError. Catch that error and instead
# print the message "Only strings can be lowercase!".
#
# Note that you may not use any conditionals in your answer.
# Note also that you should not assume that every error that
# occurs is an attribute error: any other errors should not
# be caught.


# Add your code here!


try:
    print(the_string.islower())
except AttributeError:
    print("Only strings can be lowercase!")

print()


# Write a function called get_numerals. get_numerals should
# accept one parameter, a string. It should return a string
# containing only the numerals from the original string:
# no letters, punctuation marks, or spaces.
#
# Remember, numerals have ordinal numbers between 48 ("0")
# and 57 ("9"). You may use the ord() function to get
# a letter's ordinal number.
#
# Your function should be able to handle strings with no
# numerals (return an empty string) and strings with all
# numerals (return the original string). You may assume
# we'll only use regular characters (no emojis, formatting
# characters, etc.).


# Write your function here!

def get_numerals(my_string):
    numerals = ""

    for letter in my_string:
        if ord(letter) in range(48, 58):
            numerals += letter
    return numerals


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# 1301
#
# 8675309
print(get_numerals("CS1301"))
print(get_numerals("Georgia Institute of Technology"))
print(get_numerals("8675309"))
print()


# Write a function called check_date. check_date should
# require two positional parameters: a string representing
# the name of a month, and an integer representing a date.
# check_date should also have a keyword parameter called
# is_leap_year, assumed to be False, representing whether or
# not it's a leap year.
#
# Return True if the date is a valid calendar date. Return
# False if it is not. A date may not be a valid calendar
# date if the month isn't a real month, or if that date does
# not exist for that month. You can see some examples at the
# end of this file.
#
# Remember: 30 days has September, April, June, and November.
# All the rest have 31, except February, which has 28, until
# Leap Year gives it 29.
#
# You may assume that day will be greater than 0 (you don't
# need to check negative or zero values for day).


# Write your function here!

def check_date(name_month, date, is_leap_year=False):
    if date in range(1, 29) and name_month == "February" and not is_leap_year:
        return True
    elif date == 29 and name_month == "February" and is_leap_year:
        return True
    elif date in range(1, 32) and name_month in ("January", "March", "May", "July", "August", "October", "December"):
        return True
    elif date in range(1, 31) and name_month in ("April", "June", "September", "November"):
        return True

    else:
        return False


print()

# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: True, True, False, False, each on their own line.
print(check_date("January", 31))
print(check_date("February", 29, is_leap_year=True))
print(check_date("Techtember", 15, is_leap_year=True))
print(check_date("June", 31))

print()


# The Collatz Conjecture is a famous sequence in mathematics
# proposed by Lothar Collatz. It proceeds as follows:
#
# Start with any number. If the number is even, divide it by
# 2. If the number is odd, triple it and add one. Repeat.
# Eventually, no matter what number you begin with, this
# sequence will converge on 1 (and if you continue repeating
# it, you'll repeat 1-4-2 infinitely).
#
# For example, imagine we started with the number 21:
# 5 is odd, so 5 * 3 + 1 = 16
# 16 is even, so 16 / 2 = 8
# 8 is even, so 8 / 2 = 4
# 4 is even, so 4 / 2 = 2
# 2 is even, so 2 / 1 = 1
#
# Starting with 5, this sequence converges on 1 in 5
# iterations: 5 to 16, 16 to 8, 8 to 4, 4 to 2, and 2 to 1.
#
# Implement a function called collatz. collatz should take
# as input an integer, and return the number of iterations
# it takes for the Collatz sequence to reach 1 from that
# number. For example, collatz(5) would return 5 because
# it took 5 iterations to converge on 1.


# Add your code here!


def collatz(num):
    if num <= 0:
        raise ValueError("Only positive, non-zero integers are allowed!")
    count = 0
    while num != 1:
        if num % 2:
            num = num * 3 + 1
        else:
            num //= 2
        count += 1
    return count


# def collatz_sequence(n):
# collatz_list=list() #list to store the values of sequence

# while (n!=1) :
# collatz_list.append(n)
# if n is even
# if (n%2==0) :
# n=n//2
# else:
# if n is odd
# n=(3*n)+1
# collatz_list.append(1)  #print 1 in the end
# l=len(collatz_list)

# print("The length of collatz sequence is", l)

# print("The sequence is :")

# for i in range(0,l):
# print(collatz_list[i])

# driver code
# collatz_sequence(11)

# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 5, 17, and 23, each on their own lines.
# print(collatz(5))
# print(collatz(15))
# print(collatz(25))

print()


# Write a function called product_code_check. product_code_check
# should take as input a single string. It should return a boolean:
# True if the product code is a valid code according to the rules
# below, False if it is not.
#
# A string is a valid product code if it meets ALL the following
# conditions:
#
# - It must be at least 8 characters long.
# - It must contain at least one character from each of the
#   following categories: capital letters, lower-case letters,
#   and numbers.
# - It may not contain any punctuation marks, spaces, or other
#   characters.


# Add your code here!
def product_code_check(valid_string):
    SpecialSym = "!@#$%&()-_[]{};':\",./<>?"
    val = True

    if len(valid_string) < 8:
        return False

    if not any(char.isdigit() for char in valid_string):
        return False

    if not any(char.isupper() for char in valid_string):
        return False

    if not any(char.islower() for char in valid_string):
        return False
    if any(char in " " for char in valid_string):
        return False
    if any(char in SpecialSym for char in valid_string):
        return False

    else:
        return val


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: True, True, False, False, False
print(product_code_check("g00dlONGproductCODE"))
print(product_code_check("fRV53FwSXX663cCd"))
print(product_code_check("2shOrt"))
print(product_code_check("alll0wercase"))
print(product_code_check("inv4l1d CH4R4CTERS~"))
