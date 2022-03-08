# Unit 2 practice set


# Imagine you're writing the software that controls the speed
# of a ceiling fan. The user changes the fan's speed by
# pulling a string. Pulling the string increases the fan's =
# speed by 1, unless it's already at the maximum speed. If
# it's already at the maximum speed, it changes the speed
# back to 0.
#
# Write a function called pullString. pullString should take
# two parameters: a current speed, and a maximum speed, both
# integers. pullString should return the new fan speed
# according to the reasoning above.

# You may assume that the input will be integers. You should
# also assume that the fan's speed *can* equal the maximum
# speed, but it *cannot* exceed the maximum speed. You may
# thus assume that you will never be given a currentSpeed
# higher than maxSpeed.


# Write your function here!

def pullString(current_speed, maximum_speed):
    fan_speed = current_speed + 1
    if current_speed == maximum_speed:
        return 0
    else:
        return fan_speed


# The code below will test your function. It isn't used for
# grading, so you can change or remove it if you'd like. As
# written, these three lines should print 3, 5, and 0.
print(pullString(2, 5))
print(pullString(4, 5))
print(pullString(7, 7))
print()


# NumCombinations problem:

# A common formula in probability and statistics is the
# formula for the number of possible combinations of r
# objects from a set of n objects. For example, the question,
# "How many possible 2-card hands can you deal from a deck of
# 52 unique cards?" is saying, "How many combinations of 2
# can you make from a set of 52?"
#
# The formula for the number of combinations of length r from
# a set of n objects is:
#
#  numCombinations = n! / r!(n-r)!
#
# The ! mark is the symbol for factorial. Factorial means the
# product of the number times every number between itself and
# 1. For example, 5! is 120: 5 * 4 * 3 * 2 * 1 = 120.
#
# Write a function called numCombinations with two parameters:
# n, the number of objects from which to choose, and r, the
# number of objects to choose. numCombinations should return
# the number of combinations according to the formula above.
# Don't worry if you don't fully understand what combinations
# are -- just focus on implementing a function that solves
# that formula given n and r.
#
# You may *not* use Python's built-in factorial method to
# complete this; you should implement that yourself.
#
# Hint: We'd suggest writing two functions: factorial() and
# numCombinations(). Then, call factorial() in your code for
# numCombinations(). You don't have to do this, but it will
# make your answer a little easier!
#
# Hint 2: Remember to put parentheses around the denominator.


# Write your numCombinations function (and any other functions)
# here!

## This code is copied....

# first define a function to hold the factorial using the while loop,
# you can use the for loop for or conditionals
# if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

def fact(k):
    f = i = 1
    while i <= k:
        f = i * f
        i += 1
    return f


# Then call the fact() into the numCombination function to calculate the result(n! r!(n-r)!

def numCombinations(n, r):
    num = fact(n)
    den = fact(n - r)
    den = fact(r) * den
    comb = num / den
    return comb


# The lines below will test your code. They are not used for
# grading, so feel free to modify them. As written, they should
# print: 1326.0, 252.0, and 4.0, each on their own line.
print(numCombinations(52, 2))
print(numCombinations(10, 5))
print(numCombinations(4, 1))

print()


# Extra Practice problem 3:
# An object's weight is defined as its mass times the gravity
# on the planet where it sits. We tend to assume that the
# planet is earth and its gravity is 9.807 m/s^2. However,
# sometimes we might want to calculate an object's weight on
# a different planet.
#
# Write a function called calculateWeight. calculateWeight
# should have three parameters: mass, planet, and gravity.
# planet and gravity should be keyword parameters: by
# default, they should take the values "Earth" (a string) and
# 9.807 (a float). However, they should be able to be
# overriden to let us calculate weights on other planets.
#
# The function should return a string that looks like this:
# "A [mass] kg object weighs [weight] Newtons on [planet]."
# You should round the weight to two decimal points. You
# can do this by calling round() on the weight, e.g.
# roundedWeight = round(weight, 2). The 2 dictates how
# many decimal points should be included.
#
# For example:
#
# calculateWeight(10.0) ->
#       "A 10.0 kg object weighs 98.07 Newtons on Earth."
#
# calculateWeight(5.0, planet="Jupiter", gravity=24.79) ->
#       "A 5.0 kg object weighs 24.79 Newtons on Jupiter."
#
# Hint: If you're having trouble with creating the string to
# return, here's the first part:
# result = "A " + str(mass) + " kg object weighs " ...


