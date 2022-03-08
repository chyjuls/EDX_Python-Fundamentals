my_other_variable = 1

try:
    result = 10 // my_var
    print(result)
except:
    print("An error occurred!")
print("Done!")

print()

my_var_2 = 1

try:
    result = 10 // my_var_2
    print(result)
except (ZeroDivisionError, TypeError):
    print("An expected error occurred!")
else:
    print("No errors occurred!")
finally:
    print("Closing down...")
print("Done!")
print()

i = -2
j = 2

try:
    while i < j:
        print(j // i)
        i += 1
except:
    print("An error occurred!")
print("Done!")
print()

# Coding problem 3.5.1:

words = ["dog", "sparrow", "cat", "frog"]

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# This program is supposed to print the location of the 'o'
# in each word in the list. However, line 22 causes an
# error if 'o' is not in the word. Add try/except blocks
# to print "Not found" when the word does not have an 'o'.
# However, when the current word does not have an 'o', the
# program should continue to behave as it does now.
#
# Hint: don't worry that you don't know how line 18 works.
# All you need to know is that it may cause an error.
#
# You may not use any conditionals.


# Fix this code!

for word in words:

    try:
        print(word.index("o"))
    except:
        print("Not found")

print()
# coding problem 3.5.2

mystery_value = 5

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Write a program that divides mystery_value by mystery_value
# and prints the result. If that operation results in an
# error, divide mystery_value by (mystery_value + 5) and then
# print the result. If that still fails, multiply mystery_value
# by 5 and print the result. You may assume one of those three
# things will work.
#
# You may not use any conditionals.
#
# Hint: You're going to want to test one try/except structure
# inside another! Think carefully about whether the second
# one should go inside the try block or the except block.


# Add your code here!
try:
    result_1 = mystery_value / mystery_value
    print(result_1)

except:
    try:
        result_2 = mystery_value / (mystery_value + 5)
        print(result_2)
    except:
        result_3 = mystery_value * 5
        print(result_3)
print()

# coding problem 3.5.3

given_items = ["one", "two", 3, 4, "five", ["six", "seven", "eight"]]

# Write a program that iterates through the items in the
# given list. For each item, you should attempt to iterate
# through the item and print each character seperately.
#
# If this second part fails, print "Not iterable" -- but
# even if the second part fails, you should still go on
# to the next item in the list.
#
# Hint: Although we'll cover lists more in Unit 4, all
# you need to know right now is that this syntax will run
# a loop over a list, a string, or any other iterable
# type of information:
#
#  for item in given_items:
#
# To iterate over the items in 'item', you can do the
# same thing: for subitem in item:
#
# Start out by building the nested for-each loops that
# you'll need. Then, identify where the error is
# occurring to figure out where to put the try-except
# structure.
#
# This one's tricky, but you can do it!


# Add your code here!

for item in given_items:

    try:
        for subitem in item:
            print(subitem)
    except:
        print("Not iterable")

print()


# coding problem 3.5.4


# In Chapter 3.4, we wrote a function called find_pressure
# that calculated pressure given number of moles,
# temperature, volume, and optionally, a value for R. If no
# value was given for R, we assumed its value should be
# 0.082057.
#
# However, as written, that function could crash: what about
# when the user enters a Volume of 0? That would cause a
# ZeroDivisonError! (In addition to breaking the laws of
# physics, but there's no Python error for that.)
#
# Revise that find_pressure function to catch that error. If
# that error occurs, return the string "Volume must be
# greater than 0." Otherwise, the function should work just
# as it did before.
#
# Feel free to copy your answer to that exercise and work
# from there. If you'd prefer to start from scratch, remember:
# you're creating a function called find_pressure that returns
# a value for pressure given variables n, T, V, and optionally
# R, according to this formula:
#
# Pressure = (nRT) / V
#
# You may not use a conditional. R should have a default value
# of 0.082057.


# Write your function here!
# do not forget to call your default parameter using "="
def find_pressure(num_of_moles, temp, volume, R=0.082057):
    try:
        result = (num_of_moles * R * temp) / volume
        return result
    except Exception as error:
        return "Volume must be greater than 0."


# You may use these lines to test your function. With the
# values initially supplied here, your function should return
# "Volume must be greater than 0."
test_n = 10
test_T = 298
test_V = 0
test_R = 62.364  # Torr!

print("Result:", find_pressure(test_n, test_T, test_V, R=test_R))

print()


# coding problem 3.5.5

# We've come a long way in this unit! You've learned about
# conditionals, loops, functions, and error handling. To end
# the unit, let's do a couple problems that tie all these
# concepts together.
#
# Write a function called word_count. word_count takes as
# input a string called my_string, and returns as output the
# number of words in the string. For the purposes of this
# problem, you can assume that every space indicates a new
# word; so, the number of words should be one more than the
# number of spaces. You may also assume that any strings are
# not empty, so there should always be at least one word if
# my_string is a string.
#
# Note, though, that it could be the case that a non-string
# is accidentally passed in as the argument for my_string. If
# that happens, an error will arise. If such an error arises,
# you should instead return "Not a string". Otherwise,
# return an integer representing the number of words in the
# string.


# Write your function here!
# INDENTATION MATTERS!!

def word_count(my_string):
    try:
        count = 1
        for i in my_string:

            if i == " ":
                count += 1

        return count


    except:
        return "Not a string"


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# Word Count: 4
# Word Count: 1
# Word Count: 7
# Word Count: Not a string
# Word Count: Not a string
# Word Count: Not a string

print("Word Count:", word_count("Four words are here!"))
print("Word Count:", word_count("One."))
print("Word Count:", word_count("There are seven words in this sentence."))
print("Word Count:", word_count(5))
print("Word Count:", word_count(5.1))
print("Word Count:", word_count(True))

print()


# EASIER METHOD:

# -----------------------------------------------------------
# Here are a few alternate approaches to this problem. First,
# Python has a built-in method that counts the number of
# characters in a string. We still need to do our error
# handling, but we don't have to manually count spaces:

def word_count(my_string):
    try:
        return my_string.count(" ") + 1
    except:
        return "Not a string"


# We could also use the split method, which we'll learn about
# in chapter 4.2. The split method splits a string up into
# a list of multiple smaller strings, divided wherever a
# certain character occurs. So, if we split by spaces, then
# the number of strings that results is the number of words:

def word_count(my_string):
    try:
        return len(my_string.split(" "))
    except:
        return "Not a string"


# There are other ways to do this, too, but these are two
# common ones!

print("Word Count:", word_count("Four words are here!"))
print("Word Count:", word_count("One."))
print("Word Count:", word_count("There are seven words in this sentence."))
print("Word Count:", word_count(5))
print("Word Count:", word_count(5.1))
print("Word Count:", word_count(True))

print()
print()


# For Coding problem 3.5.6 go to file ErrorHandlingEx-another method


def word_count(my_string):
    try:

        word_count = 1

        # Notice first that we're using a for loop instead of a
        # for-each loop. That's because we want to know the index
        # of each letter as we look at it. Notice also that we're
        # starting at the second letter -- we'll cover why in a
        # second.
        for i in range(1, len(my_string)):

            # Here's the unfamiliar syntax: the brackets let us
            # access the character at index i in the string. So,
            # if my_string is "Hi David!", my_string[0] will be
            # "H", my_string[1] will be "i", and so on.
            if my_string[i] == " ":

                # If we've reached here, we know the current
                # character is a space. Now we need to make sure
                # the letter before it wasn't a space. This line
                # checks the previous character, at index i - 1.
                # That's why we started the loop at 1, to avoid
                # checking the -1 character.

                if not my_string[i - 1] == " ":
                    # If we've reached here, it means that the
                    # current character is a space, and the
                    # previous character was not a space. So, we
                    # can go ahead and count:

                    word_count += 1

        # And now we're done, and can return our word count:
        return word_count

    except:
        return "Not a string"


print("Word Count:", word_count("Four words are here!"))
print("Word Count:", word_count("Hi   David"))
print("Word Count:", word_count(5))
print("Word Count:", word_count(5.1))
print("Word Count:", word_count(True))
print()
print()


# Coding problem 3.5.7


# This will be the largest, most authentic program you've
# written so far. It will require everything you've learned
# and should take some time to test and debug. Be patient,
# you can do it!
#
# Write a function called average_word_length that takes as
# input a string called my_string, and returns as output the
# average length of the words in the string.
#
# In writing this function, note the following:
#
# - You should account for consecutive spaces. A string like
#   "Hi   Lucy" is two words with an average length of 3.0
#   characters.
# - You should not assume the string starts with a letter.
#   A string like "  David" has one word with an average
#   length of 5.0 characters.
# - You should not count punctuation marks toward the
#   length of a word. A string like "Hi, Lucy" has two
#   words with an average length of 3.0 characters: the ,
#   after "Hi" does not count as a character in the word.
#   The only punctuation marks you need to handle are
#   these: . , ! ?
# - You may assume the only characters in the string are
#   letters, the punctuation marks listed above, and spaces.
# - If my_string is not a string, you should instead return
#   the string, "Not a string".
# - If there are no words in my_string, you should instead
#   return the string, "No words". This could happen for
#   strings like "" (an empty string) and ".,!?" (a string
#   of only punctuation marks). You may assume that any
#   of these punctuation marks will always be followed by
#   at least one space.
#
# Here are a few hints that might help you:
#
# - You can peak at the first character in my_string with
#   my_string[0]. If my_string is "Hi, Lucy", then the value
#   of my_string[0] is "H". You don't have to do this, but
#   you can if you want.
# - There are lots of ways you can do this. If you're
#   stuck, try taking a step back and thinking about the
#   problem from a fresh perspective.
# - If you're still stuck, try counting words and letters
#   separately, and worrying about average length only
#   after both have been counted.
# - The word count should equal the number of letters that
#   come immediately after a space or the start of the
#   string. The character count should simply equal the
#   number of characters besides spaces and punctuation
#   marks. The average word length should be character
#   count divided by word count.


# Write your function here:


def average_word_length(my_string):
    pos = -1
    letter_count = 0
    punct_1 = ['.', ',', '!', ' ""', '?', '" "']
    try:
        word_count = len(my_string.split())

        for letter in my_string:
            if letter in punct_1 and my_string[pos - 2] in punct_1:
                return "No words"

            if letter in "abcdefghijklmnopqrstuvwxyz" or letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter_count += 1

            # print(letter, letter_count)
        return letter_count / word_count
    except:
        return "Not a string"


# output:
# 2.0
# 3.0
# 4.0
# Not a string
# No words

print(average_word_length("Hi"))
print(average_word_length("Hi, Lucy"))
print(average_word_length("   What   big spaces  you    have!"))
print(average_word_length(True))
print(average_word_length("?!?!?! ... !"))

## took me ages to arrive at the above code, well had to check a few codes to arrive at the solution
# There are many more ways to solve the problem, wil keep working on it...

print()

# -----------------------------------------------------------
# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# In this problem, we're going to use some unfamiliar syntax.
# You'll learn more about this syntax in Unit 4. For now,
# though, you don't need to understand the syntax. All you
# need to know is that right now, this code will cause an
# error with the values supplied above.
#
# Revise this code so that this error is caught, and the
# message "Invalid index!!" is printed. However, your revision
# must meet these requirements, too:
#
# - If the values of the variables above are changed so
#   that the error doesn't occur, the program should behave
#   the same way that it does now.
# - The two first and last lines, "Accessing index..." and
#   "Done!", should print whether or not an error occurs.
# - If a *different* error occurs from the one that arises
#   initially, your code should instead print "Unknown
#   error!"
#
# HINT: You won't be able to do this without running the code
# first and seeing what the error is. So, try it out first!

# Revise this code:


a_list = [1, 2, 3, 4, 5]
list_index = 7

try:
    print("Accessing index...")
    result = a_list[list_index]
    print("Value at index:", result)
except IndexError:
    print("Invalid index!!")
except:
    print("Unknown error!")
print("Done!")

print()
# Counting letters:
mystery_string = "Hello! What a fine day it is today."
mystery_character = "a"

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Write some code below that will count and print how many
# times mystery_character appears in mystery_string. You may
# not use the string class's .count method.
#
# With the original values for mystery_string and
# mystery_character, your code should initially print 4. Only
# count characters with the same case as mystery_character
# (in other words, here you would ignore capital A).


# Add your code here!

count = 0
mystery_character = mystery_character.lower()
for letter in mystery_string:
    if letter == mystery_character:
        count += 1
print(count)
