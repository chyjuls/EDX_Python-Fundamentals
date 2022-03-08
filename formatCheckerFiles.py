# This is a long one -- our answer is 20 lines of code, but
# yours will probably be longer. That's because it's one of the
# more authentic problems we've done so far. This is a real
# problem you'll start to face if you want to start creating
# useful programs.
#
# One of the reasons that filetypes work is that everyone
# agrees how they are structured. A ".png" file, for example,
# always contains "PNG" in the first four characters to
# assure the program that the file is actually a png. If these
# standards were not set, it would be hard to write programs
# that know how to open and read the file.
#
# Let’s define a new filetype called ".cs1301".
# In this file, every line should be structured like so:
#
# number assignment_name grade total weight
#
# In this file, each component will meet the following
# description:
#
# - number: an integer-like value of the assignment number
#
# - assignment_name: a string value of the assignment name
#
# - grade: an integer-like value of a student’s grade
#
# - total: an integer-like value of the total possible
#   number of points
#
# - weight: a float-like value ranging from 0 to 1
#   representing the percent of the student’s grade this
#   assignment is worth. All the weights should add up to 1.
#
# Each component should be separated with exactly one space.
# A good sample file is available to view as
# "sample.cs1301".
#
# Write a function called format_checker that accepts a
# filename and returns True if the file contents accurately
# conform to the described format. Otherwise the function
# should return False. In other words, it should return True
# if:
#
# - Each line has five elements separated by spaces, AND
# - The first, third, and fourth elements are integers, AND
# - The fifth element is a decimal number, AND
# - All the fifth elements add to 1.
#
# You can make changes to test.cs1301 to test your function,
# or test it with sample.cs1301. Right now, running it on
# sample.cs1301 should return True, and on test.cs1301
# should return False.
#
# Hint 1: .split() will likely help separate each line into
# its components.
# Hint 2: .split() returns a list. So, if you were to do
# something like say split_line = line.split(), then
# split_line[0] would give the first item, split_line[1] would
# give the second item, etc.
# Hint 3: If you're having trouble, try breaking it down by
# parts. First check the file to see if it has the right
# number of items per line, then whether the items are of
# the correct type, then whether the fifth elements add to
# 1. Remember, you know how to do each individual check
# (checking types, adding numbers, finding list lengths) --
# the hard part is knitting this all together into one bigger
# solution.

# saved file code  sample_1.cs1301:
with open("sample_1.cs1301", "w") as sample_1:
    sample_1.write('''1 assignment_1 85 100 0.05
2 assignment_2 80 100 0.05
3 assignment_3 95 100 0.05
4 assignment_4 95 100 0.05
5 assignment_5 80 100 0.05
6 exam_1 85 86 0.1
7 assignment_6 100 100 0.05
8 assignment_7 97 100 0.05
9 exam_2 89 100 0.1
10 assignment_8 93 100 0.05
11 assignment_9 99 100 0.05
12 exam_3 92 100 0.1
13 final_exam 95 100 0.25''')

with open("sample_2.cs1301", "w") as sample_2:
    sample_2.write('''Hey kid!
Did you know that dragons love tacos?''')


# Write your function here!

def format_checker(format):
    with open(format, "r") as my_sample_file:
        # use try/except to catch errors and overwrite them.
        try:
            adval5 = 0
            for line in my_sample_file:
                line_a = line.strip("\n")
                line_b = line_a.split(" ")  # Creates a list
                [val_1, val_2, val_3, val_4, val_5] = line_b  # unpack list to b
                adval5 += float(val_5)  # all the floats add to 1.0
                line_c = val_1 + val_3 + val_4  # convert item 1, 3 and 4 to int
                int(line_c)
            if float(adval5) == 1.0:  # check if they ad to 1.0
                return True
            else:
                return False
        except:
            return False

    my_sample_file.close()


# Test your function below. With the original values of these
# files, these should print True, then False:
print(format_checker("sample_1.cs1301"))
print(format_checker("sample_2.cs1301"))
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

# create file here:
# write to file:
with open("sample.cs1301", "w") as sample_file:
    sample_file.write('''1 assignment_1 85 100 0.25
2 test_1 90 100 0.25
3 exam_1 95 100 0.5''')


# Write your function here!

def reader(my_grade_file):
    tuple_result = []
    with open(my_grade_file, "r") as new_read_file:
        for lines in new_read_file:
            all_lines = lines.split(" ")
            tuples_list = int(all_lines[0]), all_lines[1], int(all_lines[2]), int(all_lines[3]), float(all_lines[4])
            tuple_result.append(tuples_list)
        return tuple_result


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# [(1, 'assignment_1', 85, 100, 0.25), (2, 'test_1', 90, 100, 0.25), (3, 'exam_1', 95, 100, 0.5)]
print(reader("sample.cs1301"))
print()


# Write a function called write_1301 which will write a file
# in the format described in Coding Problem 4.4.2. The
# sample.cs1301 file has been included to refresh your
# memory. Your function should accept two arguments:
# A string of a filename to write to, and a list of tuples.
# You can assume that each tuple will have the following
# format:
#
# (int, str, int, int, float)
#
# Each tuple will represent a line in the file, and each
# item in the tuple should correspond to the
# assignment number, the assignment name, the student's
# grade, the total possible number of points, and the
# assignment weight respectively.


# Write your function here!


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


# Another method>>>
def write_1301(filename, tuple_list):
    # Like the last problem, this problem can be done
    # very easily, or it can be more difficult. Don't
    # worry if it took you a while to get -- it just
    # takes practice!
    #
    # To start, we want to open the file in write
    # mode:

    file_writer = open(filename, "w")

    # Next, we want to go through each tuple in the
    # list. These tuples will each become a line in
    # the file, so we'll use 'line' as our loop
    # variable:

    for line in tuple_list:
        # line will be a tuple with five items, and
        # we want to print each one to the file
        # separated by spaces.  However, they're not
        # all strings, so we can't use
        # " ".join(tuple_list).
        #
        # Instead, we'll just do this one part at a
        # time. To make this easier to follow, let's
        # unpack the tuple first:

        number, name, grade, max_grade, weight = line

        # Now let's print each of these parts to the
        # file, separated by spaces:

        file_writer.write(str(number) + " ")
        file_writer.write(name + " ")
        file_writer.write(str(grade) + " ")
        file_writer.write(str(max_grade) + " ")
        file_writer.write(str(weight) + "\n")

    # Then, once we're all done, we close the file.

    file_writer.close()


tuple1 = (1, "exam_1", 90, 100, 0.6)
tuple2 = (2, "exam_2", 95, 100, 0.4)
tupleList = [tuple1, tuple2]
write_1301("output.cs1301", tupleList)

print()

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
# Over write previous file to get correct output:
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
