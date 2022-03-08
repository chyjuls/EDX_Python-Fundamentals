def save_user_info(username, value, password):
    username_file = open("Username.txt", "w")
    account_value_file = open("AccountValue.txt", "w")
    password_file = open("Password.txt", "w")
    username_file.write(username)
    account_value_file.write(str(value))
    password_file.write(password)
    username_file.close()
    account_value_file.close()
    password_file.close()


save_user_info("RamblinWreck20", 222, "burd311")
save_user_info("SpursFan14", str(150), "ginobili!")
save_user_info("Jolteon911", str(225), "thunderbolt")
print()


def save_user_profile(first_name, last_name, age, height, country):
    filename = last_name + first_name + ".txt"
    output_file = open(filename, "w")
    print(last_name, file=output_file)
    print(first_name, file=output_file)
    print(country, file=output_file)
    print(height, file=output_file)
    print(age, file=output_file)
    output_file.close()


save_user_profile("David", "Joyner", 30, 1.8, "USA")
save_user_profile("Maria", "Garcia", 25, 1.6, "Chile")
save_user_profile("Aditya", "Kaur", 51, 1.7, "India")
save_user_profile("Maria", "Garcia", 32, 1.7, "Chile")
print()


def save_list(my_list, my_filename):
    output_file = open(my_filename, "w")
    for item in my_list:
        output_file.write(item + "\n")
    output_file.close()


def load_list(my_filename):
    new_list = []
    input_file = open(my_filename, "r")
    for line in input_file:
        new_list.append(line)
    return new_list


print()
# Use this file created to solve the problem below:
file_name = open("input_file.txt", "w")
file_name.write("cat\n")
file_name.write("cats\n")
file_name.write("dog\n")
file_name.write("dogs\n")
file_name.write("catsup\n")
file_name.close()
print(file_name)
print()
with open("AngryFileFinderInput.txt", "w") as Angryfile:
    Angryfile.write("If exclamation points are signs of anger, then David is angry a lot!\n")
    Angryfile.write("After all, he uses way too many exclamation points when he types!\n")
    Angryfile.write("No, really! Look at any of his announcement!\n")
    Angryfile.write("Exclamation points everywhere!\n")
    Angryfile.write("!")
Angryfile.close()
print(Angryfile)


#########
# Write a function called search_inside_files. search_inside_files
# should have two parameters: a filename and a string to search for.
# search_inside_files should return a list of line numbers as integers
# where the string appeared. Note that the string at that index does
# not need to BE the search string, but rather must just contain it.
# You should assume that the first line in a file is line 1, not line
# 0.
#
# For example, if the files contents was:
# cat
# cats
# dog
# dogs
# catsup
#
# Then search_inside_files("input_file.txt", "cat") would return
# [1, 2, 5], because "cat" appears on lines 1, 2, and 5.
#
# Make sure the list you return is sorted from lowest line number to
# highest.


# Add your code here!
def search_in_files(filename, a_string):
    line_number = 0
    new_list = []
    with open(filename, "r") as get_string:
        for line in get_string:
            line_number += 1
            if a_string in line:
                new_list.append(line_number)
        return new_list


# The code below will test your function. You can find the file it
# references in the drop-down in the top left. If your code works,
# this should print:
# [1, 2, 5]
# [3, 4]
# [2, 5]
# [5]
# []
print(search_in_files("input_file.txt", "cat"))
print(search_in_files("input_file.txt", "dog"))
print(search_in_files("input_file.txt", "cats"))
print(search_in_files("input_file.txt", "sup"))
print(search_in_files("input_file.txt", "aardvark"))
print()


# Write a function called "angry_file_finder" that accepts a
# filename as a parameter. The function should open the file,
# read it, and return True if the file contains "!" on every
# line. Otherwise the function should return False.
#
# Hint: there are lots of ways to do this. We'd suggest using
# either the readline() or readlines() methods. readline()
# returns the next line in the file; readlines() returns a
# list of all the lines in the file.


# Write your function here!

def angry_file_finder(angry_file):
    new_angry_file = open(angry_file, "r")  # Open file
    contents = new_angry_file.readlines()  # read file contents
    for lines in contents:
        if not "!" in lines:  # check if "!" in lines, return true of false
            return False
    return True


print(angry_file_finder("AngryFileFinderInput.txt"))


def angry_file_finder(file_name):
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if not "!" in line:
                return False
        return True


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: True
print(angry_file_finder("AngryFileFinderInput.txt"))
print()

# Write a function called average_file. average_file should
# have one parameter: a filename.
#
# The file should have an integer on each line. average_file
# should return the average of these integers. However, if
# any of the lines of the file are _not_ integers,
# average_file should return the string "Error reading file!"
#
# Remember, by default, every time you read a line from a
# file, it's interpreted as a string.


# Add your function here!


# def average_file(filename):
# integers = 0
##num_ints = 0
# avg = 0
# with open(filename) as f:
# for line in f:
# for s in line.split():
# try:
# i = int(s)
# integers = i + integers
# num_ints = num_ints + 1
# except ValueError:
# return "Error reading file!"

