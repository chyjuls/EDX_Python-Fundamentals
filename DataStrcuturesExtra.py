# Write a function called count_characters. count_characters
# should take as input a single string, and return a
# dictionary. In the dictionary, the keys should be
# characters, and the values should be the number of times
# each character appeared in the string.
#
# For example:
#
#  count_characters("aabbccc") -> {'a': 2, 'b': 2, 'c': 3}
#  count_characters("AaBbbb") -> {'A': 1, 'B': 1, 'a': 1, 'b': 3}
#
# You should not need to make any assumptions about the
# characters in the string: spaces, punctuation, line breaks,
# and any other characters should be handled automatically.
# You may count upper and lower case separately.


# Write your function here!
from itertools import product


def count_characters(str):
    dict_char = {}
    for i in str:
        if i in dict_char:
            dict_char[i] += 1
        else:
            dict_char[i] = 1
    return dict_char


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (although the order of the keys may vary):
#
# {'a': 2, 'b': 2, 'c': 3}
print(count_characters("aabbccc"))
print()


# Write a function called find_range. find_range should take
# as input a string representing a filename. The file
# corresponding to that filename will be a list of integers,
# one integer per line. find_range should return a tuple
# containing the smallest and largest numbers in the file
# (the smallest first, then the largest).
#
# For example, in the dropdown in the top left you'll find a
# file named FindRangeInput.txt. The smallest number in that
# file is 2, and the largest is 37. So, if you called
# find_range("FindRangeInput.txt"), the function would return
# (2, 37), a tuple with two integers.
#
# You may assume that all lines in the file will contain a
# positive integer (greater than 0). There may be duplicates.
#
# Hint: Remember, if you loop through all the lines in a file
# then you have to close and reopen the file to read it again,
# or by use file.seek(0) to start from the top. However, you
# can do this problem without having to read the file twice.


# Write your function here!

def find_range(find_range):
    min_value = 0
    max_val = 0
    range_tuple = ()
    integers = open(find_range, "r")
    numbers = {int(line) for line in integers}
    max_val = max(numbers)
    min_val = min(numbers)
    range_tuple = min_val, max_val
    return range_tuple
    integers.close()


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: (2, 37)
print(find_range("FindRangeInput.txt"))
print()


# Write a function called pivot_library. pivot_library takes
# as input one parameter, a list of 3-tuples. Each tuple in
# the list has three items: the first item is a book title
# (a string), the second item is the book's author (a
# string), and the third item is the book's ISBN number (a
# string).
#
# pivot_library should return a dictionary. In the dictionary
# that it returns, the keys should be the ISBN numbers, and
# the values should be 2-item tuples. In each tuple, the first
# item should be the book title, and the second item should
# be the author's name.
#
# Hint: Unpack the tuple to variables first, then create the
# new dictionary item.
#
# For example:
#
# books = [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"),
#          ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
# pivot_library(books)
#   -> {"978-0-140-17739-8": ("Of Mice and Men", "John Steinbeck"),
#       "978-1-260-08227-2": ("Introduction to Computing", "David Joyner")}


# Write your function here!

