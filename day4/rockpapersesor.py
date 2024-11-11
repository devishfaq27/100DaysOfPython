import random
rock = 0
paper = 1
sesor = 2

user_choice = int(input('Enter 0 for "0" for "Rock", "1" for "Paper", "2" for "Sesor":  '))
# print(f"your choice {user_choice}")
computer_choice = random.randint(0,1)
# print(f"computer choice {computer_choice}")

if user_choice >= 3 or user_choice < 0:
    print("You typed an invilad you lose")
elif user_choice == 0 and computer_choice == 2:
    print("you win")
elif computer_choice == 0 and user_choice == 2:
    print("you lose")
elif computer_choice > user_choice:
    print("you win")
elif user_choice > computer_choice:
    print("you win")
elif computer_choice == user_choice:
    print("its draw")