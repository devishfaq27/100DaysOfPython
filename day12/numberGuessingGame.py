import random
def numbers():
    random_number = random.randint(1, 101)
    print(random_number)

    lives = 0
    user_lives = input("chose easy level or hard level: ").lower()
    if user_lives == "easy":
        lives = 10
        print(f"you have {lives} lives...")
    elif user_lives == "hard":
        lives = 5
        print(f"you have {lives} lives")
    else:
        print("wrong input...")
        return

    game_over = False
    while not game_over:
        user_guess = int(input("Guess a number: "))
        if user_guess == random_number:
            print(f"You got this number was: {random_number}")
            game_over = True
        elif user_guess > random_number:
            print("guess is high...")
        else:
            print("guess is Low...")

        if user_guess != random_number:
            lives -= 1
            if lives == 0:
                game_over = True
                print(f"you are out of lives {lives}")
                print(f"the guess was {random_number}")

numbers()