# Write your function here!

def calculateWeight(mass, planet="Earth", gravity=9.807):
    object_weight = mass * gravity
    object_weight = round(object_weight, 2)
    return "A {} kg object weighs {} Newtons on {}.".format(mass, object_weight, planet)


# The lines of code below will test your function. They are
# not used for grading, so feel free to change them. As
# written, these lines should output the two lines of output
# shown above.
print(calculateWeight(10.0))
print(calculateWeight(5.0, planet="Jupiter", gravity=24.79))

print()


# Imagine you're writing a cash register application. To make
# interaction easier on the user, it doesn't have separate
# areas for passwords, PIN numbers, or cash totals --
# instead, it looks at what the cashier enters and infers
# whether it's their PIN number, their password, or the cash
# total for a transaction.
#
# The register makes this decision with the following rules:
#
# - If the cashier entered only digits, then it's a PIN
#   number.
# - If the cashier entered a decimal number, then it's the
#   transaction amount.
# - If the cashier entered anything else, then it's their
#   password.
#
# Write a function named interpretCashier. interpretCashier
# should take one parameter as input, which will always be
# a string initially.
#
# - If the string entered represents a PIN number, return
#   "PIN".
# - If the string entered represents a transaction amount,
#   return "Transaction".
# - If the string entered represents a password, return
#   "Password".
#
# Hint: There is a very easy way to do this, and a very hard
# way to do this. Remember, this test is on control
# structures, not strings.


# Write your function here!
def interpretCashier(a_string):
    # if a_string.isnumeric():
    # return "PIN"
    # elif a_string.isdecimal():
    # return "Transaction"

    # else:
    # return "Password"

    numlist = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    allnumber = False
    foundchara = False
    i = 0
    for chara in a_string:
        if chara in numlist:
            allnumber = True
        else:
            foundchara = True
            nextchara = a_string[i + 1]
            break
        i += 1
    if foundchara == True and chara == "." and nextchara != ".":
        return "Transaction"
    elif foundchara == False and allnumber == True:
        return "PIN"
    else:
        return "Password"


# The lines of code below will test your function. It is not
# used for grading, so feel free to change it. As written,
# these lines should print Transaction, PIN, and Password,
# each on a separate line.
print(interpretCashier("24.59"))
print(interpretCashier("123456"))
print(interpretCashier("my$up3rs3cur3p4$$w0rd"))

print()


# A simpler method: use try and except

def interpretCashier(a_string):
    try:
        int(a_string)
        return "PIN"

    except ValueError:
        try:
            float(a_string)
            return "Transaction"
        except:
            return "Password"


print(interpretCashier("24.59"))
print(interpretCashier("123456"))
print(interpretCashier("my$up3rs3cur3p4$$w0rd"))

print()


# coding extra practice 5:

# Write a function called remainder. remainder should take
# two parameters: a dividend and a divisor. It should return
# the remainder when you divide the dividend by the divisor.
#
# For example:
# remainder(9, 3) -> 0
# remainder(8, 3) -> 2
# remainder(7, 3) -> 1
# remainder(6, 3) -> 0
#
# You may not use Python's built-in modulus operator. The
# symbol for that operator should not appear anywhere in your
# code.
#
# You may assume both dividend and divisor will be greater
# than 0