def pivot_library(books):
    book_dict = {}
    new_tuple = ()
    for book in books:
        (book_title, author, isbn_no) = book
        book_dict[isbn_no] = book_title, author
    return book_dict


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (although the order of the keys may vary):
#
# {"978-0-140-17739-8": ("Of Mice and Men", "John Steinbeck"), "978-1-260-08227-2": ("Introduction to Computing", "David Joyner")}
books = [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"),
         ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
print(pivot_library(books))
print()


# Write a function called write_book_info. write_book_info
# will take as input two parameters: a string and a list of
# 3-tuples.
#
# The string will represent the filename to which to write.
#
# Each 3-tuple in the list will contain three strings: a
# book title, the book's author, and the book's ISBN number.
#
# write_book_info should write the list of books to the file
# given by the filename using the following format:
#
# ISBN: Title by Author
#
# So, for this list:
#
# [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"),
#  ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
#
# The file printed would look like this:
#
# 978-0-140-17739-8: Of Mice and Men by John Steinbeck
# 978-1-260-08227-2: Introduction to Computing by David Joyner
#
# We've included Sample.txt to show you what a longer version
# of one of these files might look like.

# Write your function here!
def write_book_info(book_file, books):
    my_file = open(book_file, "w")
    for book in books:
        (title, author, isbn_no) = book
        book_string = isbn_no + ": " + title + " by " + author

        my_file.writelines(str(book_string) + "\n")
    my_file.close()


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print nothing -- however, it should write the same contents
# as Sample.txt to Test.txt.
books = [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"),
         ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
write_book_info("Test.txt", books)
print()


# APA citation style cites author names like this:
#
#  Last, F., Joyner, D., Burdell, G.
#
# Note the following:
#
# - Each individual name is listed as the last name, then a
#   comma, then the first initial, then a period.
# - The names are separated by commas, including the last
#   two.
# - There is no space or comma following the last period.
#
# Write a function called names_to_apa. names_to_apa should
# take as input one string, and return a reformatted string
# according to the style given above. You can assume that
# the input string will be of the following format:
#
#  First Last, David Joyner, and George Burdell
#
# You may assume the following:
#
# - There will be at least three names, with "and" before
#   the last name.
# - Each name will have exactly two words.
# - There will be commas between each pair of names.
# - The word 'and' will precede the last name.
# - The names will only be letters (no punctuation, special
#   characters, etc.), and first and last name will both be
#   capitalized.
#
# Hint: You can use the string replace() method to delete
# text from a string. For example, a_string.replace("hi", "")
# will delete all instances of "hi". There are multiple ways
# you might choose to use this.


# Write your function below!
def names_to_apa(names):
    names = names.replace(', and ', ', ')
    names = names.split(', ')
    names = [name.split() for name in names]
    names = [name[-1] + ', ' + (''.join(initial[0] + '.' for initial in name[:-1])) for name in names]
    names = ', '.join(names[:-1]) + ', ' + "& " + names[-1]
    return names


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: Last, F., Joyner, D., & Burdell, G.
print(names_to_apa("First Last, David Joyner, and Sophia Wilson"))
print()


# Write a function called check_formula. The check_formula
# function should take as input one parameter, a string. It
# should return True if the string holds a correctly
# formatted arithmetic integer formula according to the rules
# below, or False if it does not.
#
# For this problem, here are the rules that define a
# correctly-formatted arithmetic string:
#
# - The only characters in the string should be digits or
#   the five arithmetic operators: +, -, *, /, and =. Any
#   other characters, including spaces, periods, commas,
#   or any letters, are not permitted.
# - There may not be any consecutive arithmetic operators.
#   Any arithmetic operator must have a number on either
#   side of it.
# - There must be an equals sign in the formula.
#
# You do not need to worry about negative numbers or
# parentheses, and you do not need to worry about whether
# the equation is accurate. You may also assume all the
# numbers in the string will be only one digit.
#
# Here are some examples of valid and invalid arithmetic
# formulas:
#
#   Valid     Invalid
#   5*3=5+2   5*3+5+2 (no equals)
#   5=7       5= (equals sign isn't in the middle)
#   5=2-5     50=-5 (consecutive arithmetic operators)
#   6/2=5/2   a=51 (illegal character)
#             -5=5+2 (starts with an operator)
#
# Hint: Remember, as soon as you find *one* thing wrong
# with the string, you know it's invalid and can return
# False. So, go character-by-character through the string
# checking everything that could be wrong. If you don't
# find anything wrong, return True!


# Write your function here!
def check_formula(expression):
    """returns True if expression holds a correctly formatted formula"""
    operators = ['+', '-', '*', '/', '=']  # allowed operators
    found_equals = False
    found_operator = False
    for i in range(len(expression)):
        character = expression[i]  # look at each character
        # checks if character is an allowed operator
        if character in operators:
            if found_operator:  # checks if found_operator flag is already True
                return False  # character is a consecutive operator
            if i == 0 or i == len(expression) - 1:  # checks if operator is at the beginning or end
                return False
            # checks if there is a digit on either side of the operator
            if not expression[i - 1].isdigit() or not expression[i + 1].isdigit():
                return False
            found_operator = True  # sets found operator flag as True
            if character == '=':  # operator is an equals symbol
                found_equals = True
        # checks if character is a digit
        elif character.isdigit():
            found_operator = False
        # returns False if the character is neither an allowed operator nor a digit
        else:
            return False
    # returns False if an = symbol was not found in the expression
    if not found_equals:
        return False
    # all rules correct, so returns True
    return True


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print True, then several Falses.
print(check_formula("5*3=5+2"))
print(check_formula("5*3+5+2"))
print(check_formula("5="))
print(check_formula("5=-5"))
print(check_formula("a=5"))
print(check_formula("-5=5+2"))
print()
print()


# In the game tic-tac-toe, two players take turns drawing
# Xs and Os on a 3x3 grid. If one player can place three of
# their symbols side-by-side in a row, column, or diagonal,
# they win the game.
#
# For example:
#
# X Wins:   X Wins:   X Wins:   No Winner:
# X|O|X     O|X|X     O|O|      X|O|O
# -+-+-     -+-+-     -+-+-     -+-+-
# O|O|X     X|O|      X|X|X     O|X|X
# -+-+-     -+-+-     -+-+-     -----
# O|X|X      | |O      | |      X|X|O
#
# Write a function called check_winner. check_winner will
# take one parameter as input, a 2D tuple (that is, a tuple
# of tuples). The 2D tuple represents the game board: each
# smaller tuple in the larger tuple is a row of the board,
# and each item in the smaller tuple is a spot on the
# board. There will always be three tuples in the larger
# tuple, and three items in each of the smaller tuples.
#
# Each item in the smaller tuple will always be one of three
# values: the string "X", the string "O", or the value None.
#
# check_winner should return one of three values: the string
# "X" if X has won the game; the string "O" if O has won the
# game; or the value None if there is no winner. None should
# NOT be the string "None"; it should be the value None,
# like the boolean values True and False.
#
# You may assume a player has won the game if and only if
# the board has three of their symbols in a row: you do not
# need to worry about whether the input is a valid game
# otherwise (e.g. a board of nine Xs still counts as X
# winning). You may assume that there will only be one
# winner per board.
#
# Hint: There are only eight possible places to win (three
# rows, three columns, two diagonals).
#
# Hint 2: If you're comfortable on time, you may want to
# check out the last problem before doing this one. It's
# only worth 1 point, but you might be able to design
# one solution that works for both problems!


# Write your function here!

def check_winner(tuples):
    for i in range(len(tuples)):
        if tuples[0][0] == tuples[0][1] == tuples[0][2]:
            return tuples[0][0]
        elif tuples[1][0] == tuples[1][1] == tuples[1][2]:
            return tuples[1][0]
        elif tuples[2][0] == tuples[2][1] == tuples[2][2]:
            return tuples[2][0]
        elif tuples[0][2] == tuples[1][2] == tuples[2][2]:
            return tuples[0][2]
        elif tuples[0][1] == tuples[1][1] == tuples[2][1]:
            return tuples[0][1]
        elif tuples[0][0] == tuples[1][0] == tuples[2][0]:
            return tuples[0][0]
        elif tuples[0][0] == tuples[1][1] == tuples[2][2]:
            return tuples[0][0]
        elif tuples[0][2] == tuples[1][1] == tuples[2][0]:
            return tuples[0][2]


# The code below shows how the tic-tac-toe tuples are
# created and tests your code with three games: one where
# X wins, one where O wins, and one where there is no winner.
# Remember, the line breaks in xwins and owins are optional:
# they're just to make the declarations more readable. They
# could be written the same as nowins.
xwins = (("X", "O", "X"),
         ("O", "O", "X"),
         ("O", "X", "X"))
owins = (("O", "X", "X"),
         ("X", "O", None),
         (None, None, "O"))
nowins = (("X", "O", "O"), ("O", "X", "X"), ("X", "X", "O"))
print(check_winner(xwins))
print(check_winner(owins))
print(check_winner(nowins))
print()


# Write a function called average_rainfall. average_rainfall
# should have one parameter, a list of integers. The list
# represents daily rainfall measurements for a certain area.
#
# However, at some point in the list, there will be a -1.
# This indicates that you should stop averaging, and ignore
# any subsequent values.
#
# For example:
#
# average_rainfall([1, 2, 3, 4, 5, -1, 6, 7]) -> 3.0
#
# The function would only average 1, 2, 3, 4, and 5, and
# ignore any values after the -1.
#
# You may assume all the items in the list are integers,
# that -1 is guaranteed to occur somewhere in the list,
# and that -1 will not be the first item in the list.


# Add your code here!
def average_rainfall(a_list):
    total = 0
    avg = 0
    new_list = []
    for num in a_list:
        if num >= 0:
            new_list.append(num)
        else:
            num < 0
            break

    avg = sum(new_list) / len(new_list)
    return avg


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 3.0
a_list = [1, 2, 3, 4, 5, -1, 6, 7]
print(average_rainfall(a_list))
print()


# Write a function called volume_and_area. volume_and_area
# will take in a dictionary. This dictionary is guaranteed to
# have three keys: "length", "width", and "height", whose
# values are integers representing three attributes of a
# rectangular prism (also known as a box).
#
# Modify this dictionary to add two keys: "volume" and "area".
# The values associated with these keys should be the volume
# and surface area of the box.
#
# The formula for volume is:
#  length * width * height
#
# The formula for surface area is:
#  2 * ((length * width) + (length*height) + (width*height))
#
# Because length, width, and height are integers, and because
# these formulas have no division, your results should be
# integers as well.

# Add your code here!
def volume_and_area(rectangle):
    new_dict = {}
    val_prod = 1
    surface_area = 1
    for key, value in rectangle.items():
        val_prod *= value
        surface_area = 2 * ((rectangle["length"] * rectangle["width"]) + (
                rectangle["length"] * rectangle["height"]) + (
                                    rectangle["width"] * rectangle["height"]))
    rectangle["volume"] = val_prod
    rectangle["area"] = surface_area
    return rectangle


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print 6 and 22, each on a different line.
rectangle = {"length": 1, "width": 2, "height": 3}
rectangle = volume_and_area(rectangle)
print(rectangle["volume"])
print(rectangle["area"])
print()

# Write a function called imdb_dictionary. imdb_dictionary
# should have one parameter, a string representing a
# filename.
#
# On each row of the file will be a performer's name, then
# a semicolon, then a comma-separated list of movies the have
# been in. For example, one file's contents could be:
#
# Robert Downey Jr.; Avengers: Infinity War, Sherlock Holmes 3, Spider-Man: Homecoming
# Scarlett Johansson; Avengers: Infinity War, Isle of Dogs, Ghost in the Shell
# Elizabeth Olsen; Avengers: Infinity War, Kodachrome, Wind River, Ingrid Goes West
#
# You may assume that the only semi-colon will be after the
# performer's name, and that there will be no commas in the
# movie titles.
#
# Return a dictionary where the keys are each actor's name,
# and the values are alphabetically-sorted lists of the movies
# they have been in. For example, if imdb_dictionary was called
# on the file above, the output would be:
# {"Robert Downey Jr.": ["Avengers: Infinity War", "Sherlock Holmes 3", "Spider-Man: Homecoming"],
# "Scarlett Johansson": ["Avengers: Infinity War", "Ghost in the Shell", "Isle of Dogs"],
# Elizabeth Olsen": ["Avengers: Infinity War", "Ingrid Goes West", "Kodachrome", "Wind River"]}
#
# Make sure the list of movies is sorted alphabetically. Don't
# worry about the order the keys (names) appear in the dictionary.

### write file here:
with open("some_performers.txt", "w") as imbd_file:
    imbd_file.write('''Robert Downey Jr.; Avengers: Infinity War, Sherlock Holmes 3, Spider-Man: Homecoming
Scarlett Johansson; Avengers: Infinity War, Isle of Dogs, Ghost in the Shell
Elizabeth Olsen; Avengers: Infinity War, Kodachrome, Wind River, Ingrid Goes West''')


# Add your code here!
# spent a whole trying to crack, pulled my hair out copied codes, after hours of debugging
# came up with my own code...You can not sort this after creating a dictionary, it must be sorted before, with
# the right spaces, commas, and semicolons,if not you will never get the right output....pheeew!!!
def imdb_dictionary(filename):
    lines = open(filename, "r")
    movie_dict = {}
    for line in lines:
        line = line.strip()
        line = line.split("; ")
        name, movie_title = line
        movie_title = movie_title.split(", ")  # This split makes a difference when sorting, ....
        movie_title.sort()
        # new_movie_title = ", ".join(movie_title) # reduntant code not needed
        # movie_dict[name] = [] redundant not needed
        movie_dict[name] = movie_title
    lines.close()
    return movie_dict


# below are some lines of code that will test your function.
# You can change the contents of some_performers.txt from
# the dropdown in the top left to test other inputs.
#
# If your function works correctly, this will originally print (although the order of the keys may vary): {"Robert
# Downey Jr.": ["Avengers: Infinity War", "Sherlock Holmes 3", "Spider-Man: Homecoming"], "Scarlett Johansson": [
# "Avengers: Infinity War", "Ghost in the Shell", "Isle of Dogs"], Elizabeth Olsen": ["Avengers: Infinity War",
# "Ingrid Goes West", "Kodachrome", "Wind River"]}
print(imdb_dictionary("some_performers.txt"))
print()


# Write a function called digit_count. digit_count should
# take as input a number, which could be either a float or an
# integer. It should return a dictionary whose keys are digits,
# and whose values are the number of times that digit appears
# in the number.
#
# The dictionary should NOT contain any numerals that do not
# occur at all in the number, and it should also note contain
# the decimal point character if the number is a decimal.
#
# For example:
#
#  digit_count(11223) -> {1: 2, 2: 2, 3: 1}
#  digit_count(3.14159) -> {3: 1, 1: 2, 4: 1, 5: 1, 9: 1}
#
# Hint: You should probably convert the number to a string to
# count the digits, but convert the individual digits back to
# integers to use as keys to the dictionary.

# Write your function here!
# steps:
# Create function.
# convert num to strings
# replace decimal point with ""
# replace "" with " " to create spaces between numbers
# split strings further for char in word ...
# remove first and last blanks using index slicing
# remove empty blanks using list comprehension strip
# get the items in the cleaned list, convert item to int
# assign dict key...to frequency of numbers  using if else/statement
# return new dict


def digit_count(num):
    num_dict = {}
    num_list = []
    num = str(num)
    num = num.replace(".", "")
    num = num.replace("", " ")
    num_list = [char for char in num]
    num_list = num_list[1::]
    num_list = num_list[:-1:]
    new_list = [ele for ele in num_list if ele.strip()]
    for item in new_list:
        item = int(item)
        if item in num_dict:
            num_dict[item] += 1
        else:
            num_dict[item] = 1
    return num_dict


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (although the order of the keys may vary):
#
# {1: 2, 2: 2, 3: 1}
# {3: 1, 1: 2, 4: 1, 5: 1, 9: 1}
print(digit_count(11223))
print(digit_count(3.14159))
print()


# Write a function called pivot_library. pivot_library takes
# as input one parameter, a list of 3-tuples. Each tuple in
# the list has three items: the first item is a book title
# (a string), the second item is the book's author (a
# string), and the third item is the book's ISBN number (a
# string).
#
# pivot_library should return a dictionary. In the dictionary
# that it returns, the keys should be the ISBN numbers, and
# the values should be 2-item tuples. In each tuple, the first
# item should be the book title, and the second item should
# be the author's name.
#
# Hint: Unpack the tuple to variables first, then create the
# new dictionary item.
#
# For example:
#
# books = [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"),
#          ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
# pivot_library(books)
#   -> {"978-0-140-17739-8": ("Of Mice and Men", "John Steinbeck"),
#       "978-1-260-08227-2": ("Introduction to Computing", "David Joyner")}


# Write your function here!

def pivot_library(books):
    book_dict = {}
    for book in books:
        (book_title, author, isbn_no) = book
        book_dict[isbn_no] = book_title, author
    return (book_dict)


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (although the order of the keys may vary):
#
# {"978-0-140-17739-8": ("Of Mice and Men", "John Steinbeck"), "978-1-260-08227-2": ("Introduction to Computing",
# "David Joyner")}
books = [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"),
         ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
print(pivot_library(books))
print()


# Write a function called write_class_data. write_class_data
# will take as input two parameters: a string and a list of
# 3-tuples.
#
# The string will represent the filename to which to write.
#
# Each 3-tuple in the list will contain three values:
#
# - A string representing the major of a college class (e.g.
#   "CS", "CHEM", "ENGL")
# - An integer representing a course number (e.g. 1301, 2241,
#   4001)
# - A string representing the name of a course (e.g.
#   "Introduction to Computing", "Organic Chemistry", etc.)
#
# write_class_data should write the list of classes to the file
# given by the filename using the following format:
#
# [major][number]: [class name]
#
# So, for this list:
#
# [("CS", 1301, "Introduction to Computing"),
#  ("CHEM", "1310", "General Chemistry")]
#
# The file printed would look like this:
#
# CS1301: Introduction to Computing
# CHEM1310: General Chemistry
#
# Note the specifics of that format: no space between the major
# and course number, no space between the course number and the
# colon, one space between the colon and the course name.
#
# We've included Sample.txt to show you what a longer version
# of one of these files might look like.

# Write your function here!
def write_class_data(filename, tuple_list):
    with open(filename, "w") as string_file:
        for item in tuple_list:
            course_code, course_no, course_title = item
            new_course = course_code + str(course_no) + ":" + " " + course_title
            string_file.write(new_course + "\n")


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print nothing -- however, it should write the same contents
# as Sample.txt to Test.txt.
classes = [("CS", 1301, "Introduction to Computing"), ("CHEM", "1310", "General Chemistry")]
write_class_data("Test.txt", classes)

with open("FirstLastInput.txt", "w") as  first_file:
    first_file.write('''8
rjbvm
6
16
26
10
rcubr
18
10
27
lrgfd
13
ldfsw
fsszd
22
6
35
32
36
fseog
37
2
14
14
appsp
dafdo
16
fdsww
zzffs''')
print()


# Write a function called first_to_last. first_to_last should
# take as input a string representing a filename. Inside the
# file will be some text on each line; some lines will contain
# integers, while others will contain strings of other
# characters.
#
# first_to_last should return a tuple containing the first and
# last strings in the file alphabetically. It should ignore any
# lines that contain integers.
#
# For example, in the dropdown in the top left you'll find a
# file named FirstLastInput.txt. Ignoring numerals, the first
# string alphabetically is appsp, and the last string
# alphabetically is zzffs. So, first_to_last("FirstLastInput.txt")
# would return the tuple ("appsp", "zzffs").
#
# You may assume that every line in the file contains either
# all numerals or all lower-case letters; there will be no lines
# with both numerals and letters, nor any capital letters.


# Write your function here!
def first_to_last(filename):
    with open(filename, "r") as first_file:
        line = first_file.read()  # read file use .read
        line_list = []  # create empty lists
        newline_list = []
        line = line.strip("\n")  # strip the trailing new line
        line = line.split()  # convert to a list
        line.sort()  # sort list
        result = [i for i in line if not i.isdigit()]  # extract the letters
        new_tuple_list = (result[0], result[-1])

        return (new_tuple_list)


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: ("appsp", "zzffs")
print(first_to_last("FirstLastInput.txt"))
print()


# Write a function called complete_profile. complete_profile
# will take as input a dictionary. This dictionary will have
# four keys: first, middle, last, and title. The function
# should return a dictionary with those four keys, and three
# more: name, full_name, short_name. The values for those
# keys should be:
#
# - name: the first and last name, separated by a space
# - full_name: the title, first, middle, and last names,
#   with a space between each pair of strings
# - short_name: the first letter of the first name, a space,
#   and their last name
#
# For example:
#
# complete_profile({"first": "David", "middle": "Andrew",
#                   "last": "Joyner", "title": "Dr."})
#
# would return:
#
# {"first": "David", "middle": "Andrew", "last": "Joyner",
#  "title": "Dr.", "name": "David Joyner",
#  "full_name": "Dr. David Andrew Joyner",
#  "short_name": "D Joyner"}
#
# You may either modify the dictionary that is passed in,
# or create a new one. Either way, make sure to return the
# dictionary at the end of the function.


# Add your code here!

def complete_profile(new_prof):
    dict_profile = {}
    dict_profile["name"] = new_prof["first"] + " " + new_prof["last"]
    dict_profile["full_name"] = new_prof["title"] + " " + new_prof["first"] + " " + new_prof["middle"] + " " + new_prof[
        "last"]
    get_letter = new_prof["first"][0]
    dict_profile["short_name"] = get_letter + " " + new_prof["last"]
    new_prof.update(dict_profile)
    return new_prof


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print "David Joyner", "Dr. David Andrew Joyner", and D Joyner" each on a different line (without the quotes).

prof = {"first": "David", "middle": "Andrew", "last": "Joyner", "title": "Dr."}
prof = complete_profile(prof)
print(prof["name"])
print(prof["full_name"])
print(prof["short_name"])
print()


# Write a function called pivot_library. pivot_library takes
# as input one parameter, a list of 3-tuples. Each tuple in
# the list has three items: the first item is a book title
# (a string), the second item is the book's author (a
# string), and the third item is the book's ISBN number (a
# string).
#
# pivot_library should return a dictionary. In the dictionary
# that it returns, the keys should be the ISBN numbers, and
# the values should be new dictionaries. Each new dictionary
# should have two keys: "title" and "author". Their values
# should correspond to the first and second items from the
# original 3-tuple.
#
# For example:
#
# books = [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"),
#          ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
# pivot_library(books)
#   -> {"978-0-140-17739-8": {"title": "Of Mice and Men", "author": "John Steinbeck"},
#       "978-1-260-08227-2": {"title": "Introduction to Computing", "author": "David Joyner"}}


# Write your function here!
def pivot_library(new_books):
    newbook_dict = {}

    for books in new_books:
        (title, author, ISBN) = books
        new_dict = {}  # define within loop....
        new_dict["title"] = title
        new_dict["author"] = author
        newbook_dict[ISBN] = new_dict
    return newbook_dict


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (although the order of the keys may vary):
#
# {"978-0-140-17739-8": {"title": "Of Mice and Men", "author": "John Steinbeck"}, "978-1-260-08227-2": {"title":
# "Introduction to Computing", "author": "David Joyner"}}
books = [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"),
         ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
print(pivot_library(books))
print()


# It's a well-known and indisputable fact that if you want
# to make your name sound fancy, you should list it as only
# your first two initials followed by your last name. For
# example, my full name is David Andrew Joyner, and therefore
# my fancy name is D. A. Joyner. (If you have two middle names,
# it's even better, but we'll assume we have only one -- we're
# C. S. Lewis, not J. R. R. Tolkien).
#
# Write a function called fancy_me. fancy_me should take as
# input a list of strings, each representing a full name (e.g.
# "David Andrew Joyner" or "First Middle Last". fancy_me should
# return a single string, formatting that list of names in this
# fancy style, like this:
#
#  F. M. Last, D. A. Joyner, G. P. Burdell
#
# Each individual name is the first initial, then a period, then
# a space, then the second initial, then a period, then a space,
# then the last name, then a comma. There is no comma after the
# last name in the list.
#
# For example:
#
#  fancy_me(["First Middle Last", "David Andrew Joyner", "George P Burdell"])
#
# ...would return "F. M. Last, D. A. Joyner, G. P. Burdell"


# Write your function below!

def initialize(name):
    first, middle, last = name.split()  # note this assumes all names will only be three parts

    return f"{first[0]}. {middle[0]}. {last}"


def fancy_me(namelist):
    return ", ".join(initialize(name) for name in namelist)


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: F. M. Last, D. A. Joyner, G. P. Burdell
print(fancy_me(["First Middle Last", "David Andrew Joyner", "George P Burdell"]))


# Another method if number of names not equals to three:
def initialize(name) -> str:
    parts = name.split()
    return ". ".join(part[0] for part in parts) + parts[-1][1:]


def fancy_me(namelist) -> str:
    return ", ".join(initialize(name) for name in namelist)


print(fancy_me(["First Middle Last", "David Andrew Joyner", "George P Burdell"]))
print()

# In the game Rock-Paper-Scissors, two opponents
# simultaneously choose to throw either "Rock", "Paper",
# or "Scissors". Rock beats Scissors, Scissors beats Paper,
# and Paper beats Rock. If both players throw the same
# object, the round is a tie.
#
# Write a function called find_winner. find_winner will take
# as input a list of 2-tuples, each representing a round of
# Rock-Paper-Scissors. Each 2-tuple will contain two strings.
# Each string will be either "Rock", "Paper", or "Scissors".
# The first item in the 2-tuple will represent what Player 1
# chooses in each round, and the second item in the 2-tuple
# will represent what Player 2 chooses in each round.
#
# find_winner should return the string "Player 1 wins!" if
# Player 1 wins more games than Player 2. It should return the
# string "Player 2 wins!" if Player 2 wins more games than
# Player 1. It should return the string "It's a tie!" if the
# two players win an equal number of times.
#
# The number of times the two players tie is irrelevant to the
# result: all that matters is who wins more rounds than the
# other.
#
# For example:
#
# find_winner([("Rock", "Rock"), ("Rock", "Scissors"),
#              ("Paper", "Rock"), ("Scissors", "Rock")])
#
# ...would return "Player 1 wins!" because Player 1 wins
# two round and Player 2 wins one round.


# Write your function here!
# def find_winner(tuple_list):


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
# If your function works correctly, this will originally
# print:
# Player 1 wins!
# Player 2 wins!
# It's a tie!
p1_wins = [("Rock", "Rock"), ("Rock", "Scissors"), ("Paper", "Rock"), ("Scissors", "Rock")]
p2_wins = [("Paper", "Rock"), ("Paper", "Paper"), ("Paper", "Scissors"), ("Rock", "Paper")]
itsatie = [("Paper", "Paper"), ("Paper", "Rock"), ("Rock", "Paper"), ("Scissors", "Scissors")]


# print(find_winner(p1_wins))
# print(find_winner(p2_wins))
# print(find_winner(itsatie))
# print()

# Write a function called imdb_dictionary. imdb_dictionary
# should have one parameter, a string representing a
# filename.
#
# On each row of the file will be a comma-and-space-separated
# list of movies, then a colon, then a performer's name. For
# example, one file's contents could be:
#
# Avengers: Infinity War, Sherlock Holmes 3, Spider-Man: Homecoming; Robert Downey Jr.
# Avengers: Infinity War, Isle of Dogs, Ghost in the Shell; Scarlett Johansson
# Avengers: Infinity War, Kodachrome, Wind River, Ingrid Goes West; Elizabeth Olsen
#
# You may assume that the only semi-colon will be before the
# performer's name, and that there will be no commas in the
# movie titles.
#
# Return a dictionary where the keys are each actor's name,
# and the values are alphabetically-sorted lists of the movies
# they have been in. For example, if imdb_dictionary was called
# on the file above, the output would be:
# {"Robert Downey Jr.": ["Avengers: Infinity War", "Sherlock Holmes 3", "Spider-Man: Homecoming"],
# "Scarlett Johansson": ["Avengers: Infinity War", "Ghost in the Shell", "Isle of Dogs"],
# Elizabeth Olsen": ["Avengers: Infinity War", "Ingrid Goes West", "Kodachrome", "Wind River"]}
#
# Make sure the list of movies is sorted alphabetically. Don't
# worry about the order the keys (names) appear in the dictionary.
#
# Hint: Remember to deal with the spaces after the commas and
# semicolons!


# Add your code here!
def imdb_dictionary(filename):
    lines = open(filename, "r")
    movie_dict = {}
    for line in lines:
        line = line.strip()
        line = line.split("; ")
        name, movie_title = line
        movie_title = movie_title.split(", ")  # This split makes a difference when sorting, ....
        movie_title.sort()
        new_movie_title = ", ".join(movie_title)
        movie_dict[name] = []
        movie_dict[name] = movie_title
    lines.close()
    return movie_dict


# Below are some lines of code that will test your function.
# You can change the contents of some_performers.txt from
# the dropdown in the top left to test other inputs.
#
# If your function works correctly, this will originally print (although the order of the keys may vary): {"Robert
# Downey Jr.": ["Avengers: Infinity War", "Sherlock Holmes 3", "Spider-Man: Homecoming"], "Scarlett Johansson": [
# "Avengers: Infinity War", "Ghost in the Shell", "Isle of Dogs"], Elizabeth Olsen": ["Avengers: Infinity War",
# "Ingrid Goes West", "Kodachrome", "Wind River"]}
print(imdb_dictionary("some_performers.txt"))
print()
print()


# Imagine you are trying to choose what restaurant to visit.
# You have a list of restaurants, each with a collection of
# star ratings. You also have a minimum standard; you will
# only go to a restaurant whose star rating is at least your
# minimum standard.
#
# Write a function called restaurant_rating. restaurant_rating
# has two parameters. The first is a dictionary, where the keys
# are restaurant names and the values are lists of ratings. The
# second parameter is your minimum rating. If a restaurant's
# average rating is above your minimum rating, you might visit
# it. If it is not, you won't.
#
# restaurant_rating should return a list of restaurants eligible
# for you to visit. That is, it should return a list of
# restaurant names from the dictionary whose average ratings
# (the average of the ratings in their lists) is greater than or
# equal to your minimum rating.
#
# For example:
# rest_and_rating = {'burger king':[4,5,3,4,3], 'moes':[4,5,5,5,5], 'taco bell':[1,2,3,4,5]}
# value = 4.5
# restaurant_rating(rest_and_rating, value) -> ['moes']


# Write your code here!
def restaurant_rating(rest_dict, value):
    rest_list = []
    for k, v in rest_dict.items():
        average = (sum(v) / len(v))
        if average >= value:
            rest_list.append(k)
            rest_list.sort()

    return rest_list


print()
print()

# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: ['moes']
rest_and_rating = {'burger king': [4, 5, 3, 4, 3], 'moes': [4, 5, 5, 5, 5], 'taco bell': [1, 2, 3, 4, 5]}
value = 4.5
print(restaurant_rating(rest_and_rating, value))
print()


# -----------------------------------------------------------
# Write a function called no_you_pick. no_you_pick should
# have two parameters. The first parameter is a dictionary
# where the keys are restaurant names and the values are lists
# of attributes of those restaurants as strings, such as
# "vegetarian", "vegan", and "gluten-free".
#
# The second parameter is a list of strings representing of
# necessary attributes of the restaurant you select.
#
# Return a list of restaurants from the dictionary who each
# contain all the diet restrictions listed in the list,
# sorted alphabetically. If there are no restaurants that
# meet all the restrictions, return the string  "Sorry, no
# #restaurants meet your restrictions". Types of diet
# restrictions that exist in this question's universe are:
# vegetarian, vegan, kosher, gluten-free, dairy-free
#
# For example:
# grading_scale = {"blossom": ["vegetarian", "vegan", "kosher", "gluten-free", "dairy-free"], \
#                 "jacob's pickles": ["vegetarian", "gluten-free"], \
#                 "sweetgreen": ["vegetarian", "vegan", "gluten-free", "kosher"]}
# guests_diet = ["dairy-free"]
# no_you_pick(grading_scale, guests_diet) -> ["blossom"]


# Write your code here!

def no_you_pick(my_dict, my_list):
    output = [x[0] for x in my_dict.items() if set(my_list).issubset(x[1])]
    if len(output) > 0:
        output.sort()
        return output
    return "Sorry, no restaurants meet your restrictions"


grading_scale = {'Moes, Larrys, Curlys': ['vegetarian', 'vegan', 'gluten-free'],
                 'Hot Chili Pepper': ['vegetarian', 'gluten-free', 'vegan']}
guests_diet = ["vegetarian", "vegan", "gluten-free"]
print(no_you_pick(grading_scale, guests_diet))

# Below are some lines of code that will test your function.

# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: blossom
print()
print()


# Your goal in this question is to create a playlist (that is, a list of songs) by your friend's favorite artists.
#
# Write a function called playlist. playlist should have two parameters. The first parameter is a dictionary,
# where the keys are band names and the values are song names. The second parameter is a list of strings, where each
# string is an artist.
#
# playlist should return a list of all songs by the bands listed in the second parameter, sorted alphabetically. If
# there are no matching artists, return "I guess I don't mind ads on the radio that much"
#
# For example: artists_and_songs = {"Beyonce": ["Halo", "Run the World", "Irreplaceable"],\ "Maroon 5": ["Sugar",
# "Payphone", "Memories"], "Harry Styles": \ ["Sign of the Times", "Adore You", "Falling"], "AC/DC":\ ["TNT",
# "It's a long way to the top", "Thunderstruck"]} friends_artists = ["Maroon 5", "AC/DC", "Tame Impala"] playlist(
# artists_and_songs, friends_artists) -> ["It's a long way to the top", "Memories", "Payphone", "Sugar", "TNT",
# "Thunderstruck"]


# Write your code here!
def playlist(artists_song, friends_artists):
    friends_list = []
    for artist in friends_artists:
        for k, v in artists_song.items():
            for songs in v:
                if artist in k:
                    friends_list.append(songs)
    if friends_list:
        friends_list.sort()
        return friends_list

    return "I guess I don't mind ads on the radio that much"


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: ["It's a long way to the top", "Memories", "Payphone", "Sugar", "TNT", "Thunderstruck"]
artists_and_songs = {"Beyonce": ["Halo", "Run the World", "Irreplaceable"], \
                     "Maroon 5": ["Sugar", "Payphone", "Memories"], "Harry Styles": \
                         ["Sign of the Times", "Adore You", "Falling"], "AC/DC": \
                         ["TNT", "It's a long way to the top", "Thunderstruck"]}
friends_artists = ["Maroon 5", "AC/DC", "Tame Impala"]
print(playlist(artists_and_songs, friends_artists))
print()


# Another method use good ol' list comprehension:

def playlist(artists_song, friends_artists):
    output = [songs for k, v in artists_song.items() for songs in v for x in friends_artists if x in k]
    if output:
        output.sort()
        return output

    return "I guess I don't mind ads on the radio that much"


artists_and_songs = {"Beyonce": ["Halo", "Run the World", "Irreplaceable"], \
                     "Maroon 5": ["Sugar", "Payphone", "Memories"], "Harry Styles": \
                         ["Sign of the Times", "Adore You", "Falling"], "AC/DC": \
                         ["TNT", "It's a long way to the top", "Thunderstruck"]}
friends_artists = ["Maroon 5", "AC/DC", "Tame Impala"]
print(playlist(artists_and_songs, friends_artists))

print()


# You are going through your refrigerator at home and trying to determine whether you have the proper ingredients to
# cook a meal.
#
# Write a function called food_at_home. food_at_home should have one parameter, a list of foods in your house as
# strings. In order to cook a meal, the list must contain "cooking oil" and at least one other item. If this criteria
# is not met, return the string "I guess it's pizza tonight". If you do have cooking oil and at least one other food,
# return the string, "You do have food, your options are ... or ... or ...", where the ...s are replaced by the food
# names in the list in the order in which they appear. "cooking oil" should not be one of the foods listed under
# options.
#
# For example:
# food_list = ["chicken", "mixed veggies", "greens", "beans", "corn", "cooking oil"]
# food_at_home(food_list) -> "You do have food, your options are chicken or mixed veggies or greens or beans or corn"


# Write your code here!

def food_at_home(food_list):
    for food_items in food_list:
        if "cooking oil" not in food_list:
            return "I guess it's pizza tonight"
        elif "cooking oil" in food_list and food_items in food_list:
            food_list.remove('cooking oil')
            options = " or ".join(food_list)
            return "You do have food, your options are" + " " + options


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: You do have food, your options are chicken or mixed veggies or greens or beans or corn
food_list = ["chicken", "mixed veggies", "greens", "beans", "corn", "cooking oil"]
print(food_at_home(food_list))
print()


# For this question, your goal is to decipher a text message to plain English.
# You can ignore grammar, you're just translating common text slang into
# normal words.
#
# Write a function called text_deciphered. text_deciphered should have two
# parameters: a string representing a text message, and a dictionary representing
# a set of known abbreviations. In this dictionary, the keys are the English words
# and the values are the abbreviated words.
#
# Return a translated version of the string, replacing the abbreviated words with
# the real English words.
#
# For example:
# text_message = "Hey, wat r our plans for tn"
# abbrevs = {"what": "wat", "are": "r", "tonight": "tn"}
# text_deciphered(text_message, abbrevs) -> "Hey, what are our plans for tonight"


# Write your code here!

def text_deciphered(text, args_dict):
    text_list = []
    for text_str in text.split():
        if text_str not in args_dict.values():
            text_list.append(text_str)

        for k, v in args_dict.items():

            if text_str in v:
                new_item = text_str.replace(text_str, k)
                text_list.append(new_item)

    res = ' '.join(text_list)
    return res


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: Hey, what are our plans for tonight
text_message = "Hey, wat r our plans for tn"
abbrevs = {"what": "wat", "are": "r", "tonight": "tn"}
print(text_deciphered(text_message, abbrevs))
