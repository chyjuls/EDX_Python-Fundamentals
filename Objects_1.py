# Write a class named "Phone". The Phone class should
# have an attribute called "storage" which defaults to
# 128, and an attribute called "color" which defaults
# to "red".
#
# Hint: 'attribute' is another common word for
# 'instance variable'.


# Write your class here!
class Phone:
    def __init__(self):
        self.storage = 128
        self.color = "red"


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print 128 and red, each on a separate line.
new_phone = Phone()
print(new_phone.storage)
print(new_phone.color)


class Student:
    def __init__(self):
        self.studentName = ""
        self.GPA = 0.0
        self.creditHours = 0
        self.enrolled = True
        self.classes = []


newStudent = Student()
newStudent.studentName = "George P. Burdell"
newStudent.GPA = 3.9
newStudent.creditHours = 1334
newStudent.enrolled = True
newStudent.classes = ["CS1301", "PHYS3001", "ISYE3029"]

print(newStudent.studentName)
print()


# Write a class named "Number" with one attribute called
# "value" which defaults to 0 and another attribute called
# "even" which defaults to True.
#
# Next, create an instance of this class and assign it to
# a variable called "number_instance".
#
# Then, set the value attribute to 101 and the even
# attribute to False.


# Write your code here!
class Number:
    def __init__(self):
        self.value = 0
        self.even = True


number_instance = Number()
number_instance.value = 101
number_instance.even = False
print(number_instance.value)
print(number_instance.even)


# Note that this exercise does not print anything by
# default. You're welcome to add print statements to debug
# your code when running it. Note that the autograder
# will check both your value for number_instance and your
# definition of the class Number.

class Student:
    def __init__(self, studentName, enrolled):
        self.studentName = studentName
        self.GPA = 0.0
        self.creditHours = 0
        self.enrolled = enrolled
        self.classes = []


newStudent = Student("Venus de Milo", False)
print(newStudent.studentName)
print(newStudent.enrolled)
print(newStudent.creditHours)


# Rewrite the "Number" class from 5.1.2 Coding Exercise 2.
# This time, however, require arguments for value and
# even in the constructor. Then, inside the constructor,
# create new instance variables called value and even that
# copy the values of the arguments passed into the
# constructor.
#
# In other words, rewrite the Number class such that value
# and even behave the way studentName and enrolled behaved
# in the exercise above, and the way firstname and lastname
# behaved in video 5.1.4.1.
#
# Then, as before, create an instance of this class and
# assign it to a variable called "number_instance". value
# should again be set to 101 and even should be set to
# False.
#
# Hint: Remember, the way you initialize the instance will
# have to change, too, based on the changes to the
# constructor that we're requiring.


# Write your code here!

class Number:

    def __init__(self, value, even):
        self.value = value
        self.even = even


number_instance = Number(101, False)
print(number_instance.value)
print(number_instance.even)

# Note that this exercise does not print anything by
# default. You're welcome to add print statements to debug
# your code when running it. Note that the autograder
# will check both your value for number_instance and your
# definition of the class Number.
print()


# Imagine you're writing an exercise-tracking app like Fitbit
# or MyFitnessPal. Part of your app is that a user can log an
# exercise session by naming the exercise, the intensity, and
# the duration.
#
# Write a class called ExerciseSession. ExerciseSession
# should have a constructor that requires two strings and an
# integer: the strings represent the exercise name and the
# exercise intensity, which will be "Low", "Moderate", or
# "High". The integer will represent the length of the
# exercise session in minutes. These should be saved in the
# instance of the class.
#
# Then, add three getters to the class. The getters should
# be named get_exercise, get_intensity, and get_duration,
# and should return the exercise string, the exercise
# intensity, and the duration, respectively.
#
# The setters should be named set_exercise, set_intensity,
# and set_duration. Each should have one parameter (besides
# self), which should be stored as the new value of
# exercise, intensity, or duration. You may assume only
# valid values will be passed in.
#
# HINT: You don't have to do any logging like you saw in
# the video! That was just an example of one benefit of
# using getters and setters, but this problem does not ask
# you to do that.


# Add your code here!

class ExerciseSession:
    def __init__(self, name, intensity, length=0.0):
        self.name = name
        self.intensity = intensity
        self.length = length

    def get_exercise(self):
        return self.name

    def get_intensity(self):
        return self.intensity

    def get_duration(self):
        return self.length

    def set_exercise(self, new_name):
        self.name = new_name

    def set_intensity(self, new_intensity):
        self.intensity = new_intensity

    def set_duration(self, new_duration):
        self.length = new_duration


# If your code is implemented correctly, the lines below
# will run error-free. They will result in the following
# output to the console:
# Running
# Low
# 60
# Swimming
# High
# 30
new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.get_exercise())
print(new_exercise.get_intensity())
print(new_exercise.get_duration())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.get_exercise())
print(new_exercise.get_intensity())
print(new_exercise.get_duration())
print()


class BankAccount:
    def __init__(self, name, balance=0.0):
        self.log("Account created!")
        self.name = name
        self.balance = balance

    def getBalance(self):
        self.log("Balance checked at " + str(self.balance))
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.log("+" + str(amount) + ":" + str(self.balance))

    def withdraw(self, amount):
        self.balance -= amount
        self.log("-" + str(amount) + ":" + str(self.balance))

    def log(self, message): ...


myBankAccount = BankAccount("David Joyner")
myBankAccount.deposit(20.0)
print(myBankAccount.getBalance())
myBankAccount.withdraw(10.0)
print(myBankAccount.getBalance())
print()


