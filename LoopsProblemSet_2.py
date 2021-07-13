mystery_int = 50

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Write a for loop that prints every third number from 1 to
# mystery_int inclusive (meaning that if mystery_int is 7, it
# prints 1, 4, and 7). Print each number on a separate line.
#
# Hint: There are multiple ways to do this! You might use the
# modulus operators, or you could use the third argument for
# range().


# Add your code here!

# for i in range(1, mystery_int,  3):
# print(i)

ThirdNumber = [x for x in range(mystery_int + 1) if x % 3 == 1]
print(*ThirdNumber, sep="\n")
# Another method:
print()
for i in range(1, mystery_int + 1, 3):
    print(i)

print()

away_team = [1, 0, 0, 0, 0, 0, 0, 0, 1]
home_team = [0, 1, 0, 0, 0, 0, 2, 0]

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# A baseball game consists of 9 innings. In each inning, each
# team can score some number of runs. Whoever scores the most
# runs wins the game. Note that there are reasons why the
# number of innings might differ; extra innings for a tie game,
# fewer innings for a rain-cancelled game, etc. So, you should
# not assume there are exactly 9 full innings.
#
# The two lists above give the runs scored in each inning by
# two teams. If the away team wins, print "Away team wins!"
# If the home team wins, print "Home team wins!" You may assume
# the game will not end in a tie.
#
# Remember, you can use a loop to look at each item in a list
# with this syntax:
#
# for value in the_list:
#
# Inside that loop, the variable 'value' will take on each
# value from the list until it's seen every value. You
# don't need to know anything more about lists to solve this
# problem!
#
# Note that you must use a loop to solve this problem. If you
# use something like the sum() function, your answer will not
# be accepted.


# Add your code here! With the initial values above, it should
# print "Home team wins!"
sum = 0
sum_1 = 0
for value in away_team:
    sum += value
    Avg_sum = sum / len(away_team)

    for value_1 in home_team:
        sum_1 += value_1
        Avg_sum_1 = sum / len(home_team)

if Avg_sum_1 > Avg_sum:
    print("Home team wins!")
else:
    print("Away team wins!")
print()
print()

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Take the value of a_num and repeatedly double it until the
# result has at least 7 digits. Then, print the first 7-or-more
# digit number that results from this repeated doubling.
#
# For example, for a_num = 8:
#
# 8 -> 16 -> 32 -> 64 -> 128 -> 256 -> 512 -> 1024 -> 2048 ->
# 4096 -> 8192 -> 16384 -> 32768 -> 65536 -> 131072 -> 262144 ->
# 524288 -> 1048576
#
# So, you'd print 1048576.
#
# Hint: to check the number of digits, convert the product to a
# string, then use the len() function to check the string's length.


# Add your code here!

a_num = 15625

count = 1

while a_num < 1000000:
    double = a_num * 2
    a_num = double
    count += 1
    if len(str(double)) == 7:
        print(str(double))

print()

mystery_int = 50

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Add some code below that will find and print the sum of
# every odd number between 0 and mystery_int. This time,
# exclude the bounds (e.g. if mystery_int was 51, add the odds
# from 1 to 49, but not 51).
#
# Hint: There are multiple ways to do this!


# Add your code here!

oddsum = 0
for x in range(1, mystery_int):
    if x % 2 == 1:
        oddsum = oddsum + x
print(oddsum)

print()
odd = 0
# using the step argument
for x in range(0, mystery_int, 2):
    print(x)
    odd += x
print(odd)
print()
print()
print()

mystery_int = -7

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Use a loop to find the sum of all numbers between 0 and
# mystery_int, including bounds (meaning that if
# mystery_int = 7, you add 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7).
#
# However, there's a twist: mystery_int might be negative.
# So, if mystery_int was -4, you would -4 + -3 + -2 + -1 + 0.
#
# There are a lot of different ways you can do this. Most of
# them will involve using a conditional to decide whether to
# add or subtract 1 from mystery_int.
#
# You may use either a for loop or a while loop to solve this,
# although we recommend using a while loop.


