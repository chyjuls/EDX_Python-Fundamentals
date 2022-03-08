import csv

with open('../resource/lib/public/georgia_tech_football.csv', 'w') as record_file:
    record_file.write('''
Date,Opponent,Location,Points For,Points Against
2016-12-31,Kentucky,Neutral,33,18
2016-11-26,Georgia,Away,28,27
2016-11-19,Virginia,Home,31,17
2016-11-12,Virginia Tech,Away,30,20
2016-11-05,North Carolina,Away,20,48
2016-10-29,Duke,Home,38,35
2016-10-15,Georgia Southern,Home,35,24
2016-10-08,Pittsburgh,Away,34,37
2016-10-01,Miami-FL,Home,21,35
2016-09-22,Clemson,Home,7,26
2016-09-17,Vanderbilt,Home,38,7
2016-09-10,Mercer,Home,35,10
2016-09-03,Boston College,Neutral,17,14''')


# Let's try out a sort of data analysis-style problem. In
# this problem, you're going to have access to a data set
# covering Georgia Tech's all-time football history. The data
# will be a CSV file, meaning that each line will be a comma-
# separated list of values. Each line will describe one game.
# The columns, from left-to-right, are:
#
# - Date: the date of the game, in Year-Month-Day format.
# - Opponent: the name of the opposing team
# - Location: Home, Away, or Neutral
# - Points For: Points scored by Georgia Tech
# - Points Against: Points scored by the opponent
#
# If Points For is greater than Points Against, then Georgia
# Tech won the game. If Points For is less than Points Against,
# then Georgia Tech lost the game. If the two are equal, then
# the game was a tie.
#
# You can see a subsection of this dataset in season2016.csv
# in the top left, but the actual dataset you'll be accessing
# here will have 1237 games.
#
# Write a function called all_time_record. all_time_record
# should take as input a string representing an opposing team
# name. It should return a string representing the all-time
# record between Georgia Tech and that opponent, in the form
# Wins-Losses-Ties. For example, Georgia Tech has beaten
# Clemson 51 times, lost 28 times, and tied 2 times. So,
# all_time_record("Clemson") would return the string "51-28-2".
#
# We have gone ahead and started the function and opened the
# file for you. The first line of the file are headers:
# Date,Opponent,Location,Points For,Points Against. After that,
# every line is a game.


def all_time_record(opponent):
    record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')

    # Add some code here! Don't forget to close the file when
    # you're done reading from it, before returning.
    # all_time_record:
    # Should take as input a string representing an opposing team
    # name. It should return a string representing the all-time
    # record between Georgia Tech and that opponent, in the form
    # Wins-Losses-Ties.

    gameDict = {}

    # loop through each line in the file
    for line in record_file:

        # Check whether the header file is equal to the string
        # content Date,Opponent,Location,Points For,Points Against.
        if line.strip() == "Date,Opponent,Location,Points For,Points Against":
            continue

        # Split the line at delimiter "," and store the values into the game_data
        game_data = line.strip().split(",")

        # Check the condition whether the name of the opponent is the
        # dictionary. If it is not present, then initialize the dictionary
        if game_data[1] not in gameDict:
            gameDict[game_data[1]] = [0, 0, 0]

        # Now, check whether the for points are greater than the against points
        # If it is, then increment the value of the dictionaries win value
        if int(game_data[3]) > int(game_data[4]):
            gameDict[game_data[1]][0] += 1

        # Now, check whether the for points are less than the against points
        # If it is, then increment the value of the dictionaries loss value
        elif int(game_data[3]) < int(game_data[4]):
            gameDict[game_data[1]][1] += 1

        # Now, check whether the for points are less than the against points
        # If it is, then increment the value of the dictionaries tie value
        else:
            gameDict[game_data[1]][2] += 1

        # Add some code here! Don't forget to close the file when
        # you're done reading from it, before returning.

    # Close the file

    record_file.close()

    # Now create the string format of the order Win-lose-tie and
    # return the string
    if opponent in gameDict:
        resultantString = str(gameDict[opponent][0]) + "-" + \
                          str(gameDict[opponent][1]) + "-" + \
                          str(gameDict[opponent][2])
    return resultantString

    # Otherwise, return false


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 51-28-2, 51-33-1, and 29-21-3, each on a separate
# line.
print(all_time_record("Clemson"))
print(all_time_record("Duke"))
print(all_time_record("North Carolina"))
print()

record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')

