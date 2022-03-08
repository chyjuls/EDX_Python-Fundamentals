# Write a function called abstract_names. abstract_names
# should have one parameter: a list of lists. Each list will
# be a list of strings, each with a first name and a last
# name, and each with the same first name.
#
# For example, this could be one list of lists your function
# might receive:
#
# [["David Joyner", "David Tennant", "David Beckham"],
#  ["Ananya Birla", "Ananya Agarwal", "Ananya Chatterjee", "Ananya Roy"],
#  ["Inés Sainz", "Inés Suarez", "Inés Melchor"]]
#
# abstract_names should return a dictionary. The keys to the
# dictionary should be the first names, and the values should
# be lists of the associated last names. The last names should
# be sorted alphabetically.
#
# For example, with the list above, the dictionary returned by
# abstract_names would be:
#
# {"David": ["Beckham", "Joyner", "Tennant"],
#  "Ananya": ["Agarwal", "Birla", "Chatterjee", "Roy"],
#  "Inés": ["Melchor", "Sainz", "Suarez"]}


# Write your function here!
def abstract_names(name_list):
    name_dict = {}
    for names in name_list:  # get lists from list of lists
        for name in names:
            name = name.split()  # get string from list, then split()
            name0 = name[0]  # get fist element of list
            if name0 not in name_dict:  # if not in dict, add
                name_dict[name0] = [name[1]]
            else:
                name_dict[name0] += [name[1]]
        for values in name_dict.values():
            values.sort()
    return name_dict


names = [["David Joyner", "David Tennant", "David Beckham"],
         ["Ananya Birla", "Ananya Agarwal", "Ananya Chatterjee", "Ananya Roy"],
         ["Ines Sainz", "Ines Suarez", "Ines Melchor"]]
print(abstract_names(names))

##another method:
# We create an empty dictionary that will store the names
# in the way the problem asked.

def abstract_names(name_list):
    dictionary = {}

    # We have a for each loop that will go through the name_list
    # which is the list of names given to us

    for fullNameList in name_list:

        # Each 'fullNameList' is another list since the way
        # name_list is formatted is a list within a list.
        #
        # For example, name_list would be ["David Joyner", "David Tennant",
        # "David Beckham"]
        #
        # We sort it before doing anything so that later when we append
        # we are doing it in alphabetical order.

        fullNameList.sort()

        # Within the fullNameList, we iterate with a for
        # each loop to access the fullName
        # With each fullName, we know that first name
        # will always come first, and last name will
        # always be after. Note that fullName as of right now is a
        # string, so we split it to make it accessible per first and
        # last name.

        for fullName in fullNameList:
            first = fullName.split()[0]
            last = fullName.split()[1]

            # An example of fullName is "David Joyner" where first = "David"
            # and last = "Joyner"

            # We now create a key with the first name and append the last names
            # accordingly. The .setdefault() is a method that creates the key
            # if the key does not already exist and sets the initial value to an
            # empty list.

            dictionary.setdefault(first, [])
            dictionary[first].append(last)

    # We return dictionary at the end when everything is finished

    return dictionary


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally print (although the order of the keys may vary): #{"David":
# ["Beckham", "Joyner", "Tennant"], "Ananya": ["Agarwal", "Birla", "Chatterjee", "Roy"], "Inés": ["Melchor", "Sainz",
# "Suarez"]}
names = [["David Joyner", "David Tennant", "David Beckham"],
         ["Ananya Birla", "Ananya Agarwal", "Ananya Chatterjee", "Ananya Roy"],
         ["Ines Sainz", "Ines Suarez", "Ines Melchor"]]
print(abstract_names(names))
