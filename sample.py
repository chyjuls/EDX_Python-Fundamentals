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


def average_word_length(my_string):
    letter_count = 0
    punct_1 = ['.', ',', '!', '?']
    try:
        word_count = len(my_string.split())
        print(word_count)

        for letter in my_string:
            if letter in punct_1:
                return "No words"
            if letter in "abcdefghijklmnopqrstuvwxyz" or letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter_count += 1
                # print(letter, letter_count)

                return letter_count / word_count
    except:
        return "No string"


print(average_word_length("Hi"))
print(average_word_length("Hi, Lucy"))
print(average_word_length("   What   big spaces  you    have!"))
print(average_word_length(True))
print(average_word_length("?!?!?! ... !"))
print()

dollar_fine = 0
days_late = 15
in_demand = True

if days_late == 10:
    dollar_fine = 10 * 1
    print(dollar_fine)

elif days_late > 10:
    dollar_fine = (10 * 1) + (days_late - 10) * 2
    print("$", dollar_fine)
elif in_demand:
    dollar_fine = (10 * 1) + (days_late - 10) * 2
    dollar_fine = dollar_fine  * dollar_fine
    print("$", dollar_fine)
else:
    print("$", dollar_fine)
