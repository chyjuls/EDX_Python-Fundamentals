# This problem uses the same Pet, Owner, and Name classes from
# the previous problem.
#
# In this one, instead of printing a string that lists a single
# pet's owner, you will print a string that lists all of a
# single owner's pets.
#
# Write a function called get_pets_string. get_pets_string should
# have one parameter, an instance of Owner. get_pets_string
# should return a list of that owner's pets according to the
# following format:
#
# David Joyner's pets are: Boggle Joyner, Artemis Joyner

class Name:
    def __init__(self, first, last):
        self.first = first
        self.last = last


class Pet:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []


# Add your get_pets_string function here!
def get_pets_string(pet_owner):
    all_pets = []  # Create an empty list
    owner_name = pet_owner.name.first + " " + pet_owner.name.last  # get owner's first and last name variable.

    for a_pet in pet_owner.pets:  # iterate over the class Owner pets list
        the_pet_name = a_pet.name.first + " " + a_pet.name.last  # get firat and last name of pet
        all_pets.append(the_pet_name)  # append to new list
        new_pet_string = ', '.join(all_pets)  # create string using .join()
    return "{}'s pets are: {}".format(owner_name, new_pet_string)  # format string

    print()


# Below are e some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# David Joyner's pets are: Boggle Joyner, Artemis Joyner
# Audrey Hepburn's pets are: Pippin Hepburn
owner_1 = Owner(Name("David", "Joyner"))
owner_2 = Owner(Name("Audrey", "Hepburn"))

pet_1 = Pet(Name("Boggle", "Joyner"), owner_1)
pet_2 = Pet(Name("Artemis", "Joyner"), owner_1)
pet_3 = Pet(Name("Pippin", "Hepburn"), owner_2)

owner_1.pets.append(pet_1)
owner_1.pets.append(pet_2)
owner_2.pets.append(pet_3)

print(get_pets_string(owner_1))
print(get_pets_string(owner_2))
