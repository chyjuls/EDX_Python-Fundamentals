# Write a function called population_density. The function
# should take one parameter, which will be a list of
# dictionaries. Each dictionary in the list will have three
# key-value pairs:
#
# - name: the name of the country
# - population: the population of that country
# - area: the area of that country (in km^2)
#
# Your function should return the population density of all
# the countries put together. You can calculate this by
# summing all the populations, summing all the areas, and
# dividing the total population by the total area.
#
# Note that the input to this function will look quite long;
# don't let that scare you. That's just because dictionaries
# take a lot of text to define.


# Add your function here!
def population_density(country_listdict):
    total_pop = 0
    total_area = 0
    for countries in country_listdict:
        total_pop += countries["population"]
        total_area += countries["area"]
        density = total_pop / total_area
    return density


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 133.886 (or something around there)
countries = [{"name": "China", "population": 1390700000, "area": 9640821},
             {"name": "India", "population": 1348003000, "area": 3287240},
             {"name": "United States", "population": 325300000, "area": 9826675},
             {"name": "Indonesia", "population": 237556363, "area": 1904569}]
print(population_density(countries))

print()


# Write a function called word_lengths, which takes in one
# parameter, a string, and returns a dictionary where each
# word of the string is mapped to an integer representing how
# how long that word is. You should ignore punctuation, and
# all the words should be lowercase. You can assume that the
# only punctuation marks in the string will be periods,
# commas, question marks, exclamation points, and apostrophes.
#
# For example:
#  word_lengths("I ate a bowl of cereal out of a dog bowl today.")
#  -> {'i':1, 'bowl':4, 'today':5, 'out':3, 'dog':3, 'ate':3,
#      'a':1, 'of':2, 'cereal':6}
#
# Hint: Use the split() method to split by spaces, and don't
# forget to remove punctuation marks.  Remember also: strings
# are immutable, so operations like my_string.lower() don't
# change the value of my_string like list methods: to save
# those results, you'd write my_string = my_string.lower().
#
# Your dictionary should not have any duplicate keys (in fact,
# Python won't allow a dictionary to have duplicate keys).


# Write your function here!

def word_lengths(dict_string):
    word_dict = {}
    word_string = dict_string.replace(".", "")

    word_string = word_string.replace("!", "")

    word_string = word_string.replace(",", "")

    word_string = word_string.replace("'", "")
    word_string = word_string.replace("?", "")
    word_string = word_string.lower()
    word_string_split = word_string.split(" ")

    for word in word_string_split:
        index = len(word)
        word_dict[word] = index
    return word_dict


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# {'dog': 3, 'today': 5, 'of': 2, 'ate': 3, 'bowl': 4, 'out': 3, 'a': 1, 'cereal': 6, 'i': 1}
#
# The order of the keys may differ, but that's okay!
print(word_lengths("I ate a bowl of cereal out of a dog bowl today."))
print()

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
from itertools import takewhile


def average_rainfall(a_list):
    l = [*takewhile(lambda k: k >= 0, a_list)]
    return sum(l) / len(l)


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 3.0
a_list = [1, 2, 3, 4, 5, -1, 6, 7]
print(average_rainfall(a_list))

print()


def average_rainfall(the_list):
    new_list = []
    for i in the_list:
        if i >= 0:
            new_list.append(i)

        if i < 0:
            break
    answer = sum(new_list) / len(new_list)
    return answer


a_list = [1, 2, 3, 4, 5, -1, 6, 7]
print(average_rainfall(a_list))
print()


