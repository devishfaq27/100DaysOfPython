import random
from hangman_words import word_list
from hangman_art import stages

chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)

correct_word = []

placeholder = ""
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
while not game_over:

    guess = input("Guess a letter: ")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_word.append(guess)
        elif letter in chosen_word:
            display += letter
        else:
            display += "_"
    print(display)

