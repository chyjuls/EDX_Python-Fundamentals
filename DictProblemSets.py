print()
# student grades

ANSWER_KEY = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "E"}
students = {}
students["David"] = {"1": "A", "2": "B", "3": "A", "4": "B", "5": "C"}
students["John"] = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "A"}
students["Julius"] = {"1": "A", "2": "C", "3": "C", "4": "D", "5": "A"}
for (student, answers) in students.items():
    grade = 0
    for (question, answer) in answers.items():
        if answer == ANSWER_KEY[question]:
            grade += 1
    students[student]["grade"] = grade
for (student, answers) in students.items():
    print(student, ": ", answers["grade"], sep="", end="; ")
print()

gradebook = {"David": 17, "Sasha": 21, "Jing": 16, "Lucy": 19, "Marguerite": 20, "Maria": 22}
gradebook["Sasha"] += 2
gradebook["Jackie"] = 23
gradebook["David"] = 19
print(gradebook)

for student in gradebook:
    student_grade = gradebook[student]
    if student_grade > 20:
        print(student, "is doing very well!")
# gradebook.append("Peter", 13)

opposites = {}
opposites['up'] = 'down'
opposites['short'] = 'long'
# print(opposites)
for word, opposite in opposites.items():
    print("The opposite of", word, "is", opposite)


def add_grade(gradebook, student_name, new_grade):
    if student_name not in gradebook:
        gradebook[student_name] = []
    gradebook[student_name].append(new_grade)


gradebook = [{"name": "Jack", "homework": 95, "test": 92, "exam": 100},
             {"name": "James", "homework": 95, "test": 92, "exam": 100}
             ]
new_student = {"name": "Samantha", "homework": 95, "test": 92, "exam": 100}
gradebook.append(new_student)
gradebook[0]["exam"] = 100
new_gradebook = {}
new_gradebook[gradebook[0]["name"]] = gradebook[0]
print(new_gradebook)
print()
print()


# -----------------------------------------------------------
# Let's get back to basics for a moment. We're going to write
# a function that very simply reads a dictionary and returns
# a result.
#
# Write a function called safe_lookup. safe_lookup should have
# two parameters: a dictionary and a key. safe_lookup should
# see if the key is in the dictionary. If it is, it should
# return its value. If it not, it should return None (not the
# string, but the value None: return None).
#
# safe_lookup might be used to avoid having to add error
# handling every time a dictionary is used. A programmer could
# call safe_lookup(dict, key) and know that it will not cause
# an error even if key is not found.


# Add your code here!
def safe_lookup(my_dict, my_key):
    try:
        if my_key in my_dict:
            return my_dict.get(my_key)
    except:
        return 'None'


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# 1
# 2
# 3
# None
test_dictionary = {"A": 1, "B": 2, "C": 3}
print(safe_lookup(test_dictionary, "A"))
print(safe_lookup(test_dictionary, "B"))
print(safe_lookup(test_dictionary, "C"))
print(safe_lookup(test_dictionary, "D"))

print()


# One of the confusing things about dictionaries is that they
# are unordered: the keys have no internal ordering to them.
# Sometimes though, you want to look through the keys in a
# particular order, such as printing them alphabetically if
# they represent something like artist names.
#
# For example, imagine if a forum tool used for a course
# exported its data as a dictionary. The keys of the dictionary
# are students' names, and the values are days of activity.
# Your goal is to return a list of students in the class
# in alphabetical order, followed by their days of activity,
# like this:
# Chopra, Deepak: 22
# Joyner, David: 14
# Winfrey, Oprah: 17
#
# Write a function named alphabetical_keys. alphabetical_keys
# should take as input a dictionary, and return a single string.
# The keys of the dictionary will be names and the values will
# be integers. The output should be a single string made of multiple
# lines, following the format above: the name (the key), a colon and
# space, then the number of days of activity (the value), sorted
# alphabetically by key.
#
# Remember, you are _returning_ this as a single string: you're
# going to need to put the \n character after each line.
#
# To convert a dictionary's keys into a list, use this line
# of code:
# keys_as_list = list(the_dict.keys)
#
# From there, you could sort keys_as_list like any normal list.


