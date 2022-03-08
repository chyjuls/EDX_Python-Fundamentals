# APA citation style cites author names like this:
#
#  Last, F., Joyner, D., & Burdell, G.
#
# Note the following:
#
# - Each individual name is listed as the last name, then a
#   comma, then the first initial, then a period.
# - The names are separated by commas, including the last
#   two.
# - There is also an ampersand and additional space before
#   the final name.
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
print(names_to_apa("First Last, David Joyner, and George Burdell"))