# Previously, you wrote a class called ExerciseSession that
# had three attributes: an exercise name, an intensity, and a
# duration.
#
# Add a new method to that class called calories_burned.
# calories_burned should have no parameters (besides self, as
# every method in a class has). It should return an integer
# representing the number of calories burned according to the
# following formula:
#
# - If the intensity is "Low", 4 calories are burned per
#   minute.
# - If the intensity is "Medium", 8 calories are burned
#   per minute.
# - If the intensity is "High", 12 calories are burned per
#   minute.
#
# You may copy your class from the previous exercise and just
# add to it.


# Add your code here!

class ExerciseSession:
    def __init__(self, name, intensity, length=0.0, ):
        self.name = name
        self.intensity = intensity
        self.length = length

    def get_exercise(self):
        return self.name

    def get_intensity(self):
        return self.intensity

    def get_duration(self):
        return self.length

    def set_exercise(self, new_name):
        self.name = new_name

    def set_intensity(self, new_intensity):
        self.intensity = new_intensity

    def set_duration(self, new_duration):
        self.length = new_duration

    def calories_burned(self):
        if self.intensity == "Low":
            return self.length * 4
        elif self.intensity == "Medium":
            return self.length * 8
        elif self.intensity == "High":
            return self.length * 12


# If your code is implemented correctly, the lines below
# will run error-free. They will result in the following
# output to the console:
# 240
# 360
new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.calories_burned())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.calories_burned())
print()


# Classes can also have references to other instances of
# themselves. Consider this Person class, for example,
# that allows for an instance of a father and mother
# to be given in the constructor.
#
# Create 3 instances of this class. The first should have
# the name "Mr. Burdell" with an age of 53. The second
# instance should have a name of "Mrs. Burdell" with an age
# of 53 as well. Finally, make an instance with the name of
# "George P. Burdell" with an age of 25. This final instance
# should also have the father attribute set to the instance
# of Mr. Burdell, and the mother attribute set to the
# instance of Mrs. Burdell. Finally, store the instance of
# George P. Burdell in a variable called george_p. (It does
# not matter what variable names you use for Mr. and Mrs.
# Burdell.)

class Person:
    def __init__(self, name, age, father=None, mother=None):
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother


# Write your code here!

FatherBurdell = Person("Mr. Burdell", 53)
MotherBurdell = Person("Mrs. Burdell", 53)
george_p = Person("George P. Burdell", 25, FatherBurdell, MotherBurdell)

# The code below will let you test your code. It isn't used
# for grading, so feel free to modify it. As written, it
# should print George P. Burdell, Mrs. Burdell, and Mr.
# Burdell each on a separate line.
print(george_p.name)
print(george_p.mother.name)
print(george_p.father.name)
print()


# Another method:

class Person:
    def __init__(self, name, age, father=None, mother=None):
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother


# We can even accomplish this all in one line by using the
# keyword parameters to the Person constructor:

george_p = Person("George P. Burdell", 25, mother=Person("Mrs. Burdell", 53), father=Person("Mr. Burdell", 53))


# We can use the keyword parameters to pass mother and father
# directly into the constructor, or we can even set those
# keywords equal to those new instances directly!

# We've given you a class called "Song" that represents
# some basic information about a song. We also wrote a
# class called "Artist" which contains some basic
# information about an artist.
#
# Your job is to create three instances of the song class,
# called song_1, song_2, and song_3.
#
# song_1 should have the following attributes:
#   name = "You Belong With Me"
#   album = "Fearless"
#   year = 2008
#   artist.name = "Taylor Swift"
#   artist.label = "Big Machine Records, LLC"
#
# song_2 should have the following attributes:
#   name = "All Too Well"
#   album = "Red"
#   year = 2012
#   artist.name = "Taylor Swift"
#   artist.label = "Big Machine Records, LLC"
#
# song_3 should have the following attributes:
#   name = "Up We Go"
#   album = "Midnight Machines"
#   year = 2016
#   artist.name = "LiGHTS"
#   artist.label = "Warner Bros. Records Inc."
#
# Notice, though, that song_1 and song_2 have the same
# artist and label. That means they should each have the
# SAME instance of artist: do not create separate instances
# of artist for each song.
#
# When your code is done running, there should exist three
# variables: song_1, song_2, and song_3, according to the
# requirements above.

class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label


class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist


# Write your code here!
artist_1 = Artist("Taylor Swift", "Big Machine Records, LLC")
artist_2 = Artist("LiGHTS", "Warner Bros. Records Inc.")
song_1 = Song("You Belong With Me", "Fearless", 2008, artist_1)

song_2 = Song("All Too Well", "Red", 2012, artist_1)

song_3 = Song("Up We Go", "Midnight Machines", 2016, artist_2)

# Feel free to add code to test your code below.
print(song_2.artist.label)
print()


# Below are the two class definitions we supplied previously:
# Artist and Song.
#
# Write a function called "get_song_string". It should accept
# one argument which will be a Song object. It should return
# a string in the following format:
#
# "<song name>" - <artist name> (<song year>)
# e.g:
# "You Belong With Me" - Taylor Swift (2008)
#
# The quotation marks around the song title should be *part*
# of the string.
#
# Hint: You're writing a function, not a method. That means
# the function get_song_string should not be inside either
# of these classes.

class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label


class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist


def get_song_string(new_song):
    new_song = '\"' + new_song.name + '\"' + " - " + new_song.artist.name + ' ('+ str(new_song.year)+ ')'
    return new_song


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: "You Belong With Me" -Taylor Swift (2008)
new_artist = Artist("Taylor Swift", "Big Machine Records, LLC")
new_song = Song("You Belong With Me", "Fearless", 2008, new_artist)
print(get_song_string(new_song))
