# showing more loops with continue function:

Colours = ["Red", "Blue", "Pink", "White", "Purple", "Navy", ]

print("What are you searching for....")
NewColour = input()

for colour in Colours:

    if colour == NewColour:
        print("We Found" + " " + NewColour)
        continue
    print(colour + "....Not what we are looking for......")
# Be careful with your indentation else your code will not work as it should do!!