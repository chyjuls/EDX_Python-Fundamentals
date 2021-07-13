for i in range(0, 5):
    print(i)
print("Done!")

i = 0
j = 100

while i < j:
    i = i + 10
    j = j - 10
    print("Looped!")
print()
for x in range(3):
    print("Looped!")
print()
for a in [10, 9, 8]:
    print("Looped!")
print()

i = 5
while i > 0:
    j = i
    while j > 0:
        print(j, end=" ")
        j -= 1
    i -= 1
    print("")