# avg = integers / num_ints
# return avg


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 5.0, then Error reading file!
#
# You can select valid_file.txt and invalid_file.txt from
# the dropdown in the top left to preview their contents.
# print(average_file("valid_file.txt"))
# print(average_file("invalid_file.txt"))
print()

# Write a function called st_dev. st_dev should have one
# parameter, a filename. The file will contain one integer on
# each line. The function should return the population standard
# deviation of those numbers.
#
# The formula for population standard deviation can be found here:
# edge.edx.org/asset-v1:GTx+gt-mooc-staging1+2018_T1+type@asset+block@stdev.PNG
#
# The formula is a bit complex, though, and since this is a
# CS class and not a math class, here are the steps you would
# take to calculate it manually:
#
# 1. Find the mean of the list.
# 2. For each data point, find the difference between that
#    point and the mean. Square that difference, and add it
#    to a running sum of differences.
# 4. Divide the sum of differences by the length of the
#    list.
# 5. Take the square root of the result.
#
# You may assume for this problem that the file will contain
# only integers -- you don't need to worry about invalid
# files or lines. The easiest way to take the square root is
# to raise it to the 0.5 power (e.g. 2 ** 0.5 will give the
# square root of 2).
#
# HINT: You might find this easier if you load all of the
# numbers into a list before trying to calculate the average.
# Either way, you're going to need to loop over the numbers
# at least twice: once to calculate the mean, once to
# calculate the sum of the differences.

## File for this problem, code below:
with open("some_numbers.txt", "w") as numFile:
    numFile.write('''23
58
21
15
38
86
18
74
98
28
21
58 ''')
    numFile.close()
print(numFile)


# Add your function here!
def st_dev(num_file):
    num_list = []

    with open(num_file, "r") as numbers_file:
        for line in numbers_file:
            for num in line.split():
                num = int(num)
                num_list.append(num)
                mean = sum(num_list) / len(num_list)
                variance = sum([((num - mean) ** 2) for num in num_list]) / len(num_list)
                res = variance ** 0.5
    numbers_file.close()
    return res


print()

# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print 27.796382658340438 (or something around there).
print(st_dev("some_numbers.txt"))
print()
## Dont use this:
import statistics


def st_dev(myFile):
    with open(myFile, "r") as newFile:
        num_file = newFile.readlines()
        num_list = []
        for numbers in num_file:
            num_list.append(int(numbers))
            newFile.close()
    return statistics.pstdev(num_list)


print(st_dev("some_numbers.txt"))
print()
# code below to write a file:

with open("a_few_angles.txt", "w") as free_fall:
    free_fall.write('''10 90
10 -90
100 45
20 180''')
    free_fall.close()
print(free_fall)

# Recall Coding Problem 4.3.9 (Advanced), the free body
# diagram problem. If you were unable to solve that, we've
# included the sample answer in the dropdown in the top left
# -- feel free to use that to write your answer to this
# problem.
#
# Revise your code from that problem to use a file instead of
# a list as its parameter. Name this new function
# find_net_force_from_file. The function should take one
# parameter, the name of a file. The function should return
# the net magnitude and direction, just as it did in the other
# problem.
#
# Each line of the file will have two numbers, both integers:
# the first number will be the magnitude, and the second
# number will be the angle (in degrees, from -180 to 180).
# There will be a space between them.
#
# HINT: You may have multiple functions in your code if you
# want!
#
# HINT 2: Try to write this such that you can reuse as much
# of your earlier code as possible. Remember, when loading
# from a file, any text you load is initially a string. You'll
# almost certainly need to use the split() method.

from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt


# Add your function here!

def find_net_force_from_file(Freefall_file):
    forces = []

    with open(Freefall_file, "r") as new_fall:
        for line in new_fall:
            q = line.strip().split(" ")

            p = [int(p) for p in q]

            forces.append(p)
            h_force = sum(
                [
                    p[0] *
                    cos(radians(p[1])) for p in forces
                ]
            )
            v_force = sum(
                [
                    p[0] *
                    sin(radians(p[1])) for p in forces
                ]
            )

            r_force = round(sqrt((h_force ** 2) + (v_force ** 2)), 1)
            r_angle = round(degrees(atan2(v_force, h_force)), 1)
    new_fall.close()

    return r_force, r_angle


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: (87.0, 54.4)
print(find_net_force_from_file("a_few_angles.txt"))
print()


# Another way is to create two functions:

def find_net_force(forces):
    total_horizontal = 0
    total_vertical = 0

    for force in forces:
        magnitude, angle = force
        angle = radians(angle)
        horizontal = magnitude * cos(angle)
        vertical = magnitude * sin(angle)
        total_horizontal += horizontal
        total_vertical += vertical

    net_magnitude = sqrt(total_horizontal ** 2 + total_vertical ** 2)
    net_magnitude = round(net_magnitude, 1)

    net_angle = atan2(total_vertical, total_horizontal)
    net_angle = degrees(net_angle)
    net_angle = round(net_angle, 1)

    return net_magnitude, net_angle


