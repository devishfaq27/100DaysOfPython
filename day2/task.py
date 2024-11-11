# print(type("string"))
# print(type(123))
# print(type(True))
# print(type(12.32))

# name_of_user =(input("Enter your name\n"))
# length = len(name_of_user)
# print("Number of latters in " + name_of_user + " is " + str(length))

# print((6 + 4 / 2 - (1 * 2)))
# a = int("5") / int(2.7)
# print(type(a))
# name = input("what is your name")
# print(f"your name is {name}")

# name = input("what is your name")
# print("hello" + name)
# age = str(12)
# print("your age is "+ age + "is")

# Day 2 final project
print("Welcome to the bill calculator")
bill = float(input("what was the total bill $"))
tip = int(input("what percentage tip would you like to give 10 12 15"))
people = int(input("how many peoples split the bill"))
tip_as_percentage = tip / 100
totla_tip_ammount = bill * tip_as_percentage
total_bill = bill  + totla_tip_ammount
bill_per_person = total_bill / people
final_ammount = round(bill_per_person, 2)
print(f"each person should pay {final_ammount}")
