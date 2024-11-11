#              Fixing the bugs
# for i in range(1, 20):
#     if i == 20-1:
#         print("HI")

# try:
#     age = int(input("how old are you?"))
# except ValueError:
#     print("invalid value please enter a valid input such as 15. ")
#     age = int(input("how old are you?"))
#
# if age > 18:
#     print(f"your age is {age} now you can drive.")

# word_per_page = 0
# page = int(input("number of pages"))
# word_per_page == int(input("number of words per page"))
# total_word = page * word_per_page
#
# print(f"page = {page}")
# print(f"word per page = {word_per_page}")
# print(total_word)

# def odd_even(number):
#     if number % 2 == 0:
#         return "even"
#     else:
#         return "odd"
#
# print(odd_even(2))


#with bug
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 4000 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
# print(is_leap(2044))

#Solved the big
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
# print(is_leap(2044))

#with big
# Target is the number up to which we count
# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#         elif number % 3 == 0:
#             print("Fizz")
#         elif number % 5 == 0:
#             print("Buzz")
#         else:
#             print(number)
# fizz_buzz(15)

#Without bugs
# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         # use and (not or)
#         if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#         # use elif (not if)
#         elif number % 3 == 0:
#             print("Fizz")
#         # use elif (not if)
#         elif number % 5 == 0:
#             print("Buzz")
#         else:
#             # remove square brackets []
#             print(number)
# fizz_buzz(15)