# Instead of modifying it, why don't we just reuse it as is?
# Let's create a new function called find_net_force_from_file:
def find_net_force_from_file(filename):
    # And load the angles from the file exactly as we did
    # in the other sample answer:
    file = open(filename)

    forces = []
    for line in file:
        split_line = line.split()

        magnitude = int(split_line[0])
        angle = int(split_line[1])
        new_force = (magnitude, angle)

        forces.append(new_force)

    file.close()

    # Now instead of including our net force calculations in
    # this function, let's just call the other one:
    result = find_net_force(forces)

    # That result will be the same!
    return result


print(find_net_force_from_file("a_few_angles.txt"))


# Write a function called write_weird_file. write_weird_file
# should take two positional parameters. The first should be
# a filename, and the second should be a list. The function
# should also have three keyword parameters: mode, sort_first
# and reverse_first. The default value for mode should be "w",
# and the default values for both sort_first and reverse_first
# should be False.

# write_weird_file should write the contents of the list to
# the given filename. Each item from the list should be on a
# separate line. The list items could be strings, floats,
# characters, or integers. If the mode is "w", it should
# overwrite the current contents; if the mode is "a", it
# should append to the current contents. You may assume there
# will be no other value for mode.
#
# If sort_first is True, it should sort the list before
# writing. If reverse_first is True, then it should reverse
# the list before writing. If both are True, it should sort,
# then reverse.


# Add your function here!

def write_weird_file(weird_file, myList, mode="w", sort_first=False, reverse_first=False):
    with open(weird_file, mode) as new_file:
        new_list = myList
        if sort_first:
            new_list.sort()
        if reverse_first:
            new_list.reverse()
        for item in myList:
            print(item, file=new_file)
        new_file.close()
        return new_file


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print nothing. However, if you open the file called
# output.txt in the top left after running it, the contents
# of the file should be:
# Wait, where'd the other text go?
# It's gone!
# 3
# 2
# 1
write_weird_file("output.txt", ["Hmm, I bet this text will disappear.", "I wonder where it will go?"])
write_weird_file("output.txt", ["Wait, where'd the other text go?", "It's gone!"])
write_weird_file("output.txt", [2, 1, 3], mode="a", sort_first=True, reverse_first=True)
print()

# Write a function called multiply_file_by_index. This function
# should take two parameters, both strings. The first string is
# the filename of a file to which to write (output_file), and
# the second string is the filename of a file from which to read
# (input_file).
#
# In the input file, there will be an integer on every line.
# To the output file, you should write the integer from the
# original file multiplied by the line number on which it
# appeared. You should assume that the first line of the file
# is line 1 (which is different from a list, where the first item
# is at index 0).
#
# For example, if the input file contained this text:
# 1
# 4
# 3
# 7
# 6
#
# Then the output file would contain this text:
# 1
# 8
# 9
# 28
# 30

with open("input_file.txt", "w") as the_file:
    the_file.write('''1
4
3
7
6 ''')
    the_file.close()
print(the_file)


# Add your code here!
def multiply_file_by_index(output_file, input_file):
    line_number = 0
    new_num_list = []

    with open(input_file, "r") as my_input_file:
        with open(output_file, "w") as my_output_file:
            for line in my_input_file:
                line_number += 1
                for num in line.split():
                    num = int(num)
                    new_num_list.append(num)
                    result = num * line_number
                    my_output_file.write(str(result) + "\n")
    my_input_file.close()
    my_output_file.close()


# The code below will test your function. You can find the two
# files it references in the drop-down in the top left. If your
# code works, output_file.txt should have the text:
# 1
# 8
# 9
# 28
# 30
multiply_file_by_index("output_file.txt", "input_file.txt")
print("Done running! Check output_file.txt for the result.")

# If you accidentally erase input_file.txt, here's its original
# text to copy back in (remove the pound signs):
# 1
# 4
# 3
# 7
# 6
print()

with open("input_file.txt", "w") as my_name_file:
    my_name_file.write('''David Andrew Joyner
Hart, Melissa Joan
Cyrus, Billy Ray
''')
    my_name_file.close()
print(my_name_file)


# You've been sent a list of names. Unfortunately, the names
# come in two different formats:
#
# First Middle Last
# Last, First Middle
#
# You want the entire list to be the same. For this problem,
# we'll say you want the entire list to be First Middle Last.
#
# Write a function called name_fixer. name_fixer should have two
# parameters: an output filename (the first parameter) and the
# input filename (the second parameter). You may assume that every
# line will match one of the two formats above: either First Middle
# Last or Last, First Middle.
#
# name_fixer should write to the output file the names all
# structured as First Middle Last. If the name was already structured
# as First Middle Last, it should remain unchanged. If it was
# structured as Last, First Middle, then Last should be moved
# to the end after a space and the comma removed.
#
# The names should appear in the same order as the original file.
#
# For example, if the input file contained the following lines:
# David Andrew Joyner
# Hart, Melissa Joan
# Cyrus, Billy Ray
#
# ...then the output file should contain these lines:
# David Andrew Joyner
# Melissa Joan Hart
# Billy Ray Cyrus


