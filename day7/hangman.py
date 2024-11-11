import random
# import hangman_words
# import hangman_art
from hangman_words import word_list
from hangman_art import stages

lives = 6
chosen_word = random.choice(word_list)

print(chosen_word)

# placing "_" in place of chosen word make it blaks
word_length = len(chosen_word)
placeholder = ""
for position in range(word_length):
    placeholder += "_"
print(placeholder)

correct_letter = []
game_over = False

while not game_over:
    print(f"{lives} left")

    guess = input("Guess a latter: ").lower()
    print(guess)

    if guess in correct_letter:
        print(f"You've already guess {guess}")

    # making a veriable that will replace the correct letter in the blanks
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        print(f"You've guess wrong {guess}")
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"it was {chosen_word}")
            print("You Lose!")

    if "_" not in display:
        game_over = True
        print("You win")

    print(stages[lives])
