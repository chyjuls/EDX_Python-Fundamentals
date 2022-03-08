def find_the_evens(a_list):
    list_of_evens = []
    for i in range(len(a_list)):
        if i % 2 == 0:
            list_of_evens.append(a_list[i])
            return list_of_evens


my_list = [1, 5, 4, 4, 2, 1, 5, 9]
find_the_evens(my_list)


def add_a_capitol(a_dict, a_state, a_city):
    a_dict[a_state] = a_city


my_capitols = {"Georgia": "Atlanta", "Idaho": "Boise", "Maine": "Augusta"}
print(add_a_capitol(my_capitols, "Texas", "Austin"))


def invert_dictionary(a_dict):
    new_dict = {}
    for key in a_dict:
        value = a_dict[key]
        new_dict[value] = a_dict[key]
    return new_dict


my_ords = {"A": 65, "B": 66, "C": 67, "D": 68}
my_ords = invert_dictionary(my_ords)
print(my_ords)

a = 10
b = a
a *= 2
b -= 5
print(a)
print(b)

a = ["X", "B", "R"]
b = a
a.append("Z")
b.sort()
b.append("A")
print(a[3])
print(b[4])
print()
a = {"Doe": 1, "Ray": 2, "Me": 3}
b = a
a["Fa"] = 4
b["Sew"] = 5
a["La"] = 6
b["Tea"] = 7
a["Doe"] = 8
print(a["Doe"])
print(b["Doe"])
print(a["Tea"])
print(b["La"])

print()
a = "I want"
a += " a "
b = a
b += "dog"
a += "house"
print(a)
print(b)

my_file = open("my_file.txt")
sum = 0
count = 0
for line in my_file:
    sum += int(line)
    count += 1
print(sum / count)
my_file.close()
