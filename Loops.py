# Practicing for loops.

Colours = ["Red", "Blue", "Pink", "White", "Purple", "Navy"]




print ("What are you searching for....")
NewColour = input()


for colour in Colours:
        print(colour)
        if colour == NewColour:
             print("We Found" + " " + NewColour)
             break
print("End of iteration")