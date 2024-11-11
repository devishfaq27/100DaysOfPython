import random
#                      Project: Number Guessing Game
#TODO- Import the random module to generate a random number.
#TODO- Create a variable secret_number and set it to a random number between 1 and 10 using random.randint(1, 10).
#TODO- Ask the user to guess the number by typing it.
#TODO- Store the user’s guess as an integer.
#TODO- If the user’s guess is equal to the secret_number, print “Congratulations! You guessed it!”
#TODO- If the guess is too low, print “Too low! Try again.”
#TODO- If the guess is too high, print “Too high! Try again.”
#TODO- Put steps 2 and 3 inside a while loop.
#TODO- Keep asking the user to guess until they get the correct number.
#TODO- When the user guesses correctly, break out of the loop and print “Game over!”

secret_number = random.randint(1, 10)
game = False
while not game:
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("Congratulations! You guessed it!”")
        game = True
    elif guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")

print("Game over!")