# Add your code here!
def alphabetical_keys(my_dict):
    dict_list = []

    for key, value in my_dict.items():  # get key/value pair
        temp_string = str(key) + ": " + str(value)  # put them in temp_string
        dict_list.append(temp_string)  # append to list
        dict_list.sort()  # sort list
        dict_list2 = '\n'.join(dict_list)  # convert list to string
    return dict_list2


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# Chopra, Deepak: 22
# Joyner, David: 14
# Winfrey, Oprah: 17
the_dictionary = {"Joyner, David": 14, "Chopra, Deepak": 22, "Winfrey, Oprah": 17}
print(alphabetical_keys(the_dictionary))
print()


# Write a function called name_counts. name_counts will take
# as input a list of full names. Each name will be two words
# separated by a space, like "David Joyner".
#
# The function should return a dictionary. The keys to the
# dictionary will be the first names from the list, and the
# values should be the number of times that first name
# appeared.
#
# HINT: Use split() to split names into first and last.


# Add your function here!
def name_counts(name_list):
    dict_list = {}
    for name in name_list:
        split_name = name.split()
        first_name = split_name[0]
        if first_name in dict_list:
            dict_list[first_name] += 1
        else:
            dict_list[first_name] = 1
    return dict_list


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (although the order of the keys may vary):
# {'Shelba': 5, 'Maren': 1, 'Nicol': 1, 'David': 2, 'Brenton': 2}
name_list = ["David Joyner", "David Zuber", "Brenton Joyner",
             "Brenton Zuber", "Nicol Barthel", "Shelba Barthel",
             "Shelba Crowley", "Shelba Fernald", "Shelba Odle",
             "Shelba Fry", "Maren Fry"]
print(name_counts(name_list))
print()


def name_count(nameList):
    dict_list2 = {}
    first = [x.split()[0] for x in nameList]
    # print(first)

    for name_1 in first:
        if name_1 in dict_list2:
            dict_list2[name_1] += 1
        else:
            dict_list2[name_1] = 1
    return dict_list2


another_list = ["David Joyner", "David Zuber", "Brenton Joyner",
                "Brenton Zuber", "Nicol Barthel", "Shelba Barthel",
                "Shelba Crowley", "Shelba Fernald", "Shelba Odle",
                "Shelba Fry", "Maren Fry"]
print(name_count(name_list))
print()


# Write a function called most_active. most_active should take
# one parameter, a dictionary. The dictionary's keys will all
# be strings representing people's names. The dictionary's
# values will be integers representing days of activity on a
# course forum.
#
# most_active should return the name of the most active student
# in the class. That is, most_active should return the key
# whose value is the highest in the dictionary.
#
# For example:
#
# some_dictionary = {"Joyner, David": 14, "Chopra, Deepak": 22, "Winfrey, Oprah": 17}
# most_active(some_dictionary) -> "Chopra, Deepak"
#
# The key "Chopra, Deepak" has the highest value (22), so
# the function returns "Chopra, Deepak". You may assume
# there will not be a tie for most active.


# Add your code here!
def most_active(some_dict):
    max_val = max(some_dict, key=some_dict.get)
    return max_val


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# Chopra, Deepak
some_dictionary = {"Joyner, David": 14, "Chopra, Deepak": 22, "Winfrey, Oprah": 17}
print(most_active(some_dictionary))
print()


# In the previous problem, you were given a dictionary where
# the keys were names and the values were days of activity
# on a class forum. You returned the name of the most active
# student; or, more simply, the key corresponding to the
# highest value.
#
# In this problem, you'll do the same thing, but with a more
# complex data structure. Your function should be called
# most_active, and it should have one parameter.
#
# Instead of a dictionary, your parameter is a list of
# dictionaries. Every dictionary in the list will have exactly
# two keys: 'name' and 'days_active'. Your goal, as before,
# is to return the name of the most active student.
#
# Some of the code you wrote on the previous problem will be
# reusable, but you'll need to modify it.
#
# Hint: you do NOT need to iterate over the keys in the
# dictionaries inside the lists. You can always just access
# the_dict["name"] and the_dict["days_active"] directly.
# Your only loop should be the loop over the list.


