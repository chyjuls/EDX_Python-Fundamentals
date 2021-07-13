# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Let's try something trickier! The variables above represent
# the start time for a run as well as the length of the run
# in minutes. The original values, for example, show a run
# that started at 3:48 and lasted 172 minutes.
#
# Add some code below that will print the time at which the
# run will end, using normal formatting (e.g. 6:40 for the
# original data above). To do this, you'll need to somehow
# find both the hours and minutes of the new time, convert
# both to strings, and add those to the colon ":" to print
# the time.
#
# You may assume that the length of the run will never cross
# 12:59 (e.g. you don't have to worry about going from
# 12:59 to 1:00 or 23:59 to 0:00). You also don't need to
# worry about the lack of 0 in front of single-digit minute
# counts (e.g. it's fine to show 5:07 as 5:7).

start_hour = 3
start_minute = 48
length = 172

start_hour = start_hour * 60
time_in_minutes = start_hour + start_minute
print(time_in_minutes)
end_hour = time_in_minutes + length  # convert the end hour to hrs and mins by dividing by 60
print(end_hour)
# use the floor division operator to get hours and then get minutes using the remainder function.
hour = end_hour // 60

minutes = end_hour % 60

time_string = "{}:{}".format(hour, minutes)
print(time_string)