# In the previous problem, you were given a list of integers
# representing the amount of rainfall on each of multiple
# days. Somewhere in the list was the number -1. You were
# asked to find the average of the numbers prior to the -1.
#
# Geometric mean is a different measurement of central
# tendency used in math and statistics. With a regular mean,
# you sum the numbers, then divide the sum by how many
# values there were. With a geometric mean, you multiply the
# numbers, and then you take the nth root of the product,
# where n is the number of values.
#
# For example, if the five values were 1, 2, 3, 4, 5, then
# you would first multiply the values:
#
# 1 x 2 x 3 x 4 x 5 = 120
#
# ...and then take the 5th root because there are 5 numbers.
# The simplest way to take the 5th root is to raise the
# number to the 1/5 power:
#
# (120) ** (1/5) = 2.6

# Write a function called geometric_rainfall.
# geometric_rainfall should have one parameter, a list of
# integers. geometric_rainfall should calculate the
# geometric mean of all values in the list _before_ the
# first -1.
#
# For example:
#
# geometric_rainfall([1, 2, 3, 4, 5, -1, 6, 7]) -> 2.6
#
# The function would find the geometric mean of 1, 2, 3,
# 4, and 5, and ignore any values after the -1.
#
# You may assume all the items in the list are integers,
# that -1 is guaranteed to occur somewhere in the list,
# and that -1 will not be the first item in the list.


# Add your code here!
def geometric_rainfall(my_list):
    new_list = []
    product = 1
    result = 0
    for i in my_list:
        if i >= 0:
            new_list.append(i)
            product = product * i

        if i < 0:
            break
    result = (product) ** (1 / len(new_list))
    return result


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 2.6
a_list = [1, 2, 3, 4, 5, -1, 6, 7]
print(geometric_rainfall(a_list))
print()


# Recall last exercise that you wrote a function, word_lengths,
# which took in a string and returned a dictionary where each
# word of the string was mapped to an integer value of how
# long it was.
#
# This time, write a new function called length_words so that
# the returned dictionary maps an integer, the length of a
# word, to a list of words from the sentence with that length.
# If a word occurs more than once, add it more than once. The
# words in the list should appear in the same order in which
# they appeared in the sentence.
#
# For example:
#
#  length_words("I ate a bowl of cereal out of a dog bowl today.")
#  -> {3: ['ate', 'dog', 'out'], 1: ['a', 'a', 'i'],
#      5: ['today'], 2: ['of', 'of'], 4: ['bowl'], 6: ['cereal']}
#
# As before, you should remove any punctuation and make the
# string lowercase.
#
# Hint: To create a new list as the value for a dictionary key,
# use empty brackets: lengths[wordLength] = []. Then, you would
# be able to call lengths[wordLength].append(word). Note that
# if you try to append to the list before creating it for that
# key, you'll receive a KeyError.


# Write your function here!
def length_words(sentence):
    sentence = sentence.lower()
    to_replace = ".,'!?"
    for mark in to_replace:
        sentence = sentence.replace(mark, "")
        print(sentence)
    sentence = sentence.split(' ')
    lengths = {}
    for word in sentence:
        word_length = len(word)
        if word_length in lengths:
            lengths[word_length].append(word)
        else:
            lengths[word_length] = [word]

    return lengths


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# {1: ['i', 'a', 'a'], 2: ['of', 'of'], 3: ['ate', 'out', 'dog'], 4: ['bowl', 'bowl'], 5: ['today'], 6: ['cereal']}
#
# The keys may appear in a different order, but within each
# list the words should appear in the order shown above.
print(length_words("Wow, Does that work?"))
print()


# Write a function called most_oscars, which takes in one
# parameter, a dictionary. This dictionary maps names to the
# number of Academy Awards for which they have been nominated.
# This function should return a tuple containing the name and
# number of nominations for the person who has the most
# nominations.
#
# You may assume there will not be a tie for the actor with
# the most nominations (although there may be other ties in
# the list).


# Write your function here!
def most_oscars(dic):
    new_value = []
    max_value = max(dic.values())  # maximum value
    max_keys = [k for k, v in dic.items() if v == max_value]  # getting all keys containing the `maximum`
    new_value.append(max_value)
    new_max_list = max_keys + new_value
    new_max_list = tuple(new_max_list)
    return new_max_list


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: ('Meryl Streep', 20)
nominees = {'Meryl Streep': 20, 'Robert De Niro': 7, 'Michael Caine': 6, 'Maggie Smith': 6}
print(most_oscars(nominees))
print()


