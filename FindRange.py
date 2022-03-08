# Write a function called find_range. find_range should take
# as input a string representing a filename. The file
# corresponding to that filename will be a list of integers,
# one integer per line. find_range should return a tuple
# containing the smallest and largest numbers in the file
# (the smallest first, then the largest).
#
# For example, in the dropdown in the top left you'll find a
# file named FindRangeInput.txt. The smallest number in that
# file is 2, and the largest is 37. So, if you called
# find_range("FindRangeInput.txt"), the function would return
# (2, 37), a tuple with two integers.
#
# You may assume that all lines in the file will contain a
# positive integer (greater than 0). There may be duplicates.
#
# Hint: Remember, if you loop through all the lines in a file
# then you have to close and reopen the file to read it again,
# or by use file.seek(0) to start from the top. However, you
# can do this problem without having to read the file twice.


# Write your function here!
with open("FindRangeInput.txt", "w") as find_range:
    find_range.write('''8
6
16
26
10
18
10
27
13
22
6
35
32
36
37
2
14
14
16''')

def find_range(find_range):
    min_value = 0
    max_val = 0
    range_tuple = ()
    integers = open(find_range, "r")
    numbers = {int(line) for line in integers}
    max_val = max(numbers)
    min_val = min(numbers)
    range_tuple = min_val, max_val
    return range_tuple
    integers.close()


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: (2, 37)
print(find_range("FindRangeInput.txt"))
