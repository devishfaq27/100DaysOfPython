import random
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
        39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
        57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
        75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92,
        93, 94, 95, 96, 97, 98, 99, 100]

#TODO-1: Generate a random number between 1 and 100.
#TODO-2: Ask the user to guess the number.
#TODO-3: If the guess is correct, congratulate them and end the game.
#TODO-4: If the guess is too high, print "Too high!" and let them guess again.
#TODO-5: If the guess is too low, print "Too low!" and let them guess again.
#TODO-6: Add a limit to the number of guesses they can make (like 5 or 10 tries).
#TODO-7: At the end, reveal the correct number if they didn’t guess it.

computer_guess = random.choice(nums)
print(computer_guess)
lives = 5
is_game_over = False

while not is_game_over:
    guess = int(input("guess the correct number: "))
    if guess == computer_guess:
        print("Congrats your is correct")
        is_game_over = True
    elif guess < computer_guess:
        print("Low!")
    else:
        print("High")

    if guess != computer_guess:
        lives -= 1
        print(lives)
        if lives == 0:
            print("Game Over! ")
            is_game_over = True


