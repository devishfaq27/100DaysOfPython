height = int(input("Enter your height: "))
if height >= 120:
    print("You can ride the rollercoaster!")

    age = int(input("Enter your age: "))

    if age < 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    want_photos = input("Do you want your ride photos? Enter 'y' for yes and 'n' for no: ")

    if want_photos.lower() == "y":
        bill += 3
        print(f"Your final bill is ${bill}.")
    else:
        print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you cannot ride the rollercoaster.")