# Add your code here!
# be very careful of indentations in PYTHON...you are in  for a shock if not!!
# use the splitlines() to remove newline characters when reading files**
def name_fixer(my_output_name, my_input_name):
    nameList_2 = []

    name_file = open(my_input_name, "r")
    new_read = name_file.read().splitlines()
    with open(my_output_name, "w") as new_namefile:

        for name in new_read:
            if "," not in name:

                nameList_2.append(name)
            else:
                name = name.replace(",", "")
                name = name.split(" ")  # split function converts string to a list
                name = name[1] + " " + name[2] + " " + name[0]
                nameList_2.append(name)
        new_names = '\n'.join(nameList_2)
        new_namefile.write(new_names)
    name_file.close()
    new_namefile.close()


# The code below will test your function. You can find the two
# files it references in the drop-down in the top left. If your
# code works, output_file.txt should have the text:
# David Andrew Joyner
# Melissa Joan Hart
# Billy Ray Cyrus
name_fixer("output_file.txt", "input_file.txt")
print("Done running! Check output_file.txt for the result.")

# If you accidentally erase input_file.txt, here's its original
# text to copy back in (remove the pound signs):
# David Andrew Joyner
# Hart, Melissa Joan
# Cyrus, Billy Ray

print()


# You've been sent a list of names. Unfortunately, the names
# come in two different formats:
#
# First Middle Last
# Last, First Middle
#
# You want the entire list to be the same. For this problem,
# we'll say you want the entire list to be Last, First Middle.
#
# Write a function called name_refixer. name_refixer should have two
# parameters: an output filename (the first parameter) and the
# input filename (the second parameter). You may assume that every
# line will match one of the two formats above: either First Middle
# Last or Last, First Middle.
#
# name_refixer should write to the output file the names all
# structured as Last, First Middle. If the name was already structured
# as Last, First Middle, it should remain unchanged. If it was
# structured as First Middle Last, then Last should be moved
# to the front and a comma should be added after it.
#
# The names should appear in the same order as the original file.
#
# For example, if the input file contained the following lines:
# David Andrew Joyner
# Hart, Melissa Joan
# Cyrus, Billy Ray
#
# ...then the output file should contain these lines:
# Joyner, David Andrew
# Hart, Melissa Joan
# Cyrus, Billy Ray


# Add your code here!
def name_refixer(output_filename, input_filename):
    list_2 = []
    names_file = open(input_filename, "r")
    input_file = names_file.read().splitlines()
    with open(output_filename, "w") as output_file:
        for names in input_file:
            if "," not in names:
                my_name = names
                my_name = my_name + ","
                my_name = my_name.split()
                my_name.insert(0, my_name[2])
                # print(my_name)
                my_name.pop()
                # print(my_name)
                new_name = " "
                my_name = new_name.join(my_name)
                list_2.append(my_name)
            elif "," in names:
                list_2.append(names)
        list_3 = "\n".join(list_2)
        output_file.write(list_3)
    names_file.close()
    output_file.close()


# The code below will test your function. You can find the two
# files it references in the drop-down in the top left. If your
# code works, output_file.txt should have the text:
# Joyner, David Andrew
# Hart, Melissa Joan
# Cyrus, Billy Ray
name_refixer("output_file.txt", "input_file.txt")
print("Done running! Check output_file.txt for the result.")
print()

#code to create the file for problem below:

