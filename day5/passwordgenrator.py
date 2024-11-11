import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
numbers = str([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

nr_letters = int(input("how many letters you want in your password"))
nr_symbols = int(input("how many symbols you want in your password"))
nr_numbers = int(input("how many numbers you want in your numbers"))

# Easy Level
# password = ""
# for char in range(0, nr_letters):
#     password += random.choice(letters)
#
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
#
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# print(password)

#Hard Level
# password_list = []
# for char in range(nr_numbers):
#     password_list.append(random.choice(numbers))
#
# for char in range(nr_symbols):
#     password_list.append(random.choice(symbols))
#
# for char in range(nr_letters):
#     password_list.append(random.choice(letters))
#
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
#
# # password = ""
# # for char in password_list:
# #     password += char
# #
# # print(password)
# password = ""
# for char in password_list:
#     password += char
#
# print(password)



# password_list = []
# for char in range(nr_letters):
#     password_list.append(random.choice(letters))
# for char in range(nr_numbers):
#     password_list.append(random.choice(numbers))
# for char in range(nr_symbols):
#     password_list.append(random.choice(symbols))
#
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
#
# password = ""
# for char in password_list:
#     password += char
# print(password)


password_list = []
for char in range(nr_letters):
    password_list.append(random.choice(letters))
for char in range(nr_numbers):
    password_list.append(random.choice(numbers))
for char in range(nr_symbols):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
    password += char
print(password)