# Add your code here!
def most_active(dict_list2):
    new_dict = {}
    for my_dict in dict_list2:
        new_dict[my_dict["name"]] = my_dict["days_active"]
    max_val2 = max(new_dict, key=new_dict.get)
    return max_val2


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# Chopra, Deepak
the_list = [{"name": "Joyner, David", "days_active": 14},
            {"name": "Chopra, Deepak", "days_active": 22},
            {"name": "Winfrey, Oprah", "days_active": 17}]
print(most_active(the_list))

print()


# Write a function called phonebook that takes two lists as
# input:
#
# - names, a list of names as strings
# - numbers, a list of phone numbers as strings
#
# phonebook() should take these two lists and create a
# dictionary that maps each name to its phone number. For
# example, the first name in names should become a key in
# the dictionary, and the first number in numbers should
# become the value corresponding to the first name. Then, it
# should return the dictionary that results.
#
# Hint: Because you're mapping the first name with the first
# number, the second name with the second number, etc., you do
# not need two loops. For a similar exercise, check back on
# Coding Problem 4.3.3, the Scantron grading problem.
#
# You may assume that the two lists have the same number of
# items: there will be no names without numbers or numbers
# without names.


# Write your function here!
def phonebook(name_list, phone_list):
    keys_list = name_list
    values_list = phone_list
    zip_iterator = zip(name_list, phone_list)
    a_dictionary = dict(zip_iterator)
    return a_dictionary


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (although the order of the keys may vary):
# {'Jackie': '404-555-1234', 'Joshua': '678-555-5678', 'Marguerite': '770-555-9012'

name_list = ['Jackie', 'Joshua', 'Marguerite']
number_list = ['404-555-1234', '678-555-5678', '770-555-9012']
print(phonebook(name_list, number_list))


# Another method:

def phonebook(name_list, phone_list):
    aDict = {}
    index = 0
    while index < len(name_list):
        aDict[name_list[index]] = phone_list[index]
        index += 1
    return aDict


name_list = ['Jackie', 'Joshua', 'Marguerite']
number_list = ['404-555-1234', '678-555-5678', '770-555-9012']
print(phonebook(name_list, number_list))

print()
# Do not change the line of code below. It's at the top of
# the file to ensure that it runs before any of your code.
# You will be able to access french_dict from inside your
# function.
french_dict = {"me": "moi", "hello": "bonjour",
               "goodbye": "au revoir", "cat": "chat",
               "dog": "chien", "and": "et"}


# Write a function called french2eng that takes in one string
# parameter called sentence. french2eng should look at each
# word in the sentence and translate it into French if it is
# found in the dictionary, french_dict. If a word is not found
# in the dictionary, do not translate it: use the original
# word. Then, the function should return a string of the
# translated sentence.
#
# You may assume that the sentence you're translating has no
# punctuation. However, you should convert it to lower case
# before translating.
#
# For example:
#
#  french2eng("Hello it's me") -> "bonjour it's moi"
#
# Hint: Use .split() to get a list of strings representing
# each word in the string, then use ' '.join to merge the
# translated list back into one string.
#
# Hint 2: Remember, lists are mutable, so we can change
# individual items in the list. However, to change an item
# in a list, we must change it using its index. We can
# write lines like my_words[1] = new_word.
#
# Hint 3: If you're stuck, try breaking it down into small
# parts. How do you access an item from a list? How do you
# look up a key in a dictionary? How do you change the
# value of an item in a list? How do you check if a key is
# in the dictionary?


# Write your function here!

def french2eng(eng_string):
    eng_string = eng_string.lower()  # first cob=vert to lower case
    mlist = eng_string.split(" ")  # split string into lists
    for i in range(len(mlist)):  # find index in list length
        for key in french_dict.keys():
            if key == mlist[i]:  # index of list
                mlist[i] = french_dict[key]  # if index == key
            else:
                pass
    eng_string = ' '.join(mlist)
    return eng_string


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: bonjour it's moi
print(french2eng("Hello it's me"))