# for i in range(0, mystery_int + 1):
# print(i)
# if mystery_int > 0:
# my_sum += i
# if mystery_int < 0:
# -= i
# print(my_sum)


sum = 0

if mystery_int < 0:
    for i in range(mystery_int, 0):
        sum += i
    print(sum)
elif mystery_int > 0:
    for i in range(0, mystery_int + 1):
        sum += i
    print(sum)

# other methods:
current_sum = 0
if mystery_int > 0:
    while mystery_int > 0:
        current_sum += mystery_int
        mystery_int -= 1
else:
    while mystery_int < 0:
        current_sum += mystery_int
        mystery_int += 1
print(current_sum)

# And here it is with a for loop. Note that it's a little
# more complex than we might have expected: we have to put
# mystery_int as the first argument if it's negative
# because Python requires ranges to go from lowest to
# highest.

current_sum = 0
if mystery_int > 0:
    for i in range(0, mystery_int + 1):
        current_sum += i
else:
    for i in range(mystery_int, 0):
        current_sum += i
print(current_sum)

# Or, we could also run the same for loop in reverse by
# putting -1 as our step:
current_sum = 0
if mystery_int > 0:
    for i in range(0, mystery_int + 1):
        current_sum += i
else:
    for i in range(0, mystery_int - 1, -1):
        current_sum += i
print(current_sum)

# However, in all these, notice we have a decent amount
# of repeated code: really, all that's changing is the sign
# on a couple of values. Can't we do this more efficiently?
# We can! Check out sample_answer_2.py to see how.

# That same logic can let us do this with a for loop,
# although it gets a little weird. First, we have to use
# the opposite values for change because we're running from
# 0 to mystery_int, not from mystery_int to 0:

if mystery_int < 0:
    change = -1
else:
    change = 1

# Then, because range() is exclusive of the second bound,
# we need to either run our loop to mystery_int + 1 if
# mystery_int is positive, or mystery_int - 1 if
# mystery_int is negative. We can do that by running it
# to mystery_int + change either way, and using change
# as our step argument, too:

current_sum = 0
for i in range(0, mystery_int + change, change):
    current_sum += i
print(current_sum)

# Finally, there's one more way we could do this, but it
# uses something we haven't covered yet. Check out
# sample_answer_4.py if you want to see!
# An even shorter solution:
current_sum = 0
while not mystery_int == 0:
    current_sum += mystery_int
    mystery_int -= mystery_int // abs(mystery_int)
print(current_sum)
print()

mystery_string = "Hello! What a fine day it is today."
mystery_character = "a"

# -----------------------------------------------------------
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


# using naive method to get count
# of each element in string

count = 0

for i in mystery_string:
    if i == mystery_character:
        count += 1
print(count)
print()

mystery_list = ["Taylor Swift", "Twenty Two", "Georgia Tech"]

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Above is a list of strings. Don't worry if this syntax is a
# little unfamiliar, we'll talk you through it and then cover
# it more in chapter 4.3.
#
# Write some code that will count the number of instances of
# the letter 't' in the list of strings. Count both capital
# 'T' and lower-case 't'. Then, print the number of instances
# of the letter 't'.
#
# For example, with the list declared above, you would print
# 6: two in the first string, three in the second, one in the
# third.
#
# Because we haven't used lists very extensively, we've
# gotten you started. The loop below will iterate through each
# string in the list. Next, you want to iterate through each
# letter in the current string, check if it's a t, and
# increment a counter if so.


# You'll want to add some code before the loop here.

count_t = 0

for string in mystery_list:

    for currentCharacter in string:
        if currentCharacter == "t" or currentCharacter == "T":
            count_t += 1
print(count_t)
print()

print()
mystery_int = 46

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Use a while loop to create a countdown from mystery_int to
# 0. Count down by 3s: if mystery_int is 46, then you should
# print 46, 43, 40, etc. Do not print any number lower than 0.
# Note that you should print both the original value of
# mystery_int and 0 if you land on it exactly.


# Add your code here!

