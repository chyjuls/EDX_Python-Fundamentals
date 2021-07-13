status = "sleepy"
if status == "bored":
    print("Let's play some video games.")
elif status == "hungry":
    print("Let's go get pizza.")
elif status == "tired":
    print("Get some rest.")

print()

number_of_cats = 5
number_of_dogs = 1

if number_of_cats >= 3 or number_of_dogs >= 3:
    print("You're a real animal lover!")
if number_of_cats >= 3 and number_of_dogs <= 3:
    print("Looks like you're a cat person!")
    print()

    x = 30
    y = 10

if x >= y:
    winner = "x"
else:
    winner = "y"

if x % y == 0:
    divisible = True
elif y % x == 0:
    divisible = True
else:
    divisible = False

if x >= 15 and y >= 15:
    result = "x and y are big numbers"
elif x >= 15:
    result = "x is a big number"
elif y >= 15:
    result = "y is a big number"
else:
    result = "no big numbers here"

print(winner, divisible, result)
print()

fave_language = "Spanish"
fave_instrument = "fiddle"
fave_drink = "iced tea"
fave_book = "Atlas Shrugged"
cool_languages = ["Afrikaans", "Finnish", "Latin", "American Sign Language"]
cool_instruments = ["didgeridoo", "pan pipes", "church organ", "fiddle"]
cool_drinks = ["civet coffee", "kombucha", "kefir"]
cool_books = ["The Catcher in the Rye", "Atlas Shrugged", "Anna Karenina", "Hamlet"]

if fave_book in cool_books:
    print("Nice book choice!")
    if fave_language in cool_languages:
        print("Let's practice together sometime!")
        if fave_instrument in cool_instruments:
            print("I play that, too!")
    else:
        print("You should learn a new language.")

    if fave_drink in cool_drinks or fave_instrument in cool_instruments:
        print("You have good taste!")
    else:
        print("What cool things are you into?")
else:
    print("See you later...")
print()

years = 0
months = 5
days = 0

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Ever been at a loss for what to do for your significant
# other for Valentine's Day? Let's right some code to generate
# a gift recommendation!
#
# The variables above give the length of the relationship in
# number of years, months, and days. Add some code below to
# print a gift recommendation based on these values:
#
# - If you've been dating for at least 4 years, give them a
#   dog ("dog").
# - If you've been dating for at least 1 year but less than
#   4 years, give them a watch ("watch").
# - If you've been dating for at least 6 months but less than
#   1 year, give them concert tickets ("concert tickets").
# - If you've been dating for at least a day but less than 6
#   months, give them candy ("candy").
# - If aren't actually dating, go big or go home: give them
#   a yacht to sail away together ("yacht").
#
# Note that no matter what, you should only print one gift.
# sample method:

if years >= 4:  # if this true we are done,
    print("dog")
elif years >= 1:  # if this is true we are done if not we move on
    print("watch")
elif months >= 6:  # if this is true we are done...but if not move to the next:
    print("concert tickets")
elif months >= 1 or days >= 1:  # got tricky here, need to use both months and days
    print("candy")
else:
    print("yacht")
print()
# long way round:
days_we_have = (years * 365) + (months * 30) + days

if days_we_have >= (4 * 365):
    print("dog")
elif 365 <= days_we_have < (4 * 365):
    print("watch")
elif 6 * 30 <= days_we_have < 365:
    print("concert tickets")
elif 1 <= days_we_have < 6 * 30:
    print("candy")
else:
    print("yacht")

print()

my_int = -3

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Check to see whether the value of my_int is even or odd, and
# whether it's positive or negative.
#
# - If it's even and positive, print "Evenly positive".
# - If it's even and negative, print "Evenly negative".
# - If it's odd and positive, print "Oddly positive".
# - If it's odd and negative, print "Oddly negative".
#
# You may assume the number will not be 0.

# Add your code here!

if my_int % 2 == 0 and my_int > 0:
    print("Evenly positive")
elif my_int % 2 == 1 and my_int > 0:
    print("Oddly positive")
elif my_int % 2 == 0 and my_int < 0:
    print("Evenly negative")
elif my_int % 2 == 1 and my_int < 0:
    print("Oddly negative")

    hour = 2
    minute = 45

    # You may modify the lines of code above, but don't move them!
    # When you Submit your code, we'll change these lines to
    # assign different values to the variables.

    # Around Georgia Tech, there are plenty of places to get a
    # late night bite to eat. However, they have different hours,
    # so when choosing where to go, you have to think about who's
    # still open!
    #
    # Imagine you're choosing between the following restaurants:
    #
    # - Barrelhouse: Closes at 11:00PM
    # - Taco Bell: Closes at 2:00AM
    # - Cookout: Closes at 3:00AM
    # - Waffle House: Never closes. Ever.
    #
    # Assume that this list is also a priority list: if Barrelhouse
    # is open, you choose Barrelhouse. If not, you choose Taco Bell
    # if it's open. If not, you choose Cookout if it's open. If
    # not, you choose Waffle House.
    #
    # However, there are two wrinkles:
    #
    # - We're using 12-hour time.
    # - hour will always represent a time from 10PM to 5AM.
    #
    # That means that if hour is 10 or 11, it's PM; if hour is
    # 12, 1, 2, 3, 4, or 5, it's AM. This will make your reasoning
    # a little more complex. You may assume that all four
    # restaurants open later than 6AM, though, so you don't have
    # to worry about opening time, just closing time.
    #
    # Add some code below that will print what restaurant you'll
    # go to based on the current values of hour and minute.

if hour == 10:
    print("BarrelHouse")
