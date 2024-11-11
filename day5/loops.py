# fruits = ["Apple", "Pie", "Banana"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " peach")

# students_score = [15, 120, 121, 130, 199, 140, 150, 80, 100]
# max_score = 0
# for score in students_score:
#     if score > max_score:
#         max_score = score
#
# print(max_score)

# total = 0
# for numbers in range(1,101):
#     total += numbers
#     # print(total)
# print(total)

total = 0
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBizz!")
    elif num % 3 == 0:
        print("Fizz!")
    elif num % 5 == 0:
        print("Bizz!")
    else:
        print(num)