x = 0
while x <= mystery_int:
    print(mystery_int)
    mystery_int -= 3
print()
print()

flips = "HHTTHTHHTTHHTHTHTHHTTHH"

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# The string above gives the results of a series of coin flips,
# H for heads and T for tails.
#
# Count the number of heads and number of tails. Then, print
# a message like this one based on the results:
#
# 13 heads, 10 tails. Heads wins.
#
# Replace 13 and 10 with the actual numbers of heads and tails.
# Replace 'Heads wins.' with 'Tails wins.' ift there are more
# tails, or with 'It's a tie.' if there are the same number of
# heads and tails.
#
# For example:
#
# "HHTTHH" -> 4 heads, 2 tails. Heads wins.
# "THTHTT" -> 2 heads, 4 tails. Tails wins.
# "TTHHHT" -> 3 heads, 3 tails. It's a tie.


# Add your code here!

Count_H = 0
Count_T = 0

for currentCharacter in flips:
    if currentCharacter == "H":
        Count_H += 1
    if currentCharacter == "T":
        Count_T += 1
if Count_H > Count_T:
    print("{} heads,{} tails.Heads wins.".format(Count_H, Count_T))
elif Count_H == Count_T:
    print("{} heads,{} tails.It's a tie.".format(Count_H, Count_T))
else:
    print("{} heads,{} tails.Tails wins.".format(Count_H, Count_T))

print()
print()

a_string = "F12dav^f%$25d"

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# a_string is a string of random characters. Write some code
# that adds all the digits that appear in the string and prints
# their sum.
#
# For example, the digits in the string above are 1, 2, 2, and 5,
# so your code would print 10.
#
# Remember, you can iterate over each character in a string with
# this syntax:
#
# for a_character in a_string:
#
# Remember also, you can check if a character is in a list of other
# characters within this syntax:
#
# if a_character in "ABCDEFG":
#
# If there are no digits in the string, print 0.


# Add your code here!

sum = 0
for a_character in a_string:
    if a_character.isdigit():
        sum += int(a_character)
print(sum)
print()

start_character = "A"
end_character = "Z"

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Print all the letters from start_character to end_character,
# each on their own line. Include start_character and
# end_character themselves.
#
# Remember, you can convert a letter to its underlying ASCII
# number using the ord() function. ord("A") would give 65.
# ord("Z") would give 90. You can use these values to write
# your loop.
#
# You can also convert an integer into its corresponding ASCII
# character using the chr() function. chr(65) would give "A".
# chr(90) would give "Z". So, for this problem, you'll need
# to convert back and forth between ordinal values and
# characters based on whether you're trying to loop over
# numbers or print letters.
#
# You may assume that both start_character and end_character
# are uppercase letters (although you might find it fun to
# play around and see what happens if you put other characters
# in instead!).


# Add your code here! With the original values for
# start_character and end_character, this will print the
# letters from A to Z, each on their own line.


for i in range(ord(start_character), ord(end_character) + 1):
    print(chr(i))

    print()

    beats_per_measure = 4
    measures = 5

    # You may modify the lines of code above, but don't move them!
    # When you Submit your code, we'll change these lines to
    # assign different values to the variables.

    # Recall our earlier problem where you printed out beats based
    # on measures and beats per measure (3.3.5 Coding Exercise 1).
    # In that exercise, you printing out 1 through the number of beats
    # in a measure over and over depending on the number of measures.
    #
    # Copy and modify your code, but this time, you should replace the
    # number 1 with the number of the current measure. So, the first
    # number in each measure will always rise.
    #
    # For example, instead of 1 2 3 4 1 2 3 4 1 2 3 4 (with each
    # number on its own line), you'd now print 1 2 3 4 2 2 3 4 3 2 3 4,
    # and so on.
    #
    # You can use our sample answer from that problem if you'd prefer.
    #
    # HINT: One approach would involve adding a conditional.

    # Add your code here! Using the original values of the variables
    # above, this will initially print the following numbers (but each
    # on their own line):
    # 1 2 3 4 2 2 3 4 3 2 3 4 4 2 3 4 5 2 3 4

