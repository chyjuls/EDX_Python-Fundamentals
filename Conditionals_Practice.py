mystery_int_1 = 7
mystery_int_2 = 2

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# The variables below hold two integers, mystery_int_1 and
# mystery_int_2. Complete this program below such that it
# prints "Factors!" if either of the numbers is a factor of
# the other. If neither number is a factor of the other,
# do not print anything.
#
# Hint: You can do this with just one conditional statement
# by using the logical expressions we learned earlier (and,
# or, and not). You'll also use the modulus operator we
# learned in Chapter 2.4.


# Add your code here!

if mystery_int_1 % mystery_int_2 == 0:
    print('Factors!')
elif mystery_int_2 % mystery_int_1 == 0:
    print('Factors!')
else:
    print('Not factors :(')

hunger = True
boredom = False

if hunger == True and boredom == True:
    print("Let's order pizza!")
else:
    print("Let's wait until dinnertime.")

mystery_state = "Georgia"

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# It's snowing!
#
# The variable above holds the name of the state that you're
# in (hypothetically). Complete the code below so that it
# prints the following messages depending on what state you're
# in:
#
# - "School isn't cancelled." if we're in New Jersey
# - "School is postponed." if we're in North Carolina
# - "School is cancelled!" if we're in Georgia
# - "idk wear a sweater" if we're in any other state (or if
#   the value doesn't represent a valid state).


# Add your code here!

if mystery_state == 'New Jersey':
    print("School isn't cancelled.")
elif mystery_state == 'North Carolina':
    print("School is postponed.")
elif mystery_state == 'Georgia':
    print("School is cancelled.")
else:
    print("idk wear a sweater")
    print()
    mystery_string = "zizazzle"

    # You may modify the lines of code above, but don't move them!
    # When you Submit your code, we'll change these lines to
    # assign different values to the variables.

    # The variable above creates a string. Add some code below
    # that will print based on the maximum number of consecutive
    # z's in the string:
    #
    # - If z appears three or more times in a row, print "I'm sleepy..."
    # - If z appears two times in a row, print "I love ZZ Top!"
    # - If z appears once, print "One is the loneliest number."
    # - If z does not appear, print "Who needs z anyway?"
    #
    # The message you print should correspond to the most
    # consecutive z's: in the original value of mystery_string,
    # for example, you'd print "I love ZZ Top!" because there are
    # two consecutive z's, even though there are also some
    # individual z's.
    #
    # Ignore upper-case z's -- only look for lower-case z's.
    #
    # Hint: Remember the 'in' operator! It returns true if the
    # first string is found within the second string. For example,
    # "bog" in "boggle" would return True, but "bog" in "artemis"
    # would return False.

    if 'zzz' in mystery_string:
        print("I'm sleepy...")
    elif 'zz' in mystery_string:
        print("I love ZZ Top!")
    elif 'z' in mystery_string:
        print("One is the loneliest number.")
    else:
        print("Who needs z anyway?")
    print()

    clean_shirts = ["blue", "striped", "black", "maroon"]
    weather = "raining"
    desired_shirt = "striped"
    raincoat_clean = True

    print("Can I wear my striped shirt and raincoat today?")
    if desired_shirt in clean_shirts and weather == "raining" and raincoat_clean == True:
        print("Yes!")
    else:
        print("Nope; try a different outfit.")
    print()

team_3 = "Georgia Tech"
team_3_score = 30
team_4 = "Georgia"
team_4_score = 40

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Above we've created four variables: two team names and two
# scores. A team wins if their score is greater than the other
# team's score.
#
# Add to the code below. To print a messages like these
# depending on the values:
#
# - If one team beat the other, print:
#     "[winner] beat [loser] by [margin]"
# - If neither team won, print:
#     "[team_1] played [team_2] and it was a tie"
#
# For example, with the original values in this code, you
# should print "Georgia Tech beat Georgia by 1"
#
# Hint: to make this easier, create three variables: winner,
# loser, and margin. Then, find their values before worrying
# about printing the final message.


margin = team_3_score - team_4_score
margin = abs(margin)

if team_3_score == team_4_score:
    print(team_3 + " played " + team_4 + " and it was a tie")

elif team_3_score > team_4_score:
    print(team_3 + " beat " + team_4 + " by " + str(margin))
elif team_3_score < team_4_score:
    print(team_4 + " beat " + team_3 + " by " + str(margin))

    print()

# another way...

team_1 = "Georgia Tech"
team_1_score = 28
team_2 = "Georgia"
team_2_score = 27

