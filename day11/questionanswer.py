import random
import math
#                         1. Number Guessing Game
#TODO-1: Goal: The computer picks a random number, and the user tries to guess it with hints on each guess.
#TODO-2: Generate a random number between 1 and 100.
#TODO-3: Ask the user to guess the number.
#TODO-4: If the guess is correct, congratulate them and end the game.
#TODO-5: If the guess is too high, print "Too high!" and let them guess again.
#TODO-6: If the guess is too low, print "Too low!" and let them guess again.
#TODO-7: Add a limit to the number of guesses they can make (like 5 or 10 tries).
#TODO-8: At the end, reveal the correct number if they didn’t guess it.

# def random_numbers():
#     num = random.randint(1,100)
#     print(num)
#     lives = 5
#     game_over = False
#     while not game_over:
#         user_guess = int(input("Guess the number: "))
#         if user_guess == num:
#             return "congratulate"
#         elif user_guess > num:
#             print("high")
#         else:
#             print("low")
#
#         if user_guess != num:
#             lives -= 1
#             if lives == 0:
#                 game_over = True
#                 print(f"remening lives: {lives} and the number: {num}")
#
# while input("want to play number guessing game, type 'y' for yes 'n' for no") == "y":
#     random_numbers()

#                   2. Rock, Paper, Scissors Game
#TODO-1: Goal: Play a game of Rock, Paper, Scissors against the computer.
#TODO-2: Create a function to take the user's choice of "rock," "paper," or "scissors."
#TODO-3: Generate a random choice for the computer.
#TODO-4: Compare the user’s choice with the computer’s choice using game rules:
#TODO-5: Rock beats Scissors
#TODO-6: Scissors beat Paper
#TODO-7: Paper beats Rock
#TODO-8: Print who won or if it was a draw.
#TODO-9: Ask if they want to play again, and loop if they say "yes."

# def rock_paper_scissor():
#     choice = ["rock", "paper", "scissor"]
#     computer_choice = random.choice(choice)
#
#     user_choice = input("pick one of these rock, paper and scissor: ").lower()
#     if user_choice not in choice:
#         print("please chose a valid input")
#         return
#
#     if user_choice == "paper" and computer_choice == "rock":
#         print("You win")
#     elif user_choice == "rock" and computer_choice == "scissor":
#         print("you win")
#     elif user_choice == "scissor" and computer_choice == "paper":
#         print("you win")
#     else:
#         print("you lose")
#     print(f"you choice: {user_choice} and computer choice: {computer_choice}")
#
# while input("do you want to play rock paper scissor game, type yes or no: ").lower() == "yes":
#     rock_paper_scissor()


#                          3. Simple Quiz Game
#TODO-1: Goal: Ask the user a few questions and keep track of their score.
#TODO-2: Create a list of 5–10 questions and answers.
#TODO-3: Loop through each question, showing it to the user.
#TODO-4: Check if their answer is correct; if it is, add to their score.
#TODO-5: Show their final score and ask if they want to play again.


# print("Welcome to the Quiz Game!")
# def question():
#     questions = [
#         {"question": "What is the capital of France?", "correct_answer": "paris"},
#         {"question": "What is 5 + 7?", "correct_answer": "12"},
#         {"question": "Which planet is known as the Red Planet?", "correct_answer": "mars"},
#         {"question": "Who wrote 'Romeo and Juliet'?", "correct_answer": "shakespeare"},
#         {"question": "What is the largest ocean on Earth?", "correct_answer": "pacific"}
#     ]
#
#     score = 0
#
#     for items in questions:
#         print(items["question"])
#         user_answer = input("Answer the question: ")
#         if user_answer == items["correct_answer"]:
#             print("correct")
#             score += 1
#         elif user_answer != items["correct_answer"]:
#             print("wrong answer")
#     print(score)
#
# while input("Do you want to play quiz game tpye yes or no") == "yes":
#     question()



#                        4. Dice Rolling Simulator
#TODO-1: Goal: Simulate rolling a dice and let the user roll as many times as they want.
#TODO-2: Create a function that generates a random number between 1 and 6 to simulate rolling a dice.
#TODO-3: Show the result to the user.
#TODO-4: Ask if they want to roll again.
#TODO-5: If they say "yes," roll again. If "no," end the game.

# def rolling():
#     roller_dice = random.randint(1, 6)
#     print(roller_dice)
#
# while input("do you want to roll it again, type yes or no: ") == "yes":
#     rolling()


#                                  5. Magic 8-Ball Game
#TODO-1: Goal: The user asks a yes/no question, and the program gives a random response like a Magic 8-Ball.
#TODO-2: Create a list of possible responses (e.g., "Yes," "No," "Maybe," "Ask again later").
#TODO-3: Ask the user to type a yes/no question.
#TODO-4: Randomly select a response from the list and show it to the user.
#TODO-5: Ask if they want to ask another question, and repeat if they say "yes."

# def magic_ball():
#     responses = ["yes", "no", "maybe", "ask again later"]
#
#
#     ask_user = input("type a yes/no: ")
#     if ask_user == "yes":
#         while input("want to ask another question: ") == "yes":
#             random_responses = random.choice(responses)
#             print(random_responses)
#     else:
#         return
#
# magic_ball()