with open("top500.txt", "w") as code_file:
    code_file.writelines('''Doctor Strange	232641920
Terminator Salvation	125322469
Ant-Man	180202163
The Fugitive	183875760
The Break-Up	118703275
The Twilight Saga: Eclipse	300531751
Chicken Little	135386665
The Divergent Series: Insurgent	130179072
Thor	181030624
Lilo & Stitch	145794338
Armageddon	201578182
The Simpsons Movie	183135014
Beauty and the Beast (2017)	170000000
Oz The Great and Powerful	234911825
Bad Boys II	138608444
The Lord of the Rings: The Fellowship of the Ring	315544750
The Da Vinci Code	217536138
Jaws	260000000
The Karate Kid	176591618
Rango	123477607
The SpongeBob Movie: Sponge Out of Water	162994032
Honey, I Shrunk the Kids	130724172
Fast and Furious	155064265
Mr. & Mrs. Smith	186336279
I Now Pronounce You Chuck and Larry	120059556
Shark Tale	160861908
Fast Five	209837675
Kingsman: The Secret Service	128261724
The Day After Tomorrow	186740799
X-Men: Apocalypse	155442489
Hannibal	165092268
Safe House	126373434
Van Helsing	120177084
The Conjuring	137400141
Sleepless in Seattle	126680884
WALL-E	223808164
Raiders of the Lost Ark	248159971
Deep Impact	140464664
The Curious Case of Benjamin Button	127509326
Dumb and Dumber	127175374
Fast & Furious 6	238679850
Night at the Museum: Battle of the Smithsonian	177243721
Logan	184026885
Tron Legacy	172062763
American Hustle	150117807
The Vow	125014030
The Rock	134069511
Speed	121248145
I, Robot	144801023
The Flintstones	130531208
The Fault in our Stars	124872350
Mulan	120620254
Harry Potter and the Goblet of Fire	290013036
National Treasure	173008894
The Lost World: Jurassic Park	229086679
Marvel's The Avengers	623357910
Beauty and the Beast	218967620
Meet the Fockers	279261160
Ghost	217631306
Captain America: Civil War	408084349
Signs	227966634
Cheaper by the Dozen	138614544
Identity Thief	134506920
Hidden Figures	165559069
The Mask	119938730
21 Jump Street	138447667
The Empire Strikes Back	290475067
Ratatouille	206445654
Ocean's Eleven	183417150
Tomorrow Never Dies	125304276
The Chronicles of Narnia: The Lion, the Witch and the Wardrobe	291710957
Slumdog Millionaire	141319928
On Golden Pond	119285432
Cinderella (2015)	201151353
Over the Hedge	155019340
The Great Gatsby (2013)	144840419
The Dark Knight Rises	448139099
2 Fast 2 Furious	127154901
Quantum of Solace	168368427
Star Wars: The Force Awakens	936662225
Lethal Weapon 3	144731527
Shrek 2	441226247
The Sting	156000000
The Good Dinosaur	123087120
Ghostbusters	242212467
Superman Returns	200081192
Maleficent	241410378
Fatal Attraction	156645693
Harry Potter and the Deathly Hallows Part 2	381011219
Erin Brockovich	125595205
The Croods	187168425
Grown Ups 2	133668525
What Lies Beneath	155464351
The Matrix Revolutions	139313948
The LEGO Batman Movie	167423352
I Am Legend	256393010
Fantastic Four (2005)	154696080
Toy Story 2	245852179
Indiana Jones and the Temple of Doom	179870271
Saving Private Ryan	216540909
The Hunger Games: Mockingjay - Part 2	281723902
Juno	143495265
Men in Black	250690539
Puss in Boots	149260504
The Longest Yard	158119460
A Christmas Carol (2009)	137855863
Neighbors	150157400
Fahrenheit 9/11	119194771
National Lampoon's Animal House	141600000
Transformers: Age of Extinction	245439076
Dr. Seuss' Horton Hears a Who!	154529439
Hairspray (2007)	118871849
There's Something About Mary	176484651
The Bourne Supremacy	176241941
The Waterboy	161491646
The Dark Knight	534858444
My Best Friend's Wedding	127120029
Gran Torino	148095302
300	210614939
Pearl Harbor	198542554
Wreck-It Ralph	189422889
Troy	133378256
Spider-Man 2	373585825
Night at the Museum	250863268
Transformers	319246193
Rogue One: A Star Wars Story	530748532
Hancock	227946274
Fantastic Four: Rise of the Silver Surfer	131921738
Skyfall	304360277
Marley and Me	143153751
The Santa Clause	144833357
Terminator 2: Judgment Day	204843345
Coming to America	128152301
Silver Linings Playbook	132092958
X-Men	157299717
The Hunger Games: Catching Fire	424668047
The Blair Witch Project	140539099
Furious 7	353007020
The Godfather	134966411
The Silence of the Lambs	130742922
The Truman Show	125618201
The Hangover Part II	254464305
We're the Millers	150394119
Jurassic Park	402453882
Die Another Day	160942139
Toy Story 3	415004880
My Big Fat Greek Wedding	241438208
Megamind	148415853
Dinosaur	137748063
Gravity	274092705
Get Out	133117620
The Hangover	277322503
Home Alone 2: Lost in New York	173585516
Batman Returns	162831698
Home (2015)	177397510
Little Fockers	148438600
Mission: Impossible III	134029801
Austin Powers in Goldmember	213307889
Blades of Glory	118594548
Star Wars: Episode III - Revenge of the Sith	380270577
How to Train Your Dragon	217581231
Avatar	760507625
G.I. Joe: The Rise of Cobra	150201498
Star Wars: Episode II - Attack of the Clones	310676740
50 First Dates	120908074
Three Men and a Baby	167780960
Who Framed Roger Rabbit	156452370
Shrek	267665011
Patch Adams	135026902
Crouching Tiger, Hidden Dragon	128078872
Cars 2	191452396
Despicable Me 2	368061265
Sully	125070033
Titanic	658672302
X-Men: The Last Stand	234362462
Central Intelligence	127440871
Happy Feet	198000317
The Hunt for Red October	122012643
Charlie and the Chocolate Factory	206459076
How the Grinch Stole Christmas	260044825
Pirates of the Caribbean: At World's End	309420425
Dances with Wolves	184208848
Elf	173398518
Harry Potter and the Sorcerer's Stone	317575550
Mission: Impossible II	215409889
Stuart Little	140035367
King Kong	218080025
American Beauty	130096601
Ted	218815487
Jurassic Park III	181171875
Super 8	127004179
X-Men Origins: Wolverine	179883157
Avengers: Age of Ultron	459005868
The Last Airbender	131772187
The Proposal	163958031
Superbad	121463226
La La Land	149764184
Life of Pi	124987023
Captain America: The First Avenger	176654505
Sing	269347740
Apollo 13	173837933
A Beautiful Mind	170742341
Split	136870965
Lethal Weapon 2	147253986
Lone Survivor	125095601
The King's Speech	138797449
Ice Age: Dawn of the Dinosaurs	196573705
Twister	241721524
Mission: Impossible - Ghost Protocol	209397903
Rush Hour 2	226164286
Spider-Man	403706375
An Officer and a Gentleman	129795554
Liar Liar	181410615
American Gangster	130164645
Anger Management	135645823
The Twilight Saga: New Moon	296623634
The Help	169708112
Doctor Dolittle	144156605
The Twilight Saga: Breaking Dawn Part 1	281287133
Star Trek	257730019
Prometheus	126477084
Batman Forever	184031112
Taken 2	139854287
Inside Out	356461711
Shrek the Third	322719944
The Green Mile	136801374
Jurassic World	652270625
Cloudy with a Chance of Meatballs 2	119793567
Tootsie	177200000
The Hobbit: The Battle of the Five Armies	255119788
Transformers: Revenge of the Fallen	402111870
Into the Woods	128002372
Tarzan	171091819
Good Morning, Vietnam	123922370
G.I. Joe: Retaliation	122523060
The Smurfs	142614158
Wedding Crashers	209255921
Lucy	126663600
Madagascar 3: Europe's Most Wanted	216391482
Four Christmases	120146040
Chicago	170687518
Get Smart	130319208
Aladdin	217350219
Pitch Perfect 2	184296230
Minority Report	132072926
Spectre	200074609
The Peanuts Movie	130178411
The Polar Express	185618322
Hulk	132177234
The Perfect Storm	182618434
The Revenant	183637894
The Nutty Professor II: The Klumps	123309890
Alice in Wonderland (2010)	334191110
Spider-Man 3	336530303
Moana	248060698
Indiana Jones and the Kingdom of the Crystal Skull	317101119
The Mummy Returns	202019785
National Treasure: Book of Secrets	219964115
The Pursuit of Happyness	163566459
World War Z	202359711
Jason Bourne	162434410
The Fast and the Furious	144533925
The Legend of Tarzan	126643061
Clear and Present Danger	122187717
True Grit	171243005
Seabiscuit	120277854
The Lord of the Rings: The Return of the King	377845905
Walk the Line	119519402
Live Free or Die Hard	134529403
Tangled	200821936
101 Dalmatians (1996)	136189294
Planet of the Apes (2001)	180011740
Gone Girl	167767189
Casino Royale	167445960
Monsters University	268492764
Ransom	136492681
Trolls	153649648
Man of Steel	291045518
Sherlock Holmes: A Game of Shadows	186848418
Return of the Jedi	309306177
The Devil Wears Prada	124740460
X-Men: Days of Future Past	233921534
The Hobbit: An Unexpected Journey	303003568
As Good as It Gets	148478011
The Martian	228433663
Sweet Home Alabama	127223418
Bee Movie	126631277
The Twilight Saga: Breaking Dawn Part 2	292324737
Catch Me If You Can	164615351
Mr. Deeds	126293452
Cars	244082982
Alvin and the Chipmunks	217326974
The Amazing Spider-Man	262030663
Teenage Mutant Ninja Turtles (2014)	191204754
Shrek Forever After	238736787
Rambo: First Blood Part II	150415432
Batman	251188924
The Exorcist	232906145
Lemony Snicket's A Series of Unfortunate Events	118634549
Kung Fu Panda 2	165249063
Big Hero 6	222527828
American Sniper	350126372
Fifty Shades of Grey	166167230
Sister Act	139605150
Star Wars: Episode I - The Phantom Menace	474544677
The Secret Life of Pets	368384330
Star Trek Beyond	158848340
Pocahontas	141579773
Ice Age: The Meltdown	195330621
The Blind Side	255959475
Back to the Future	210609762
The Incredible Hulk	134806913
Frozen	400738009
The Mummy	155385488
Blazing Saddles	119601481
Brave	237283207
Gremlins	153083102
Pirates of the Caribbean: The Curse of the Black Pearl	305413918
Finding Dory	486295561
Smokey and the Bandit	126737428
Bruce Almighty	242829261
Captain America: The Winter Soldier	259766572
Indiana Jones and the Last Crusade	197171806
Mrs. Doubtfire	219195243
E.T.: The Extra-Terrestrial	435110554
Madagascar: Escape 2 Africa	180010950
Robots	128200012
The Passion of the Christ	370782930
The Matrix	171479930
Beverly Hills Cop II	153665036
Rocky III	125049125
Despicable Me	251513985
Rush Hour	141186864
2012	166112167
Rain Man	172825435
Rio	143619809
Wayne's World	121697323
Star Wars	460998007
Enchanted	127807262
Look Who's Talking	140088813
The LEGO Movie	257760692
Independence Day	306169268
Deadpool	363070709
Iron Man	318412101
Runaway Bride	152257509
Borat: Cultural Learnings of America for Make Benefit Glorious Nation of Kazakhstan	128505958
Rush Hour 3	140125968
XXX	142109382
Cast Away	233632142
Mamma Mia!	144130063
The Sound of Music	158671368
Gone with the Wind	198676459
Snow White and the Huntsman	155332381
The Chronicles of Narnia: Prince Caspian	141621490
Divergent	150947895
Sherlock Holmes	209028679
Ocean's Twelve	125544280
The Amazing Spider-Man 2	202853933
Inception	292576195
Kung Fu Panda	215434591
Wild Hogs	168273550
Twilight	192769854
Jerry Maguire	153952592
Lincoln	182207973
How to Train Your Dragon 2	177002924
Hotel Transylvania	148313048
Charlie's Angels	125305545
Finding Nemo	380843261
War of the Worlds	234280354
101 Dalmatians	144880014
22 Jump Street	191719337
Hook	119654823
Dawn of the Planet of the Apes	208545589
Platoon	138530565
The Bourne Identity	121661683
Alvin and the Chipmunks: The Squeakquel	219614612
City Slickers	124033791
Robin Hood: Prince of Thieves	165493908
Minions	336045770
The Jungle Book	141843612
True Lies	146282411
The Bourne Ultimatum	227471070
The Ring	129128133
Traffic	124115725
X2: X-Men United	214949694
Rocky IV	127873716
Iron Man 3	409013994
Straight Outta Compton	161197785
Batman Begins	206852432
The Wolverine	132556852
Scary Movie	157019771
Ride Along	134938200
Harry Potter and the Deathly Hallows Part 1	295983305
Grease	188755690
Harry Potter and the Half-Blood Prince	301959197
Les Miserables (2012)	148809770
Forrest Gump	330252182
The World Is Not Enough	126943684
Alvin and the Chipmunks: Chipwrecked	133110742
Paul Blart: Mall Cop	146336178
The Nutty Professor (1996)	128814019
X-Men: First Class	146408305
Click	137355633
Argo	136025503
Austin Powers: The Spy Who Shagged Me	206040086
Teenage Mutant Ninja Turtles	135265915
Transformers: Dark of the Moon	352390543
Hitch	179495555
Ghostbusters (2016)	128350574
Harry Potter and the Chamber of Secrets	261988482
Wanted	134508551
The Matrix Reloaded	281576461
The Lion King	422783777
The Bodyguard	122006740
Hotel Transylvania 2	169700110
Django Unchained	162805434
Inglourious Basterds	120540719
Angels & Demons	133375846
Iron Man 2	312433331
Star Trek Into Darkness	228778661
Mad Max: Fury Road	154058340
Pirates of the Caribbean: Dead Man's Chest	423315812
Madagascar	193595521
Harry Potter and the Order of the Phoenix	292004738
A Few Good Men	141340178
Pretty Woman	178406268
Rise of the Planet of the Apes	176760185
The Incredibles	261441092
Gladiator	187705427
Lethal Weapon 4	130444603
Zootopia	341268248
Mission: Impossible	180981856
Mission: Impossible - Rogue Nation	195042377
The Lord of the Rings: The Two Towers	342551365
The Heat	159582188
Dr. Seuss' The Lorax	214030500
Fantastic Beasts and Where To Find Them	233868941
Superman	134218018
Air Force One	172956409
Cloudy with a Chance of Meatballs	124870275
Home Alone	285761243
Bridesmaids	169106725
Taken	145000989
Terminator 3: Rise of the Machines	150371112
American Pie 2	145103595
MIB 3	179020854
Pirates of the Caribbean: On Stranger Tides	241071802
The Birdcage	124060553
The Firm	158348367
Anchorman 2: The Legend Continues	127352707
Talladega Nights: The Ballad of Ricky Bobby	148213377
Monsters Vs. Aliens	198351526
Ice Age: Continental Drift	161321843
Clash of the Titans (2010)	163214888
Harry Potter and the Prisoner of Azkaban	249541069
Suicide Squad	325100054
Good Will Hunting	138433435
The Sixth Sense	293506292
Top Gun	179800601
Total Recall	119412921
The Hunger Games	408010692
Godzilla	136314294
Close Encounters of the Third Kind	132088635
The Jungle Book (2016)	364001123
Interstellar	188020017
San Andreas	155190832
Beverly Hills Cop	234760478
Daddy's Home	150357137
The Hobbit: The Desolation of Smaug	258366855
The Sum of All Fears	118907036
Men in Black II	190418803
Big Daddy	163479795
Knocked Up	148768917
Thor: The Dark World	206362140
Up	293004164
Rio 2	131538435
The Departed	132384315
Toy Story	191796233
Grown Ups	162001186
The Santa Clause 2	139236327
The Other Guys	119219978
Kung Fu Panda 3	143528619
Ice Age	176387405
Bringing Down the House	132716677
Batman v Superman: Dawn of Justice	330360194
Guardians of the Galaxy	333176600
Something's Gotta Give	124728738
The Hunger Games: Mockingjay - Part 1	337135885
Godzilla (2014)	200676069
Snow White and the Seven Dwarfs	184925486
Scooby-Doo	153294164
Meet the Parents	166244045
Shutter Island	128012934
G-Force	119436770
What Women Want	182811707
A Bug's Life	162798565
Monsters, Inc.	289916256
Lara Croft: Tomb Raider	131168070
Crocodile Dundee	174803506
Sex and the City	152647258''')


