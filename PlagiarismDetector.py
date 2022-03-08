# write files

with open("file_1.txt", "w") as my_file1:
    my_file1.write("i took a walk around the world to ease my troubled mind i left my body lying somewhere in the "
                   "sands of time i watched the world float to the dark side of the moon i feel there is nothing i "
                   "can do yeah i watched the world float to the dark side of the moon after all i knew it had to be "
                   "something to do with you i really dont mind what happens now and then as long as youll be my "
                   "friend at the end if i go crazy then will you still call me superman if im alive and well will "
                   "you be there holding my hand ill keep you by my side with my superhuman might kryptonite")
with open("file_2.txt", "w") as my_file2:
    my_file2.write("i dont care if i go crazy then one two three four five switch crazy go i if care dont i five four "
                   "three two one and switch")

with open("file_3.txt", "w")as my_file3:
    my_file3.write("when i was young i took a walk around the woods i found that i was both taller and smaller than "
                   "the trees returning to my home i set out for the desert i journeyed for long days and nights my "
                   "spirit left my body and i left my body lying somewhere in the sands of time unburdened by "
                   "physical form i watched the world float away from me and into the vast moonlight")





# A common problem in academic settings is plagiarism
# detection. Fortunately, software can make this pretty easy!
#
# In this problem, you'll be given two files with text in
# them. Write a function called check_plagiarism with two
# parameters, each representing a filename. The function
# should find if there are any instances of 5 or more
# consecutive words appearing in both files. If there are,
# return the longest such string of words (in terms of number
# of words, not length of the string). If there are not,
# return the boolean False.
#
# For simplicity, the files will be lower-case text and spaces
# only: there will be no punctuation, upper-case text, or
# line breaks.
#
# We've given you three files to experiment with. file_1.txt
# and file_2.txt share a series of 5 words: we would expect
# check_plagiarism("file_1.txt", "file_2.txt") to return the
# string "if i go crazy then". file_1.txt and file_3.txt
# share two series of 5 words, and one series of 11 words:
# we would expect check_plagiarism("file_1.txt", "file_3.txt")
# to return the string "i left my body lying somewhere in the
# sands of time". file_2.txt and file_3.txt do not share any
# text, so we would expect check_plagiarism("file_2.txt",
# "file_3.txt") to return the boolean False.
#
# Be careful: there are a lot of ways to do this problem, but
# some would be massively time- or memory-intensive. If you
# get a MemoryError, it means that your solution requires
# storing too much in memory for the code to ever run to
# completion. If you get a message that says "KILLED", it
# means your solution takes too long to run.


# Add your code here!

def check_plagiarism(filename_1, filename_2):
    doc_1 = open(filename_1, 'r')
    doc_2 = open(filename_2, 'r')
    for line in doc_1:
     words_1 = line.split(' ')
    for line in doc_2:
      words_2 = line.split(' ')
    doc_1.close()
    doc_2.close()
    plagia = []
    tups = []
    same = False
    for i in range(len(words_1) - 5):
      for j in range(len(words_2) - 5):
        if words_1[i:i + 5] == words_2[j:j + 5]:
            same = (i, j)
            tups.append(same)
    if same == False:
        return same
    for tup in tups:
        i = tup[0]
        j = tup[1]
        temp = []
        while words_1[i] == words_2[j]:
            temp.append(words_1[i])
            i += 1
            j += 1
        if len(temp) > len(plagia):
             plagia = temp

    return (' ').join(plagia)

# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# if i go crazy then
# i left my body lying somewhere in the sands of time
# False
print(check_plagiarism("file_1.txt", "file_2.txt"))
print(check_plagiarism("file_1.txt", "file_3.txt"))
print(check_plagiarism("file_2.txt", "file_3.txt"))
