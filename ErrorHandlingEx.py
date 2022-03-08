mystery_value = 9

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Create a program that divides 10 by mystery_value and prints
# the result. In the case that mystery_value is equal to 0,
# print "Not possible". Do not catch any other errors. This
# means there will be an uncaught error in the correct answer!
#
# You may not use any conditionals or the type() function.


# Add your code here!

try:
    mystery_value_2 = 10 / mystery_value
    print(mystery_value_2)
except ZeroDivisionError:
    print("Not possible")
print()

mystery_value = "my string"

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Create a program that divides 10 by mystery_value and
# prints the result. In the case that mystery_value is
# equal to 0, print "Can't divide by zero". If for any other
# reason the operation fails, print "Not possible".
#
# You may not use any conditionals or the type() function.


# Add your code here!
try:
    mystery_value_2 = 10 / mystery_value
    print(mystery_value_2)
except ZeroDivisionError:
    print("Can't divide by zero")
except Exception as error:
    print("Not possible")
print()


# function tests with errors:

def has_a_vowel(a_str):
    for letter in a_str:
        if letter in "aeiou":
            return True
        else:
            return False


has_a_vowel(a_str="beeswax")


# Testing errors:

def has_a_vowel(a_str):
    print("Starting...")
    for letter in a_str:
        print("Checking", letter)
        if letter in "aeiou":
            print(letter, "is a vowel, returning True")
            return True
        else:
            print(letter, "is not a vowel, returning False")
            return False
    print("Done!")


has_a_vowel(a_str="sttttttr")
print()


# Terminating a function too early, fixing the above error..
def has_a_vowel(a_str):
    for letter in a_str:
        if letter in "aeiou":
            return True

    return False
    print("Done!")


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: True, then True, then False, then False, each on
# its own line.
print(has_a_vowel("abba"))
print(has_a_vowel("beeswax"))
print(has_a_vowel("syzygy"))
print(has_a_vowel(""))

print()
# Another exercise with loops within or without try and except:

# Right now, the code below will encounter an error when num
# is 0, but it will not print anything when it does, and then
# it will keep running for num = 1, num = 2, and num = 3
# afterwards. Modify this code so that once it hits an error,
# the loop stops altogether.
#
# You still should not print anything when the error is
# encountered, and the loop definition on line 10 should not
# be changed.


try:

    for num in range(-3, 3):
        print(5 / num)
except:
    pass
print()


# Error handling within functions exercise:

# Write a function called get_integer that takes as input one
# variable, my_var. If my_var can be converted to an integer,
# do so and return that integer. If my_var cannot be converted
# to an integer, return a message that says, "Cannot convert!"
#
# For example, for "5" as the value of my_var, get_integer would
# return the integer 5. If the value of my_var is the string
# "Boggle.", then get_integer would return a string with the
# value "Cannot convert!"
#
# Do not use any conditionals or the type() function.


# Write your function here!

def get_integer(my_var):
    try:
        return int(my_var)
    except Exception as error:
        return "Cannot convert!"


# LESSON:ALWAYS RETURN STATEMENTS WITHIN THE FUNTION, AND THEN PRINT WHILE  CALLING THE FUNCTION OTHERWISE
# NONE WILL BE THE OUTPUT PLUS YOUR PRINT STATEMENT.
# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 5, Cannot convert!, and 5.

print(get_integer("5"))
print(get_integer("Boggle."))
print(get_integer(5.1))
print()
print()


# Coding problem 3.5.6

# Now let's make things a little more challenging.
#
# Last exercise, you wrote a function called word_count that
# counted the number of words in a string essentially by
# counting the spaces. However, if there were multiple spaces
# in a row, it would incorrectly add additional words. For
# example, it would have counted the string "Hi   David" as
# 4 words instead of 2 because there are two additional
# spaces.
#
# Revise your word_count method so that if it encounters
# multiple consecutive spaces, it does *not* count an
# additional word. For example, these three strings should
# all be counted as having two words:
#
# "Hi David"
# "Hi   David"
# "Hi                 David"
#
# Other than ignoring consecutive spaces, the directions are
# the same: write a function called word_count that returns an
# integer representing the number of words in the string, or
# return "Not a string" if the input isn't a string. You may
# assume that if the input is a string, it starts with a
# letter word instead of a space.

# Write your function here!

def word_count(my_string):
    try:
        return len(my_string.split())
    except:
        return "Not a string"


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# Word Count: 4
# Word Count: 2
# Word Count: Not a string
# Word Count: Not a string
# Word Count: Not a string

print("Word Count:", word_count("Four words are here!"))
print("Word Count:", word_count("Hi   David"))
print("Word Count:", word_count(5))
print("Word Count:", word_count(5.1))
print("Word Count:", word_count(True))
print()