my_first_beat = 1

for i in range(my_first_beat, measures + 1):
    print(my_first_beat)
    my_first_beat += 1
    for j in range(2, beats_per_measure + 1):
        print(j)

print()

lyrics = ["I wanna be your endgame", "I wanna be your first string",
          "I wanna be your A-Team", "I wanna be your endgame, endgame"]
lines_of_sanity = 6

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Recall the Earworm problem (3.3.5 Coding Exercise 2). The
# first time, you would still finish printing the entire list
# of lyrics after lines_of_sanity was exceeded.
#
# Revise that code so that you always stop when lines_of_sanity
# is reached. If lines_of_sanity is 6, you would print 6 lines,
# no matter how many lines are in the list. If there are fewer
# than 6 lines in the list, then you'd repeat the list until
# the number of lines is reached.
#
# For example, with the values above, you'd print:
# I wanna be your endgame
# I wanna be your first string
# I wanna be your A-Team
# I wanna be your endgame, endgame
# I wanna be your endgame
# I wanna be your first string
# MAKE IT STOP
#
# That's 6 lines: the entire list once, then the first two lines
# again to reach 6. As before, print MAKE IT STOP when you're
# done.
#
# HINT: There are multiple ways to do this: some involve a small
# change to our earlier answer, others involve a more wholesale
# rewrite. If you're stuck on one, try to think of a totally
# different way!


# Add your code here! Using the initial inputs from above, this
# should print 7 lines: all 4 lines of the list, then the first
# two lines again, then MAKE IT STOP


counter = 0
while counter <= lines_of_sanity:
    for my_lyrics in lyrics:
        counter += 1
        if counter <= lines_of_sanity:
            print(my_lyrics)
print("MAKE IT STOP")

print()
# This prints 8 lines then make it stop(earworm1:

lyrics = ["I wanna be your endgame", "I wanna be your first string",
          "I wanna be your A-Team", "I wanna be your endgame, endgame"]
lines_of_sanity = 6

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Imagine you have a song stuck in your head. Worse, you have
# only a few lines from a song stuck in your head. They just
# keep repeating over and over. The specific lines you have
# stuck in your head are stored in the variable lyrics.
#
# You can only stay sane so long while doing this.
# Specifically, you can only listen to lines_of_sanity lines
# before going crazy. Once you've reached lines_of_sanity,
# your brain will finish out the current list, then crumble.
#
# Write some code that will print the lyrics that run through
# your head. It should keep repeating each line one-by-one
# until you've reached lines_of_sanity lines. Then, it should
# keep going to finish out the current verse. After that, print
# "MAKE IT STOP" in all caps (without the quotes).
#
# HINT: Remember, we can iterate through items in a list using
# this syntax:
#
#  for item in list_of_items:
#
# HINT 2: You'll probably need a counter to count how many lines
# have been printed so far.


# Add your code here! Using the initial inputs from above, this
# should print 9 lines: all 4 lines of the list twice, followed
# by MAKE IT STOP


counter = 0
while counter < lines_of_sanity:
    for my_lyrics in lyrics:
        print(my_lyrics)
        counter += 1
print("MAKE IT STOP")
print()
# There are a lot of ways to do this, but many of them rely on things
# we haven't learned yet. So, first, let's do this using only what we've
# covered so far.
#
# We're still going to need to count the number of lines heard so far:
lines_heard = 0

# And we're still going to want to repeat until lines_heard exceeds
# lines_of_sanity:
while lines_heard < lines_of_sanity:

    # And we still want to iterate over each line in the lyrics:
    for line in lyrics:

        # The difference here is: we only want to print if lines_head
        # still doesn't exceed lines_of_sanity. It's possible that it
        # exceeded it since the last time the while loop condition was
        # checked since it could be incremented several times inside
        # this for loop.
        #
        # So, we only want to print if it's still less:

        if lines_heard < lines_of_sanity:
            lines_heard += 1
            print(line)

        # Technically, we could break here: it would stop the for loop,
        # send us back to check the while loop, and that would
        # terminate. We don't really need to, though. Without that, the
        # for loop will run a few more times, but they still won't print
        # anything.