# We've given you a file called "top500.txt" which contains
# the name and lifetime gross revenue of the top 500
# films at the time this question was written.
#
# Each line of the given file is formatted like so:
# <name>\t<gross revenue in dollars>
#
# In other words, you should call .split("\t") to split
# the line into the movie name (the first item) and the
# gross (the second item).
#
# Unfortunately, these movies are not in order. Write a
# function called "sort_films" that accepts two parameters:
# a string of a source filename and a string of a
# destination filename. Your function should open the
# source file and sort the contents from greatest gross
# revenue to least gross revenue, and write the sorted
# contents to the destination filename. You may assume the
# source file is correctly formatted.
#
# Hint: one common issue on this problem is that every line
# in the input file ends with a line break except the last
# one. If the autograder gives you an index error, open
# top500result.txt and make sure there are 500 lines in your
# output file!
def sort_films(input_movie, output_movie):
    revenue_list = []
    top_grossing = " "
    movie_list = open(input_movie, "r")
    movie_outputlist = open(output_movie, "w")
    for movies in movie_list:
        movies = movies.split("\t")
        top_movies = [movies[0], movies[1].strip()]
        top_movies.reverse()
        revenue_list.append(top_movies)

    revenue_list.sort()
    revenue_list.reverse()
    for movie in revenue_list:
        print(str(movie[1]) + "\t" + str(movie[0]), file=movie_outputlist)
    movie_list.close()
    movie_outputlist.close()


