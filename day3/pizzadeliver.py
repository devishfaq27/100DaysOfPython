print("welcome to python pizza delivery.")
size = input("what size pizza do you want, s, m or l: ")
pepperoni = input("Do you want pepperoni i your pizza? Y or N: ")
extra_cheese = input("Do you want extra chees on your piizza y or n: ")

bill = 0
if size == "s":
    bill = 15
elif size ==  "m":
    bill = 20
elif size == "l":
    bill = 25
else:
    print("you put the wrong inputs.")
if pepperoni == "y":
    bill += 3
else:
    bill += 0

if extra_cheese == "y":
    bill += 1
else:
    bill += 0

print(f"Your total bill is {bill}")