# Write a function called course_info that takes as input a
# list of tuples. Each tuple contains two items: the first
# item in each tuple is a student's name as a string, and the
# second item in each tuple is that student's age as an
# integer.
#
# The function should return a dictionary with two keys.
# The key "students" should have as its value a list of all
# the students (in other words, a list made from the first
# value of each tuple), in the original order in which they
# appeared in the list. The key "avg_age" should have as its
# value a float representing the average age of all the
# students in the list (in other words, the average of all
# the second items in the tuples).
#
# For example:
#
#  course_info([("Jackie", 20), ("Marguerite", 21)])
#  -> {"students": ['Jackie', 'Marguerite'], "avg_age": 20.5}
#
# Hint: Concentrate first on building the list of students
# and calculating the average age. Save creating the
# dictionary for last.


# Write function here:

def course_info(student_tuple):
    new_list = []
    list_dict = {}
    avg_age = 0
    for tuple_list in student_tuple:
        new_list.append(tuple_list[0])
        avg_age += tuple_list[1]
        list_dict["students"] = new_list
        list_dict["avg_age"] = float(avg_age / len(student_tuple))

    return list_dict


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (although the order of the keys may vary):
# {'avg_age': 20.5, 'students': ['Jackie', 'Marguerite']}
print(course_info([("Jackie", 20), ("Marguerite", 21)]))


# Another method:

def course_info(student_list):
    # There are two high-level ways we can do this: we could
    # create the list and float first, and create the
    # dictionary last; or, we could create the dictionary
    # first and change it directly.
    #
    # The first one is probably a little easier, so let's
    # start there. First, we create an empty list for the
    # student names, and a sum to add up all their ages:

    students = []
    total_age = 0

    # Then, we want to iterate through the list of tuples:

    for student_tuple in student_list:
        # For each one, we want to add the name to the list
        # and add the age to total_age. To make this easier,
        # let's first unpack the tuple. Remember, the name
        # is first and the age is second:

        student_name, student_age = student_tuple

        # This unpacks the first item of student_tuple to
        # student_name, and the second item to student_age.
        #
        # Now, let's add student_name to the list:

        students.append(student_name)

        # ...and add the age to total_age:

        total_age += student_age

    # That's all we need to do inside the loop! When the
    # loop is done running, students will be a list of all
    # the names, and student_age will be the sum of their
    # ages. Now all we need to do is divide student_age by
    # the number of students, and then create the dictionary.
    # We can do this all at once:

    student_info = {"students": students, "avg_age": total_age / len(student_list)}

    # We can do that calculation for avg_age in-line, or we
    # could separate it out into a separate calculation.
    #
    # Finally, we return our result:

    return student_info


print(course_info([("Jackie", 20), ("Marguerite", 21)]))
print()


# Write a function called modify_dict. modify_dict takes one
# parameter, a dictionary. The dictionary's keys are people's
# last names, and the dictionary's values are people's first
# names. For example, the key "Joyner" would have the value
# "David".
#
# modify_dict should delete any key-value pair for which the
# key's first letter is not capitalized. For example, the
# key-value pair "joyner":"David" would be deleted, but the
# key-value pair "Joyner":"david" would not be deleted. Then,
# return the modified dictionary.
#
# Remember, the keyword del deletes items from lists and
# dictionaries. For example, to remove the key "key!" from
# the dictionary my_dict, you would write: del my_dict["key!"]
# Or, if the key was the variable my_key, you would write:
# del my_dict[my_key]
#
# Hint: If you try to delete items from the dictionary while
# looping through the dictionary, you'll run into problems!
# We should never change the number if items in a list or
# dictionary while looping through those items. Think about
# what you could do to keep track of which keys should be
# deleted so you can delete them after the loop is done.
#
# Hint 2: To check if the first letter of a string is a
# capital letter, use string[0].isupper().


# Write your function here!
# first create a function.
# create a variable list []
# key/value pair using .items()
# check if key starts with lower case
## append to the list.
# else: pass (empty statement)
# loop through the list to check
# delete the item as key in dict.
def modify_dict(my_dict):
    my_list = []
    for last_name, first_name in my_dict.items():
        if last_name.islower():
            my_list.append(last_name)
        else:
            pass
    for item in my_list:
        del my_dict[item]
    return my_dict


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (although the order of the keys may vary):
#  {'Diaddigo':'Joshua', 'Elliott':'jackie'}
my_dict = {'Joshua': 'Diaddigo', 'joyner': 'David', 'Elliott': 'jackie', 'murrell': 'marguerite'}
print(modify_dict(my_dict))
print()


# Another method, similar to above:

def modify_dict(name_dict):
    # The hint in the original instructions tells you that
    # we can't iterate through the dictionary and delete
    # items from it at the same time. Why not? When
    # iterating, Python keeps a pointer to the current item.
    # When you delete an item, every item slides back one
    # spot -- so the pointer is now pointing to what *was*
    # the next item. Then, when it gets the next item, it
    # skips what was actually the next item.
    #
    # So instead, we want to first make a list of all the
    # keys we want to delete. First, we initialize an
    # empty list:

    del_list = []

    # Then we iterate through the keys:

    for key in name_dict:

        # And if the key is not capitalized (e.g. if it
        # does not equal the capitalized version of
        # itself)...

        if key != key.capitalize():
            # ...then we add it to our list of keys to
            # delete:

            del_list.append(key)

    # Once that's done, del_list has a list of all the
    # keys in name_dict to delete. Now we want to iterate
    # through the keys we stored into del_list. Note that
    # this is okay because we're iterating through del_list
    # and deleting from name_dict, *not* iterating through
    # name_dict:

    for key in del_list:
        del name_dict[key]

    # After that, name_dict is modified with the new value,
    # so we just return it:

    return name_dict


my_dict = {'Joshua': 'Diaddigo', 'joyner': 'David', 'Elliott': 'jackie', 'murrell': 'marguerite'}
print(modify_dict(my_dict))
print()


# Write a function called clean_data. clean_data takes one
# parameter, a dictionary. The dictionary represents the
# observed rainfall in inches on a particular calendar day
# at a particular location. However, the data has some
# errors.
#
# clean_data should delete any key-value pair where the value
# has any of the following issues:
#
# - the type is not an integer or a float. Even if the value
#   is a string that could be converted to an integer (e.g.
#   "5") it should be deleted.
# - the value is less than 0: it's impossible to have a
#   negative rainfall number, so this must be bad data.
# - the value is greater than 100: the world record for
#   rainfall in a day was 71.8 inches
#
# Return the dictionary when you're done making your changes.
#
# Remember, the keyword del deletes items from lists
# and dictionaries. For example, to remove the key "key!" from
# the dictionary my_dict, you would write: del my_dict["key!"]
# Or, if the key was the variable my_key, you would write:
# del my_dict[my_key]
#
# Hint: If you try to delete items from the dictionary while
# looping through the dictionary, you'll run into problems!
# We should never change the number if items in a list or
# dictionary while looping through those items. Think about
# what you could do to keep track of which keys should be
# deleted so you can delete them after the loop is done.
#
# Hint 2: To check if a variable is an integer, use
# type(the_variable) == int. To check if a variable is a float,
# use type(the_variable) == float.


# Write your function here!
def clean_data(my_rainfall):
    delete_data = []
    for key_data, val_data in my_rainfall.items():
        if type(val_data) != int and type(val_data) != float:
            delete_data.append(key_data)

        elif val_data < 0 or val_data > 100:
            delete_data.append(key_data)

    for item in delete_data:
        del my_rainfall[item]
    return my_rainfall


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (although the order of the keys may vary):
# {"20190101": 5, "20190103": 7.5, "20190104": 0, "20190107": 1}
rainfall = {"20190101": 5, "20190102": "6", "20190103": 7.5,
            "20190104": 0, "20190105": -7, "20190106": 102,
            "20190107": 1}
print(clean_data(rainfall))
print()


# Recall in an earlier problem you were given two lists: one
# list was a student's answers to a test, and the other was
# the answer key. Your goal was to return a score
# representing the number of problems the student got correct.
#
# Let's do that again, but with dictionaries instead of lists.
# Write a function called calculate_score. calculate_score
# should take two parameters: a dictionary of student answers
# and a dictionary of correct answers. Both dictionaries should
# have integers as their keys, and one-character strings as
# their values.
#
# calculate_score should count how many questions the student
# got right. Or, in more precise terms, calculate_score should
# count how many keys for which the associated value is the
# same in the student's dictionary and in the answer key
# dictionary.
#
# As before, it is possible that there will be more answers in
# one than the other. This means that these answers don't
# belong to the same test! If that happens, return -1.


# Add your function here!