# The line of code below will test your function and put
# your results in top500result.txt. Then, it will print
# "Done!"
sort_films("top500.txt", "top500result.txt")
print("Done!")

#### Fles to use here:
with open("sample.cs1301", "w") as sample_file:
    sample_file.write('''1 assignment_1 85 100 0.25
2 test_1 90 100 0.25
3 exam_1 95 100 0.5''')


####
def write_1301(filename, tupleList):
    outputFile = open(filename, "w")
    b = []
    for item in tupleList:
        for val in item:
            b.append(val)
        print(b[0], b[1], b[2], b[3], b[4], file=outputFile)
        b = []

    outputFile.close()


# The code below will test your function. It's not used
# for grading, so feel free to modify it! You may check
# output.cs1301 to see how it worked.
tuple1 = (1, "exam_1", 90, 100, 0.6)
tuple2 = (2, "exam_2", 95, 100, 0.4)
tupleList = [tuple1, tuple2]
write_1301("output.cs1301", tupleList)

print()


# Write a function called "reader" that reads in a ".cs1301"
# file described in the previous problem. The function should
# return a list of tuples representing the lines in the file like so:
#
# [(line_1_number, line_1_assignment_name, line_1_grade, line_1_total, line_1_weight),
# (line_2_number, line_2_assignment_name, line_2_grade, line_2_total, line_2_weight)]
#
# All items should be of type int except for the name (string)
# and the weight (float). You can assume the file will be in the
# proper format -- in a real program, you would use your code
# from the previous problem to check for formatting before
# trying to call the function below.
#
# Hint: Although you could use readlines() to read in all
# the lines at once, they would all be strings, not a list.
# You still need to go line-by-line and convert each string
# to a list.