# Add your function here!
def remainder(dividend, divisor):
    if dividend > 0 and divisor > 0:
        result = dividend - divisor * (dividend // divisor)
        return result


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 0, 3, 2
print(remainder(9, 3))
print(remainder(11, 4))
print(remainder(27, 5))


# Coding practice 6:

# Write a function called sortString. sortString should take
# one parameter as input, a string. If the input is not a
# string, sortString should return the string "Not a string!"
# If the input is a string, sortString should return a four-
# line string according to the following directions:
#
# - On the first line should be each capital letter in the
#   string, in the order in which they appear.
# - On the second line should be each lower-case letter in
#   the string, in the order in which they appear.
# - On the third line should be each punctuation mark or
#   numeral in the string, in the order in which they
#   appear.
# - On the fourth line should be an integer representing
#   how many spaces were found in the string.
#
# There should be no other text in the string that you output
# besides these four lines and the line breaks between them.
# To insert a line break into a string, insert the character
# sequence "\n". For example, line1 + "\n" + line2 would give
# a string with the first two lines and a line break in
# between. You may assume that the string will only be
# letters, spaces, and punctuation -- no numbers, line breaks,
# tabs, etc.
#
# For example, calling sortString("Hello, world!!1" should
# return: "H\nelloworld\n,!!1\n1", which would look like this
# when printed:
# H
# elloworld
# ,!!1
# 1
#
# Hint: Use the ord() function! Remember, when you pass a
# one-character string into ord(), it returns a number.
#
# - Lower-case letters will return a number from 97 to 122.
# - Upper-case letters will return a number from 65 to 90.
# - Puncutation marks and numbers will return a number from
#   33 to 64.
# - Spaces will return the number 32.
#
# So, you can check if a letter is lowercase by seeing if
# ord(letter) is between 97 and 122 (inclusive; 97 is 'a',
# 122 is 'z'), and so on for uppercase and punctuation.
#
# Hint 2: Build up three separate strings (one for
# uppercase, one for lowercase, and one for punctuation),
# then combine them and the count of the number of spaces
# into a string to return at the end.


# Write your sortString function here!

def sortString(my_string):
    lower_letter = ""
    upper_letter = ""
    punct = ""
    spaces = ""
    try:
        if str(my_string):
            for letter in my_string:
                if ord(letter) in range(65, 91):
                    upper_letter += letter
                elif ord(letter) in range(97, 123):
                    lower_letter += letter


                elif ord(letter) in range(33, 65):
                    punct += letter
                elif ord(letter) == 32:
                    spaces += letter
        return upper_letter + "\n" + lower_letter + "\n" + punct + "\n" + str(spaces.count(" "))
    except TypeError:
        return "Not a string!"


# The line of code below will test your function. It is not
# used for grading, so feel free to modify it. As written,
# it should print:
# ZOMGHCS
# ello
# ,1301!!
# 2
print(sortString("ZOMG Hello, CS1301!!"))

print()
# Coding practice 7:

int1 = 7
int2 = 5

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Write a conditional that will print one of the following
# messages:
#
# - If the value of int1 is greater than the value of int2,
#   print "int1 is greater" (without the quotes).
# - If the value of int2 is greater than the value of int1,
#   print "int2 is greater" (without the quotes).
# - If the two values are equal, print "int1 and int2 are
#   equal" (without the quotes).
#
# With the initial values above, this should print "int1 is
# greater".


# Add your code here!


if int1 > int2:
    print("int1 is greater")
elif int2 > int1:
    print("int2 is greater")
else:
    print("int1 and int2 are equal")

print()
# coding practice 8:

driver_speed = 51
speed_limit = 55
school_zone = False


# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Write a conditional that decides the price of a speed ticket
# depending on the driver's speed, the speed limit, and
# whether or not they were in a school zone.
#
# The reasoning that determines the price of the ticket is:
#
# - $100 for speeding at all (any instance where driver_speed
#   is greater than speed limit).
# - $10 dollars per mile over the speed limit the driver was
#   going.
# - 2x the value otherwise if the violation occurred in a
#   school zone, as represented by the value of school_zone.
#
# Print the cost of the speeding ticket. If the driver was not
# speeding, print $0.
#
# Under the original values above, this should print $240:
# $100 for speeding, $20 for going 2mph above the speed limit,
# and x2 for it occurring in a school zone.


# Add your code here! Make sure to print the dollar sign, too.

def SpeedTicket(ticket_cost_1=None):
    initial_cost = 100

    if driver_speed > speed_limit and school_zone:
        ticket_cost_1 = initial_cost + (driver_speed - speed_limit) * 10
        final_ticket_cost = ticket_cost_1 * 2
        return "$" + str(final_ticket_cost)
    elif driver_speed > speed_limit and not school_zone:
        ticket_cost_1 = initial_cost + (driver_speed - speed_limit) * 10
        return "$" + str(ticket_cost_1)

    else:
        return "$" + "0"


print(SpeedTicket())

print()

# Coding practice 9:

minimum = 5
maximum = 10

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.
#
# Write a loop (we suggest a for loop) that prints all the
# numbers from minimum to maximum. Each number should be
# printed on its own line, and you should print both minimum
# and maxmimum themselves. You may assume minimum will always
# be less than maximum.
#
# With the initial values for minimum and maximum above, this
# should print 5, 6, 7, 8, 9, 10 -- each number would be on
# its own line, no commas.


# Add your code here!

for num in range(minimum, maximum + 1):
    print(num, end='\n')

print()

# coding practice 10:


n = 5


# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Write some code that will find and print the factorial of
# the number given by n above. You may not import anything
# from the Python math library.
#
# Hint: Use a while loop, but be careful to avoid an infinite
# loop!


# Add your code here!

def fact(n):
    f = i = 1
    while i <= n:
        f = i * f
        i += 1
    return f


print(fact(n))
print()


# coding problem 11 and 12:

# Write a function called find_weight. find_weight should
# take one parameter, a float that represents the mass of
# an object in kilograms. It should return the weight of
# the object on earth.
#
# Remember, the formula for weight is mass * gravity. You
# should use 9.81 as the value for gravity on earth. If
# you find Python is making rounding errors, try reversing
# the order in which you multiply the numbers.


# Add your code here!

def find_weight(mass, gravity=9.81):
    weight_kg = mass * gravity
    return weight_kg


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# 88.29
# 11.772
print(find_weight(9.0))
print(find_weight(1.2))
print()

# Coding problem 13:

list_sum = 7
list_count = 0


# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.
#
# The variables above give the sum of all numbers in a list,
# and the count of how many numbers were in the list. Your
# goal is to find their average.
#
# However, if list_count is 0, then we can't divide list_sum
# by list_count. In this case, you should print "Can't divide
# by zero!" Otherwise, you should print the average.
#
# Note that you may not use any conditionals in your answer.
# Note also that you should not assume that every error that
# occurs is a divide-by-zero error: any other errors should
# not be caught.


# Add your code here!


def average(list_sum, list_count):
    try:
        average_count = list_sum / list_count
        return average_count
    except ZeroDivisionError:
        return "Can't divide by zero!"


print(average(list_sum, list_count))
print()

# coding problem 14:

input_string = "1234"


# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Imagine that you're writing some software for a check-out
# register. The software tries to guess what information was
# entered based on its structure:
#
# - If the information entered as all numbers, then it's a
#   PIN number.
# - If the information entered was a number with a decimal,
#   it's a transaction amount.
# - If the information entered was neither, it's a password.
#
# Write some code to figure out which of these types of
# information the inputted string is. Print "PIN" for PIN
# number, "amount" for transaction amount, or "password" for
# password. You may assume these are the only three possible
# outcomes.
#
# Hint: You can do this however you want, but error handling
# will be easier than using conditionals.


# Add your code here!


def Register(input_string):
    try:
        int(input_string)
        return "PIN"

    except ValueError:
        try:
            float(input_string)
            return "amount"
        except:
            return "password"


print(Register(input_string))
print()


# Coding problem 15:
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


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: True, True, False, False, each on their own line.
print(check_date("December", 1))
print(check_date("February", 29, is_leap_year=True))
print(check_date("Techtember", 15, is_leap_year=True))
print(check_date("June", 31))

print()


# coding problem 16:

# Write a function called get_capitals. get_capitals should
# accept one parameter, a string. It should return a string
# containing only the capital letters from the original
# string: no lower-case letters, numbers, punctuation marks,
# or spaces.
#
# Remember, capital letters have ordinal numbers between 65
# ("A") and 90 ("Z"). You may use the ord() function to get
# a letter's ordinal number.
#
# Your function should be able to handle strings with no
# capitals (return an empty string) and strings with all
# capitals (return the original string). You may assume
# we'll only use regular characters (no emojis, formatting
# characters, etc.).


# Write your function here!


def get_capitals(a_string):
    upper_letter = ""
    if str(a_string):
        for letter in a_string:
            if ord(letter) in range(65, 91):
                upper_letter += letter
        return upper_letter


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# CS
# GIT
print(get_capitals("CS1301"))
print(get_capitals("Georgia Institute of Technology"))

print()


#
# Sum of all evens: Coding extra practice 17

# Write a function called sum_evens. sum_evens should take
# two parameters: a minimum and a maximum. It should add up
# all the even numbers between minimum and maximum and
# return the sum.
#
# sum_evens should work inclusively: both the minimum and
# the maximum should be added if they are even. For example,
# sum_evens(2, 6) -> 12 (2 + 4 + 6 = 12)


# Add your function here!
def sum_evens(min, max):
    sumEven = 0

    for num in range(min, max + 1):
        if num % 2 == 0:
            sumEven += num
    return sumEven


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 12, 0, 66, each on their own line.
print(sum_evens(2, 6))
print(sum_evens(-2, 2))
print(sum_evens(5, 17))

print()


# Collatz conjecture, function: coding extra practice 18:

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
# This code is copied**
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


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 5, 17, and 23, each on their own lines.
print(collatz(5))
print(collatz(15))
print(collatz(25))

print()


# Is Prime function: Coding extra practice 19:

# Write a function called is_prime. is_prime should take
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


# Password_check again: coding extra practice 20:

# Write a function called password_check. password_check should
# take as input a single string. It should return a boolean:
# True if the password is a valid password according to the rules
# below, False if it is not.
#
# A string is a valid password if it meets ALL the following
# conditions:
#
# - It must be at least 8 characters long.
# - It must contain at least one character from each of the
#   following categories: capital letters, lower-case letters,
#   numbers, and punctuation. For punctuation, the following
#   punctuation marks are acceptable: !@#$%&()-_[]{};':",./<>?
# - It may not contain any characters that do not fit into the
#   four categories above. This includes any punctuation marks
#   not listed in the bullet point above, spaces, and any other
#   character.


# Add your code here!
# Finally got it!! wooow...

def password_check(password):
    SpecialSym = "!@#$%&()-_[]{};':\",./<>?"
    val = True

    if len(password) < 8:
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char in SpecialSym for char in password):
        return False
    if any(char in " " for char in password):
        return False
    if any(char in "`" for char in password):
        return False

    else:
        return val


# Below are some lines of code that will test your function.


# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: True, True, False, False, False
print(password_check("tHIs1sag00d.p4ssw0rd."))
print(password_check("3@t7ENZ((T"))
print(password_check("2.shOrt"))
print(password_check("all.l0wer.case"))
print(password_check("inv4l1d CH4R4CTERS~"))
print(password_check("""6Y07wH3pI`i8x{"""))
