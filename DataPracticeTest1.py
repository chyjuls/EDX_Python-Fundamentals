def round_the_float(num):
    num = round(num, 2)
    return num


a = 2.71828
round_the_float(a)
b = a
print(b)
print(round_the_float(a))
print()


def absolute_reciprocal(an_int):
    abs(an_int)
    an_int = 1 / an_int
    return an_int


new_int = -5
(absolute_reciprocal(new_int))
print()


def find_the_positives(a_list):
    list_of_positives = []
    for i in range(len(a_list)):
        if i > 0:
            list_of_positives.append(a_list[i])
    return (list_of_positives)


my_list = [1, -5, 4, -4, 2, -1, 5, 9]
my_list = (find_the_positives(my_list))
print(my_list)
print()


def add_to_list(a_list, new_item, new_index):
    a_list.insert(new_index, new_item)


# my_list = ["L", "O", "N"]
# add_to_list(my_list, 1, "E")
# print(add_to_list(my_list, ))
# print()


def add_a_capitol(a_dict, a_state, a_city):
    a_dict[a_state] = a_city


my_capitols = {"Georgia": "Atlanta", "Idaho": "Boise", "Maine": "Augusta"}
my_capitols = add_a_capitol(my_capitols, "Texas", "Austin")
print(my_capitols)

a = 5
b = a
b += 5
c = a
c *= 2
a -= 5
print(a)
print(b)
print(c)
print()
list_1 = ["Bananas", "Apples", "Carrots"]
list_2 = list_1
list_1.sort()
list_2.append("Dewberry")
list_2.reverse()
print(list_1[0])
print(list_2[0])
print()



print()