# Write your function here!

def reader(my_grade_file):
    tuple_result = []
    with open(my_grade_file, "r") as new_read_file:
        for lines in new_read_file:
            all_lines = lines.split(" ")
            tuples_list = int(all_lines[0]), all_lines[1], int(all_lines[2]), int(all_lines[3]), float(all_lines[4])
            tuple_result.append(tuples_list)
        return tuple_result
    new_read_file.close()


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# [(1, 'assignment_1', 85, 100, 0.25), (2, 'test_1', 90, 100, 0.25), (3, 'exam_1', 95, 100, 0.5)]
print(reader("sample.cs1301"))

print()

with open("sample.cs1301", "w") as gradeFile:
    gradeFile.write('''1 assignment_1 85 100 0.05
2 assignment_2 80 100 0.05
3 assignment_3 95 100 0.05
4 assignment_4 95 100 0.05
5 assignment_5 80 100 0.05
6 exam_1 85 100 0.1
7 assignment_6 100 100 0.05
8 assignment_7 97 100 0.05
9 exam_2 89 100 0.1
10 assignment_8 93 100 0.05
11 assignment_9 99 100 0.05
12 exam_3 92 100 0.1
13 final_exam 95 100 0.25''')


# Write a function called get_grade that will read a
# given .cs1301 file and return the student's grade.
# To do this, we would recommend you first pass the
# filename to your previously-written reader() function,
# then use the list that it returns to do your
# calculations. You may assume the file is well-formed.
#
# A student's grade should be 100 times the sum of each
# individual assignment's grade divided by its total,
# multiplied by its weight. So, if the .cs1301 just had
# these two lines:
#
# 1 exam_1 80 100 0.6
# 2 exam_2 30 50 0.4
#
# Then the result would be 72:
#
# (80 / 100) * 0.6 + (30 / 50) * 0.4 = 0.72 * 100 = 72


# Write your function here!
def reader(my_grade_file):
    tuple_result = []
    with open(my_grade_file, "r") as new_read_file:
        for lines in new_read_file:
            all_lines = lines.split(" ")
            tuples_list = int(all_lines[0]), all_lines[1], int(all_lines[2]), int(all_lines[3]), float(all_lines[4])
            tuple_result.append(tuples_list)
        return tuple_result
    new_read_file.close()


def get_grade(grade_file):
    sum_grades = 0

    grades_list = reader(grade_file)
    for item in grades_list:
        calc_sum = int(item[2]) / int(item[3]) * float(item[4])
        sum_grades += calc_sum
    return sum_grades * 100
    grades_list.close()


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 91.55
print(get_grade("sample.cs1301"))
print()
