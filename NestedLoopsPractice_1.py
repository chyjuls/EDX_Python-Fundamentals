beats_per_measure = 4
measures = 5

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# In music, a song's time signature is given in terms of beats
# per measure. A common time signature is 4 beats per measure:
# for every measure of music, a conductor might count from 1
# to 4 with the tempo of the music.
#
# A song then has a number of measures. For example, a short
# song might have only 5 measures. In which case, a conductor
# would count from 1 to 4 five times. If the time signature had
# instead been 3 beats per measure, she would could from 1 to 3
# five times instead.
#
# Write a nested for loop that will print out the beats of the
# piece of music. For example, if the song had 4 beats per
# measure and only 2 measures, this would print out:
#
# 1
# 2
# 3
# 4
# 1
# 2
# 3
# 4
#
# We print from 1 to 4 before starting over because there are
# 4 beats per measure, and we print them all twice because there
# are two measures.


# Add your code here! Using the original values of the variables
# above, this will initially print 1 through 4 five times for a
# total of 20 lines.


for i in range(measures):
    for j in range(beats_per_measure):
        j += 1
        print(j)
print()

# for adding to every first beat:

for measure in range(0, measures):
    for beat in range(1, beats_per_measure + 1):

        # Previously, we always printed the current value
        # of beat. However, we no longer always want to
        # do that, so we'll comment out what was here:
        # print(beat)

        # What we print depends on the value of beat. If
        # beat is 1, then we want to print the current
        # value of measure. However, we started the measure
        # range at 0, so we want to add one to it before
        # printing it:
        if beat == 1:
            print(measure + 1)

        # If beat wasn't 1, then we print beat as usual:
        else:
            print(beat)
print()

for i in range(1, 6):
    j = 0
    while j < i:
        print(j, end=" ")
        j += 1
    print("")

for i in range(1, 6):
    for j in range(0, i):
        print(j, end=" ")
    print("")

    print()

num = [12, 23, 34, 45, 56, 67, 78]
sum = 0
for i in range(0, len(num)):
    current_num = num[i]
    sum += current_num

print(sum / len(num))
print()

for i in range(1, 4):
    print(i, end=", ")
    i += 1
    print(i, end=",")
    print()
print()

num_spaces = 0
ListOfStrings = ["This is the first string", "This is the second string"]
for current_string in ListOfStrings:
    for currentCharacter in current_string:
        if currentCharacter == " ":
            num_spaces += 1

## num_words = num_spaces + len(ListOfStrings) # is this really needed to count number of characters or
# spaces...
print(num_spaces)

for i in "hey":
    print("Looped!")
print()

for x in range(3):
    print("Looped!")
print()

for a in [10, 9, 8]:
    print("Looped!")
print()

for num in range(10, 1, -3):
    print("Looped!")

mystery_string = "my cat your cat"

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Add some code below that will count and print how many
# times the character sequence "cat" appears in mystery_string.
# For example, for the string above, it would print 2.
#
# This one is tricky! Think carefully about for-each loops,
# conditionals, and booleans. How can you track what character
# you're currently looking for? We expect you'll use a loop
# and a single big conditional, but there are other approaches
# as well. Try to stick with the topics we've covered so far.


# Add your code here!


# print(mystery_string.find("cat"))


word = "cat"
count = 0
for i in range(len(mystery_string)+1):
    if mystery_string[i:i+len(word)] == word:
        count += 1
print(count)
print()
# A tedious way to  do this:
mystery_string = "my cat your cat"

# Later on, we'll cover lots of other ways to do this, using
# more sophisticated approaches to using substrings and other
# concepts. We can still do this using just what we know now,
# though!
#
# First, we know we need a counter since the problem says to
# count something:

count = 0

# Next, we need to keep track of what letter we're currently
# searching for. The first letter in "cat" is "c", so by
# default, we'll set this to "c":
current_search_letter = "c"

# Then, we loop over all the letters in the string:
for letter in mystery_string:

    # For each letter, we want to see if it's the letter
    # we're looking for.
    #
    # If it's a 'c' and we're looking for 'c', great! Now
    # we're looking for 'a':
    if letter == "c":
        current_search_letter = "a"

    # If it's an 'a' and we're looking for 'a', great! Now
    # we're looking for 't':
    elif letter == "a" and current_search_letter == "a":
        current_search_letter = "t"

    # If it's a 't' and we're looking for 't', then we've
    # found the word 'cat'! So, we add one to the counter,
    # and start over looking for 'c' again:
    elif letter == "t" and current_search_letter == "t":
        count += 1
        current_search_letter = "c"

    # Here's the trick: if we find any letter other than the
    # one we were looking for, then we need to start over!
    # If we've found "ca" but the next letter is "b", then
    # it doesn't matter if the one after it is "t": "cabt"
    # isn't the same as "cat":
    else:
        current_search_letter = "c"
print(count)