print("MAKE IT STOP")

# There's a more elegant way to do this, though. Check out
# sample_answer_2.py to see how.

# The more elegant solution relies on being able to access individual
# elements from lyrics by number. We'll cover how to do that in chapter
# 4.3. However, here's what that will look like:
#
# First, we're just going to use lines_of_sanity as our range for our
# for loop. After all, we know exactly how many lines we need to print.

for i in range(0, lines_of_sanity):
    # Next, we want to print a line from lyrics. Which line? Well, for
    # the first four lines, we want to print the line at the index of
    # i.
    #
    # After that, though, i might exceed the length of the list. What
    # do we do then? Well, instead of just printing the item at
    # index i, we want to print the item at index i % length. That way,
    # if i is greater than the length, it 'wraps around' to the start
    # again.
    #
    # So, that would look like this:

    print(lyrics[i % len(lyrics)])

    # The brackets after parentheses let us specify which item in lyrics
    # we're printing. i % len(lyrics) finds which lyric to print right
    # now. If i is 4 and there are 4 lyrics, then it will print the first
    # one again. if i is 6 and there are 4 lyrics, it will print the
    # third one again.

print("MAKE IT STOP")
print()

mystery_int = 5

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# This is a tough one! Stick with it, you can do it!
#
# Write a program that will print the times table for the
# value given by mystery_int. The times table should print a
# two-column table of the products of every combination of
# two numbers from 1 through mystery_int. Separate consecutive
# numbers with either spaces or tabs, whichever you prefer.
#
# For example, if mystery_int is 5, this could print:
#
# 1	2	3	4	5
# 2	4	6	8	10
# 3	6	9	12	15
# 4	8	12	16	20
# 5	10	15	20	25
#
# To do this, you'll want to use two nested for loops; the
# first one will print rows, and the second will print columns
# within each row.
#
# Hint: How can you print the numbers across the row without
# starting a new line each time? With what you know now, you
# could build the string for the row, but only print it once
# you've finished the row. There are other ways, but that's
# how to do it using only what we've covered so far.
#
# Hint 2: To insert a tab into a string, use the character
# sequence "\t". For example, "1\t2" will print as "1	2".
#
# Hint 3: Need to just start a new line without printing
# anything else? Just call print() with no arguments in the
# parentheses.
#
# Hint 4: If you're stuck, try first just printing out all
# the products in one flat list, each on its own line. Once
# that's working, then worry about how to organize it into
# a table.


# Add your code here!

for i in range(1, mystery_int + 1):
    for j in range(1, mystery_int + 1):
        print("%3d  " % (i * j), end="")

    print()
print()
# Another way of creating rows and columns
for i in range(1, mystery_int + 1):
    row_string = ""
    for j in range(1, mystery_int + 1):
        product = i * j
        row_string += str(product) + "\t"
    print(row_string)

print()
mystery_string = "Lucy"

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# There's an easy way to do this exercise, and a hard way. For
# a hint on the easier way, revisit the sample answers for the
# previous coding exercise.
#
# Above we've created a variable called mystery_string. Write
# some code that will print the first letter of the string on
# the first line, the first two letters on the second line,
# the first three letters on the third line, etc., until it
# prints the entire string on the last line.
#
# For example, if the string was "Lucy", then the output would
# be:
#
# L
# Lu
# Luc
# Lucy
#
# Hint: to print without automatically starting a new line,
# include the text end="" inside the print statement's
# parentheses. For example, print("Hello", end="") will print
# the word "Hello" without starting a new line afterward. So,
# calling it twice would print "HelloHello" on one line
# instead of two lines.


# Add your code here!

output = ""
for x in mystery_string:
    output += x
    print(output)
print()
# even shorter: same problem, different approaches
for i in range(1, len(mystery_string) + 1):
    print(mystery_string[0:i])
print()