# Sample answer:

def most_oscars(oscar_dict):
    # There are several slightly different ways we could
    # do this. This is mine, but yours might differ.
    #
    # At a high level, we want to keep track of who has
    # the most nominations of the people we've looked at
    # so far, and update that if we encounter someone
    # with more nominations. So, we need to keep track
    # of a name...

    current_max_person = ""

    # ...and a number. However, we can easily look up
    # the number associated with the current name in the
    # dictionary, so I'm not going to have a separate
    # variable for that. You'll see why shortly.
    #
    # So, now we need to iterate through all the keys
    # in the dictionary. We could also go ahead and
    # iterate over the values, but let's stick to just
    # the keys:

    for person in oscar_dict:

        # Now we want to check if this current person
        # has more Oscars than the current maximum
        # we've found. The only caveat is that if this
        # is the first person we've checked, we want to
        # copy their name in no matter what. So, we do
        # this:
        #
        # If this is the first person, set this person
        # as our current_max_person:

        if current_max_person == "":
            current_max_person = person

        # Otherwise, if this is not the first person,
        # but this person has more nominations than the
        # current max person, set this person as our
        # current_max_person:
        elif oscar_dict[current_max_person] < oscar_dict[person]:
            current_max_person = person

    # When that loop is done, current_max_person will be
    # the key in the dictionary that corresponds to the
    # largest value. So, we can return that key and its
    # value from the dictionary:

    return (current_max_person, oscar_dict[current_max_person])


winners = {'Meryl Streep': 20, 'Robert De Niro': 7, 'Michael Caine': 6, 'Maggie Smith': 6}
print(most_oscars(winners))
print()


# Recall in coding problem 4.4.3 that you wrote a function
# called "reader" that read a .cs1301 file and returned a
# list of lists.
#
# Let's revise that problem. Instead of a list of lists,
# that's return a dictionary of dictionaries.
#
# Write a function called "reader" that takes one parameter,
# a filename as a string corresponding to a .cs1301 file,
# and reads in that .cs1301 file.
#
# Each line of the .cs1301 file will have five items, each
# separated by a space: the first, third, and fourth will
# represent integers, the second will be a string, and the
# fifth will represent a float. (Note: when reading the
# file, these will all be strings; you can assume each of
# these strings can be converted to the corresponding data
# type, however.)
#
# The function should return a dictionary of dictionaries
# representing the file contents.
#
# The keys of the top-level dictionary should be the
# assignment names. Then, the value for each of those keys
# should be a dictionary with four keys: "number", "grade",
# "total", and "weight". The values corresponding to each of
# those four keys should be the values from the file,
# converted to the corresponding data types (ints or floats).
#
# For example, if the input file read:
#
# 1 exam_1 90 100 0.6
# 2 exam_2 95 100 0.4
#
# Then reader would return this dictionary of dictionaries:
#
# {"exam_1": {"number": 1, "grade": 90, "total": 100, "weight": 0.6},
#  "exam_2": {"number": 2, "grade": 95, "total": 100, "weight": 0.4}}
#
# Hint: Although the end result is pretty different, this
# should only dictate a minor change to your original
# Problem 4.4.3 code!

# Write your function here!
def reader(my_grade_file):
    new_dict_list = {}
    with open(my_grade_file, "r") as new_read_file:
        for lines in new_read_file:
            all_lines = lines.split(" ")

            new_dict_list[str(all_lines[1])] = {"number": int(all_lines[0]), "grade": int(all_lines[2]),
                                                "total": int(all_lines[3]), "weight": float(all_lines[4])}
    new_read_file.close()
    return new_dict_list


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (although the order of the keys may vary):
# {'assignment_1': {'total': 100, 'number': 1, 'grade': 85, 'weight': 0.25}, 'test_1': {'total': 100, 'number': 2, 'grade': 90, 'weight': 0.25}, 'exam_1': {'total': 100, 'number': 3, 'grade': 95, 'weight': 0.5}}
print(reader("sample.cs1301"))
print()


