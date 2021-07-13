years = 0
months = 0
days = 7

days_we_have = (years * 365) + (months * 30) + days

if days_we_have >= (4 * 365):
    print("dog")
elif 365 <= days_we_have < (4 * 365):
    print("watch")
elif 6 * 30 <= days_we_have < 365:
    print("concert tickets")
elif 1 <= days_we_have < 6 * 30:
    print("candy")
else:
    print("yacht")
print()

mystery_int_1 = 3
mystery_int_2 = 4
mystery_int_3 = 5

while mystery_int_1 > 0 or mystery_int_2 > 0 or mystery_int_3 > 0:
    mystery_int_1 -= 1
    mystery_int_2 -= 1
    mystery_int_3 -= 1
    print(mystery_int_1, mystery_int_2, mystery_int_3)

a_num = 8

#
print()

while a_num * 2 < 10000:
    print(a_num * 2)
    a_num += 1

print()
print()

mystery_int = -7
print()
print()

a_string = "Up with the white and gold"

count = 1
for i in range(len(a_string)):
    if a_string[i] == ' ' or a_string == '/n' or a_string == '\t':
        count += 1
print(count)

print()


count_2 = 0
for k in a_string:
    if k != " ":
        count_2 += 1
print(count_2)
average = count_2/count
print(average)


