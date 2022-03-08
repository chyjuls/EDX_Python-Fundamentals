# Write a function called count_types. count_types
# should take as input a single string, and return a
# dictionary. In the dictionary, the keys should be
# types of characters, and the values should be the
# number of times each type of character appeared in
# the string.
#
# The types of characters that should be handled (and
# thus, the keys in the dictionary) are:
#
# - upper: the count of upper-case or capital letters
# - lower: the count of lower-case letters
# - punctuation: the count of punctuation characters.
#   You may assume this is limited to these punctuation
#   characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# - space: the count of spaces
# - numeral: the count of numerals, 0123456789
#
# Note, however, that any type of character that does
# NOT appear in the string should not be in the dictionary
# at all.
#
# For example:
#
# count_characters("aabbccc") ->
# {"lower": 7}
# count_characters("ABC 123 doe ray me!") ->
# {"upper": 3, "lower": 8, "punctuation": 1, "space": 4, "numeral": 3}
#
# Because the first string has only lower-case letters,
# "lower" is the only key in the dictionary.
#
# HINT: If you're sing the ord() function, capitals of
# ordinals between 65 and 90; lower-case letters have
# ordinals between 97 and 122; numerals are between 48
# and 57; spaces are 32; all other numbers between 33
# and 126 are punctuations, and no character will have
# an ordinal outside that range.


# Write your function here!


def count_types(Astring):
    Adict = {}
    characters = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
    characters0 = "'"

    for item in Astring:
        if item.isupper():
            if "upper" not in Adict:
                Adict["upper"] = 1
            else:
                Adict["upper"] += 1
        if item.islower():
            if "lower" not in Adict:
                Adict["lower"] = 1
            else:
                Adict["lower"] += 1

        if item.isnumeric():
            if "numeral" not in Adict:
                Adict["numeral"] = 1
            else:
                Adict["numeral"] += 1

        if item.isspace():
            if "space" not in Adict:
                Adict["space"] = 1
            else:
                Adict["space"] += 1
        if item in characters or item in characters0:
            if "punctuation" not in Adict:
                Adict["punctuation"] = 1
            else:
                Adict["punctuation"] += 1

    return Adict


print(count_types("aabbccc"))
print(count_types("ABC 123 doe ray me!"))
print()


def count_types(string):
    dictionary = {'lower':0, 'upper':0, 'space':0, 'numeral':0, 'punctuation':0}

    # We use a for each loop to go through the input string and check
    # if each character is either an upper, lower, space, numeral, or punctuation.

    for char in string:

        if 'Z' >= char >= 'A':
            dictionary.setdefault("upper", 0)
            dictionary["upper"] += 1
        elif 'z' >= char >= 'a':
            dictionary.setdefault("lower", 0)
            dictionary["lower"] += 1
        elif char == ' ':
            dictionary.setdefault("space", 0)
            dictionary["space"] += 1
        elif '9' >= char >= '0':
            dictionary.setdefault("numeral", 0)
            dictionary["numeral"] += 1
        else:
            dictionary.setdefault("punctuation", 0)
            dictionary["punctuation"] += 1

    # When an if-statement is triggered, we first create the key within the
    # dictionary with the default value of 0. As shown that line is:
    # dictionary.setdefault("upper", 0)
    # The setdefault() method is to create the key in the dictionary. In this
    # case, the key name will be "upper" and the initial value will be 0
    # We need this line because if we just simply increment the value of a key
    # there will be an error since we cannot increment an uninitialized value.
    # This is repeated for all the conditions and at the end we return the dictionary

    return dictionary


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (although the order of the keys may vary):
#
# {"lower": 7}
# {"upper": 3, "lower": 8, "punctuation": 1, "space": 4, "numeral": 3}
print(count_types("aabbccc"))
print(count_types("ABC 123 doe ray me!"))
print()