# This is a challenging one! The output will be very long as
# you'll be working on some pretty big dictionaries. We don't
# expect everyone to be able to do it, but it's a good chance
# to test how far you've come!
#
# Write a function called stars that takes in two
# dictionaries:
#
# - movies: a dictionary where the keys are movie titles and
#   the values are lists of major performers in the movie. For
#   example: movies["The Dark Knight"] = ["Christian Bale",
#   "Heath Ledger", "Maggie Gyllenhall", "Aaron Eckhart"]
# - tvshows: a dictionary where the keys are TV show titles
#   and the values lists of major performers in the show.
#   For example: tvshows["Community"] = ["Joel McHale", "Alison
#   Brie", "Danny Pudi", "Donald Glover", "Yvette Brown"]
#
# The function stars should return a new dictionary. The keys
# of the new dictionary should be the performers' names, and
# the values for each key should be the list of shows and
# movies in which that performer has appeared. Sort the shows
# and movies alphabetically.

# Write your function here!

def stars(movies, tv_shows):
    new_dict = {}

    for movie, actor_movie in movies.items():
        for item in actor_movie:  # value
            if item in new_dict:
                new_dict[item].append(movie)
            else:
                new_dict[item] = [movie]
    for tv_show, tv_actor in tv_shows.items():
        for item in tv_actor:
            if item in new_dict:
                new_dict[item].append(tv_show)
            else:
                new_dict[item] = [tv_show]
    for key, value in new_dict.items():
        value.sort()
    return new_dict


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (although the order of the keys may vary):
#
# {'Portia de Rossi': ['Arrested Development'], 'Will Ferrell': ['The Lego Movie'], 'Yvette Brown': ['Community'],
# 'Rebel Wilson': ['How to Be Single'], 'Danny Pudi': ['Community'], 'Elizabeth Banks': ['30 Rock', 'The Lego
# Movie'], 'Alec Baldwin': ['30 Rock'], 'Alison Brie': ['Community', 'How to Be Single', 'The Lego Movie'],
# 'Tina Fey': ['30 Rock'], 'Dakota Johnson': ['How to Be Single'], 'Joel McHale': ['Community'], 'Jack McBrayer': [
# '30 Rock'], 'Tracy Morgan': ['30 Rock'], 'Donald Glover': ['Community'], 'Will Arnett': ['Arrested Development',
# 'The Lego Movie'], 'Jason Bateman': ['Arrested Development']}

movies = {"How to Be Single": ["Alison Brie", "Dakota Johnson",
                               "Rebel Wilson"],
          "The Lego Movie": ["Will Arnett", "Elizabeth Banks",
                             "Alison Brie", "Will Ferrell"]}
tvshows = {"Community": ["Alison Brie", "Joel McHale",
                         "Danny Pudi", "Yvette Brown",
                         "Donald Glover"],
           "30 Rock": ["Tina Fey", "Tracy Morgan", "Jack McBrayer",
                       "Alec Baldwin", "Elizabeth Banks"],
           "Arrested Development": ["Jason Bateman", "Will Arnett",
                                    "Portia de Rossi"]}
print(stars(movies, tvshows))
print()


# Another method by creating two functions, this is more efficient:

def movies_to_performers(orig_dict, new_dict):
    for performance, performers in orig_dict.items():
        for performer in performers:
            if performer not in new_dict:
                new_dict[performer] = []
            new_dict[performer].append(performance)


