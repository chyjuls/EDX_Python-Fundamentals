# Write a function called write_book_info. write_book_info
# will take as input two parameters: a string and a list of
# 3-tuples.
#
# The string will represent the filename to which to write.
#
# Each 3-tuple in the list will contain three strings: a
# book title, the book's author, and the book's ISBN number.
#
# write_book_info should write the list of books to the file
# given by the filename using the following format:
#
# ISBN: Title by Author
#
# So, for this list:
#
# [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"),
#  ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
#
# The file printed would look like this:
#
# 978-0-140-17739-8: Of Mice and Men by John Steinbeck
# 978-1-260-08227-2: Introduction to Computing by David Joyner
#
# We've included Sample.txt to show you what a longer version
# of one of these files might look like.


# Write your function here!
def write_book_info(book_file, books):
    my_file = open(book_file, "w")
    for book in books:
        (title, author, isbn_no) = book
        book_string = isbn_no + ": " + title + " by " + author

        my_file.writelines(str(book_string) + "\n")
    my_file.close()


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print nothing -- however, it should write the same contents
# as Sample.txt to Test.txt.
books = [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"),
         ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
write_book_info("data.txt", books)