# What we actually print is based on the which team's score
# is greater and what the margin of victory is. So, the first
# thing we might want to do is identify who is the winner and
# who is the loser:

if team_1_score > team_2_score:
    winner = team_1
    loser = team_2
    margin = team_1_score - team_2_score
else:
    winner = team_2
    loser = team_1
    margin = team_1_score - team_2_score

# Here, we're labeling a team as the 'winner' even if the game
# was tied: we'll take care of that in the next conditional.
# Now, we want to print one message if the score was tied, and
# a different one if it wasn't:

if margin == 0:
    print(team_1, "played", team_2, "and it was a tie")
else:
    print(winner, "beat", loser, "by", margin)

# Notice we're using Python's comma syntax for print statements
# here. That's why we don't have to convert margin to an
# integer. We could also rewrite that last print statement like
# this:
steak = False
pork = True
guacamole = False
queso = False

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.
#
# Imagine you're writing code for a cash register at a
# restaurant. This restaurant serves burritoes. The base price
# of a burrito is $5. If the customer wants steak or pork, it
# adds $0.50. If they want quacamole, it adds $1.00. If they
# want queso, it adds $1.00. The customer may only select one
# meat, but they may have both queso and guacamole, neither,
# or just one.
#
# Write some code below that will print the cost of the
# burrito based on the variables above. You do not need to
# print the dollar sign or extra 0s. Remember, your final answer
# should only print out the price: comment out any debug
# statements once you have the right answer.


price = 5.00
if steak or pork:
    price += 0.50
if guacamole:
    price += 1.00
if queso:
    price += 1.00

print(price)

print()

time = 2359
tiredness_level = 90
homework_done = True
early_class = False

time = 2359
tiredness_level = 90
homework_done = True
early_class = False

if time >= 2300:

    if tiredness_level >= 85:

        if homework_done == True:

            if early_class == True:

                print("Go to sleep!")
            else:
                print("Go to sleep soon...")
        else:
            print("Finish your work, then sleep!")
    else:
        print("Stay up a little longer!")
else:
    print("It's still pretty early.")

sunny = True
windy = True

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Below, we've gone ahead and written some code that uses a
# conditional to print a message based on the variables above.
# Revise this code so that it uses nested conditionals instead
# of the 'and' operator. There should be _no_ instances of the
# 'and' reserved word in your code, but it should behave the
# same as it did originally.

if sunny:

    if not windy:
        print("Wear a hat!")

if sunny:
    if windy:
        print("Enjoy the breeze!")

print()



# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Above we've created three variables representing an attempt
# to enter a password. Add some code below that will print the
# result of this check:
#
# - "Login successful." if entered is the same as password
#   and tries is less than or equal to 3.
# - "Incorrect password." if entered is not the same as
#   password, but tries is less than or equal to 3.
# - "Tries exceeded." if tries is greater than 3.
#
# You don't need to worry about incrementing tries if the
# password is incorrect.

entered = "abc123"
password = "abc123"
tries = 3

if entered == password:
    if tries <= 3: # not needed
        print("Login successful.")
elif entered != password:
    if tries <= 3: # not needed
        print("Incorrect password.")
if tries > 3:
    print("Tries exceeded.")
    print()

# Another method
if tries > 3:
    print("Tries exceeded.")

# Now, if the user has run out of tries, the next two blocks
# will never trigger because they are 'else' blocks to the
# preceding 'if'. So, we don't need to recheck whether tries
# is greater than 3: if we've reached the next blocks, it
# isn't. So instead, we can just check whether the password
# is correct:

elif password == entered:
    print("Login successful.")
else:
    print("Incorrect password.")
    # We could also design this a little differently byusing
    # nested conditionals:

    if tries > 3:
        print("Tries exceeded.")
    else:
        if password == entered:
            print("Login successful.")
        else:
            print("Incorrect password.")
print()
todaysWeather = "cold"

if todaysWeather == "cold" and todaysWeather == "windy":
    print("jacket")
    print("scarf")
print("done")

balance = 20
purchase = 19
salesTax = 1.08
if balance >= purchase * salesTax:
    print("Purchase possible")
else:
    print("Purchase not possible")
print("done")
print()
gallons_of_milk = 2
dozens_of_eggs = 10

if gallons_of_milk and dozens_of_eggs <=6:
    print( "Time to take a trip to the store")
elif gallons_of_milk or dozens_of_eggs <=3:
    print("We need to stock up!")
else:
    print( "We have everything we need!")