# Compare this to the reasoning in sample_answer_1.py.
# You'll see it's *identical*: all we did was replace
# movies or tvshows with orig_dict, and movie or tvshow
# with performance.
#
# What good does that do us? Check out how simple our
# stars() function is now:

def stars(movies, tvshows):
    new_dict = {}
    movies_to_performers(movies, new_dict)
    movies_to_performers(tvshows, new_dict)

    for performer, performances in new_dict.items():
        performances.sort()
    return new_dict

    # By using a function like movies_to_performers, we let
    # ourselves call that long block of code multiple times
    # in only one line of code each.


movies = {"How to Be Single": ["Alison Brie", "Dakota Johnson",
                               "Rebel Wilson"],
          "The Lego Movie": ["Will Arnett", "Elizabeth Banks",
                             "Alison Brie", "Will Ferrell"]}
tvshows = {"Community": ["Alison Brie", "Joel McHale",
                         "Danny Pudi", "Yvette Brown",
                         "Donald Glover"],
           "30 Rock": ["Tina Fey", "Tracy Morgan", "Jack McBrayer",
                       "Alec Baldwin", "Elizabeth Banks"],
           "Arrested Development": ["Jason Bateman", "Will Arnett",
                                    "Portia de Rossi"]}
print(stars(movies, tvshows))
print()
# use this to save file:
with open("marta.csv", "w") as marta_file:
    marta_file.write('''01/18/2016,12:01:08,RVG10405,30,9,3E8CADDB574A4E4A
01/18/2016,08:01:06,RVG10402,30,9,3E8CADDF4A674E4A
01/18/2016,16:01:03,RVG10402,30,9,3E8CADF935024E4A
01/18/2016,06:01:19,RVG10402,30,9,3E8CADEFC9EF4E4A
01/18/2016,06:01:49,RVG10402,30,10,3E8CADE945914E4A
01/18/2016,15:01:22,RVG10404,30,10,3E8CADEEDC244E4A
01/18/2016,10:01:04,RVG10505,31,9,3E8CADD98AEF4E4A
01/18/2016,16:01:10,RVG10505,31,10,3E8CADEAA6A54E4A
01/18/2016,16:01:10,RVG10505,31,9,3E8CADEAA6A54E4A
01/18/2016,17:01:00,RVG10504,31,10,3E8CADF990EE4E4A
''')

marta_file = open("marta.csv", 'r')
a_list = []
a_dic = {}
total = 0
count = 0

for line in marta_file:
    line = line.split(",")
    line[3] = int(line[3])
    line[4] = int(line[4])
    a_list.append(line)
    print(line)

for my_list in a_list:
    if not my_list[3] in a_dic:
        a_dic[my_list[3]] = 0
    a_dic[my_list[3]] += 1

for i in a_dic:
    total += a_dic[i]
    count += 1

average = total / count


def calc_distance_to_average(dic):
    if a_dic[dic] < average:
        return average - a_dic[dic]
    elif a_dic[dic] > average:
        return a_dic[dic] - average
    else:
        return 0


def income(dic):
    return a_dic[dic]


closest_to_average = min(a_dic, key=calc_distance_to_average)
lowest_income = min(a_dic, key=income)

print(f"The average amount of Breeze Card taps is {average}")
print(f"The station with the closest to the average Breeze Card taps is station number {closest_to_average}")
print(f"The station with the lowest income is station number {lowest_income}")
marta_file.close()

def write_movie_info(astring,adict):
    OpenFile = open(astring,"w")

    for dic in adict:
        AList = ""

        for keys,values in adict.items():
            keys = str(keys)
            values = str(values)
            keyitem = keys+": "
            AList+=keyitem
            AList+=values
            AList = AList.replace("[","")
            AList = AList.replace("]","")
            AList = AList.replace("'","")
            OpenFile.write(AList +"\n")



movies = {"chocolat": ["Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"],
          "Skyfall": ["Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris"]}
write_movie_info("Test.txt", movies)