def calculate_score(stud_answers, correct_answers):
    grade = 0
    if len(stud_answers) == len(correct_answers):
        for key in stud_answers:
            if (key in correct_answers and stud_answers[key] == correct_answers[key]):
                grade += 1
        return grade
    else:
        return -1


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 3
student_answers = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}
correct_answers = {1: "A", 2: "B", 3: "A", 4: "D", 5: "B"}
print(calculate_score(student_answers, correct_answers))
print()


# -----------------------------------------------------------
# Another method:
# First, we define the function:

def calculate_score(student, correct):
    # Next, I'm going to check to see if the lengths of the
    # two dictionaries are the same. If not, we'll go ahead
    # and return -1:
    if not len(student) == len(correct):
        return -1

    # You might be tempted to do this with error handling, and
    # you'd be pretty close: after all, if we try to access a
    # key that doesn't exist in one dictionary, then an error
    # will occur, and we could handle that and return -1.
    #
    # The problem with that approach is: how do we know which
    # dictionary to iterate through? If we iterate through the
    # shorter one, then we'll never try to access a key that
    # doesn't exist because we're not checking the keys of the
    # longer one. So, it's better to just handle this case
    # manually.

    # Next, since we're counting something, we'll initialize a
    # counter:
    total = 0

    # Now, we want to iterate through all the key-value pairs in
    # either dictionary. It doesn't really matter which, so I'll
    # go through the student's:
    for (question, answer) in student.items():

        # With this loop, we know that 'answer' is the student's
        # answer to the question given by 'question'. So, we need
        # to see if the answer corresponding to the same key from
        # the answers is the same.
        #
        # Here's how we can do that:
        if answer == correct[question]:
            # That simple line is somewhat complex. answer is the
            # answer we already know the student put. correct is
            # the dictionary of correct answers. question is the
            # number of the problem, which we can use as a key to
            # the correct dictionary to find its value for that
            # question.
            #
            # If they're the same, we add one to the score:
            total += 1

    # And at the end, we return the total score:
    return total


student_answers = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}
correct_answers = {1: "A", 2: "B", 3: "A", 4: "D", 5: "B"}
print(calculate_score(student_answers, correct_answers))
print()


# In the Pokemon video game series, every Pokemon has six
# stats: HP, Attack, Defense, Special Attack, Special Defense,
# and Speed.
#
# Write a function called total_stats that will take as input
# a list of dictionaries. Each dictionary will have seven
# key-value pairs:
#
# - name: a Pokemon's name
# - hp, attack, defense, special attack, special defense,
#   and speed: an integer representing that Pokemon's stat
#   in that category
#
# Your function should return a single dictionary. The keys
# of the dictionary should be the Pokemon names from the
# original list, and the values should be the _total_ stats
# for each Pokemon (add HP, Attack, Defense, Special Attack,
# Special Defense, and Speed).
#
# For example, if this was one of the dictionaries in the
# original list:
#
# {"name": "Bulbasaur", "hp": 45, "attack": 49, "defense": 49,
# "special attack": 65, "special defense": 65, "speed": 45}
#
# Then one of the key-value pairs in the dictionary you
# return would be: "Bulbasaur": 318 (45 + 49 + 49 + 65 + 65 +
# 45 = 318).


# Add your function here!

def total_stats(dict_list):
    new_dict = {}  # create an empty

    for list_dict in dict_list:  # get your dict in a list of dicts
        name = list_dict["name"]  # get first name assign to a variable
        add_val = list_dict["hp"] + list_dict["attack"] + list_dict["defense"] + list_dict["special attack"] + \
                  list_dict["special defense"] + list_dict["speed"]
        new_dict[name] = add_val
    return new_dict


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (although the order of the keys may vary):
# {'Bulbasaur': 318, 'Charmander': 309, 'Squirtle': 314}
starters = [{"name": "Bulbasaur", "hp": 45, "attack": 49, "defense": 49, "special attack": 65, "special defense": 65,
             "speed": 45},
            {"name": "Charmander", "hp": 39, "attack": 52, "defense": 43, "special attack": 60, "special defense": 50,
             "speed": 65},
            {"name": "Squirtle", "hp": 44, "attack": 48, "defense": 65, "special attack": 50, "special defense": 64,
             "speed": 43}]
print(total_stats(starters))
