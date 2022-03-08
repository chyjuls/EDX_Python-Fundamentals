## write to file

with open("heronames.txt", "w") as my_file:
    my_file.write(''' 
Captain
Night
Ancident
Moon
Spider
Invisible
Silver
Dark
Professor
Golden
Radioactive
Incredible
Impossible
Iron
Rocket
Power
Green
Super
Wonder
Metal
Doctor
Masked
Crimson
Omega
Lord
Sun
Lightning
Knight
Hulk
Centurion
Surfer
Warriors
Ghost
Hornet
Yellow Jacket
Moon
Ghost
Phantom
Machine
X
Doom
Z
Fist
Shadow
Claw
Torch
Soldier
Skull
Thunder
Hurricane
Falcon
Hawk
''')




# A common meme on social media is the name generator. These
# are usually images where they map letters, months, days,
# etc. to parts of fictional names, and then based on your
# own name, birthday, etc., you determine your own.
#
# For example, here's one such image for "What's your
# superhero name?": https://i.imgur.com/TogK8id.png
#
# Write a function called generate_name. generate_name should
# have two parameters, both strings. The first string will
# represent a filename from which to read name parts. The
# second string will represent an individual person's name,
# which will always be a first and last name separate by a
# space.
#
# The file with always contain 52 lines. The first 26 lines
# are the words that map to the letters A through Z in order
# for the person's first name, and the last 26 lines are the
# words that map to the letters A through Z in order for the
# person's last name.
#
# Your function should return the person's name according to
# the names in the file.
#
# For example, take a look at the names in heronames.txt
# (look in the drop-down in the top left). If we were to call
# generate_name("heronames.txt", "Addison Zook"), then the
# function would return "Captain Hawk": Line 1 would map to
# "A", which is the first letter of Addison's first name, and
# line 52 would map to "Z", which is the first letter of
# Addison's last name. The contents of those lines are
# "Captain" and "Hawk", so the function returns "Captain Hawk".
#
# You should assume the contents of the file will change when
# the autograder runs your code. You should NOT assume
# that every name will appear only once. You may assume that
# both the first and last name will always be capitalized.
#
# HINT: Use chr() to convert an integer to a character.
# chr(65) returns "A", chr(90) returns "Z".


# Add your code here!
def generate_name(filename, person_name):
    # Read data into a list
    first_name_map = {}
    last_name_map = {}

    # Open the file
    with open(filename) as file:
        # Read all lines
        lines = file.readlines()
        # Loop through each line
        for i in range(len(lines)):
            name = lines[i].strip()
            # Check for first name or last name
            if i < 26:
                ch = chr(i + 65)
                first_name_map[ch] = name
            else:
                ch = chr(i + 65 - 26)
                last_name_map[ch] = name

    # Now calculate the result for first name and Last name
    first_name = person_name.split(' ')[0]
    last_name = person_name.split(' ')[1]

    # Return result
    result = first_name_map[first_name[0]] + ' ' + last_name_map[last_name[0]]
    return result


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: Captain Hawk, Doctor Yellow Jacket, and Moon Moon,
# each on their own line.
print(generate_name("heronames.txt", "Addison Zook"))
print(generate_name("heronames.txt", "Uma Irwin"))
print(generate_name("heronames.txt", "David Joyner"))