elif hour == 11 or hour == 12 or hour == 1:
    print("Taco Bell")
elif hour == 2:
    print("Cookout")
else:
    print("Waffle House")

    print()

rating = "R"
age = 15

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# The United States has a movie rating system that rates
# movies with one of five ratings: G, PG, PG-13, R, and NC-17.
# Although some of the ratings are not binding, imagine that
# you are a parent who decides on the following rules:
#
# - Any child can see a G-rated movie.
# - To see a PG-rated movie, your child must be 8 or older.
# - To see a PG-13-rated movie, your child must be 13 or older.
# - To see an R-rated movie, your child must be 17 or older.
# - Your child may never see an NC-17 movie.
#
# The variables above give a rating and a child's age. Use
# these variables to select and print one of these two
# messages based on the criteria above:
#
# - "You may see that movie!"
# - "You may not see that movie!"
#
# However, there's one trick: you may not use the 'and' operator
# anywhere in this code!


# Add your code here!


if rating == "G":
    print("You may see that movie!")
if rating == "PG":
    if age >= 8:
        print("You may see that movie!")
    else:
        print("You may not see that movie")
if rating == "PG-13":
    if age >= 13:
        print("You may see that movie!")
    else:
        print("You may not see that movie!")
if rating == "R":
    if age >= 17:
        print("You may see that movie!")
    else:
        print("You may not see that movie!")
if rating == "NC-17":
    print("You may not see that movie!")

cafe = "Starbucks"
balance = 4.32

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Atlanta is full of great coffee places. Unfortunately, great
# coffee is usually expensive. The variables above will
# contain a balance and a cafe name. Below are the prices of
# a cup of coffee at each of three locations:
#
# - Octane: $6
# - Galloway: $5
# - Starbucks: $4
# - Revelator: $3
# - Dunkin: $2
#
# Add some code above that will print one of the following
# two messages depending on whether the value of balance is
# high enough to buy a cup of coffee at the given cafe.
#
# - If it is sufficient, print "With [balance] dollars, I
#   can buy coffee at [cafe]"
# - If it is not sufficient, print "With [balance] dollars,
#   I cannot buy coffee at [cafe]"

print()
# Add your code here!

# Octane = 6
# Galloway = 5
# Starbucks = 4
# Revelator = 3
# Dunkin = 2

if cafe == "Octane":
    if balance >= 6:
        print("With {} dollars, I can buy coffee at {}".format(balance, cafe))
    else:
        print("With {} dollars, I can not buy coffee at {}".format(balance, cafe))
elif cafe == "Galloway":
    if balance >= 5:
        print("With {} dollars, I can buy coffee at {}".format(balance, cafe))
    else:
        print("With {} dollars, I can not buy coffee at {}".format(balance, cafe))
elif cafe == "Starbucks":
    if balance >= 4:
        print("With {} dollars, I can buy coffee at {}".format(balance, cafe))
    else:
        print("With {} dollars, I can not buy coffee at {}".format(balance, cafe))
elif cafe == "Revelator":
    if balance >= 3:
        print("With {} dollars, I can buy coffee at {}".format(balance, cafe))
    else:
        print("With {} dollars, I can not buy coffee at {}".format(balance, cafe))
elif cafe == "Dunkin":
    if balance >= 2:
        print("With {} dollars, I can buy coffee at {}".format(balance, cafe))
    else:
        print("With {} dollars, I can not buy coffee at {}".format(balance, cafe))
# Another shorter method:

can_afford = True

# Then, for each possible cafe, we check if we can't afford
# it. If we can't, we change can_afford to False:

if cafe == "Octane" and balance < 6:
    can_afford = False

# Notice here that we're using an additional 'if' instead of
# an elif. The reason is that if the conditional above wasn't
# True because it was the wrong cafe, then we still want to
# check the other cafes.

if cafe == "Galloway" and balance < 5:
    can_afford = False
if cafe == "Starbucks" and balance < 4:
    can_afford = False

# Notice also that we could revise this to use a bunch of 'or'
# operators, but that would lead to a loooong line of code.
# We'd rather avoid that.
if cafe == "Revelator" and balance < 3:
    can_afford = False
if cafe == "Dunkin" and balance < 2:
    can_afford = False

# Now, can_afford holds whether we can afford it or not, so
# we can just print our message depending on its value:
if can_afford:
    print("With", balance, "dollars, I can buy coffee at", cafe)
else:
    print("With", balance, "dollars, I cannot buy coffee at", cafe)
# yet another way:
# -----------------------------------------------------------
# Notice that the two possible messages we might print are
# only different by three characters: we either print 'can'
# or 'cannot'. So, why not instead make that the variable we
# change?
#
# Most of our code is the same, but notice that we've changed
# can_afford to a string instead of a boolean:

can_afford = "can"

# Our code is the same, but we change can_afford to "cannot"
# if we can't afford the coffee instead of changing it to False.

if cafe == "Octane" and balance < 6:
    can_afford = "cannot"
if cafe == "Galloway" and balance < 5:
    can_afford = "cannot"
if cafe == "Starbucks" and balance < 4:
    can_afford = "cannot"
if cafe == "Revelator" and balance < 3:
    can_afford = "cannot"
if cafe == "Dunkin" and balance < 2:
    can_afford = "cannot"

# The benefit to this is that we don't need a final conditional at
# the end of our program. Instead, we just print the final value
# of the variable can_afford:

print("With", balance, "dollars, I", can_afford, "buy coffee at", cafe)

# If we could afford it, can_afford is the string "can". If we couldn't,
# can_afford is the string "cannot". Either way, the message ends up
# correct!
