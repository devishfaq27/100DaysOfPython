import random
from art import logo
from data import data


#printing the data name profession country in a formate
def formate(account):
    account_name = account["name"]
    account_profession = account["profession"]
    account_country = account["country"]
    return f"Name is {account_name}, is a {account_profession} from {account_country}"


#now making a function that compaire a and b to print the correct answer
def compare(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

score = 0
account_b = random.choice(data)
continue_game = True
while continue_game:
    #taking random data from data file
    account_a = account_b
    account_b = random.choice(data)
    #make sure account_a is not equal to account_b
    if account_b == account_a:
        account_b = random.choice(data)

    print(f"Compare A: {formate(account_a)}")
    print(f"Against B: {formate(account_b)}")
    guess = input("Guess who has more followers on instagram A or B: ").lower()

    #taking the followers of celebraties and store it in the veriables
    account_a_followers = account_a["followers"]
    account_b_followers = account_b["followers"]

    #checking if user is corret or not
    isCorrect = compare(guess, account_a_followers, account_b_followers)
    if isCorrect:
        score += 1
        print(f"you are right!, your score is {score}")
    else:
        continue_game = False
        print(f"sorry you are wrong, your score is {score}")






# def format_data(account):
#     account_name = account["name"]
#     account_profession = account["profession"]
#     account_country = account["country"]
#     return f"name is {account_name} is a {account_profession} from {account_country}"
#
#
# def compare(user_guess, a_follower, b_follower):
#     if a_follower > b_follower:
#         return guess == "a"
#     else:
#         return guess == "b"
#
#
# print(logo)
# score = 0
# account_b = random.choice(data)
# is_continue = True
# while is_continue:
#     account_a = account_b
#     account_b = random.choice(data)
#     if account_b == account_a:
#         account_b = random.choice(data)
#
#     print(f"Compare A: {format_data(account_a)}")
#     print(f"Compare B: {format_data(account_b)}")
#     guess = input("who has more followers on instagram A or B: ").lower()
#
#     a_follower_count = account_a["followers"]
#     b_follower_count = account_b["followers"]
#     isCorrect = compare(guess, a_follower_count, b_follower_count)
#     if isCorrect:
#         score += 1
#         print(f"Your are right your score is: {score}")
#     else:
#         is_continue = False
#         print(f"wrong your score is: {score}")




















# def formate_data(account):
#     account_name = account["name"]
#     account_descr = account["profession"]
#     account_country = account["country"]
#     return f"{account_name}, a {account_descr} from {account_country}"
#
#
# def compire(user_guess, a_follower, b_follower):
#     if account_a["followers"] > account_b["followers"]:
#         return guess == "a"
#     else:
#         return guess == "b"
#
#
# print(logo)
# account_b = random.choice(data)
# score = 0
#
# is_continue = True
# while is_continue:
#     account_a = account_b
#     account_b = random.choice(data)
#     if account_a == account_b:
#         account_b = random.choice(data)
#
#     a_follower_count = account_a["followers"]
#     b_follower_count = account_b["followers"]
#     print(f"COMPARE A: {formate_data(account_a)} ")
#     print(f"AGAINST B: {formate_data(account_b)}")
#     guess = input("who has more followers on instagram: type A or B: ").lower()
#
#     isCorrect = compire(guess, a_follower_count,  b_follower_count)
#     if isCorrect:
#         score += 1
#         print(f"Your are right! score is {score}")
#     else:
#         is_continue = False
#         print(f"wrong, your score is {score}")
#
#





# def formate_data(account):
#     account_name = account["name"]
#     account_descr = account["profession"]
#     account_country = account["country"]
#     return f"{account_name}, a {account_descr} from {account_country}"
#
#
# def check_answer(user_guess, a_follower,  b_follower):
#     if a_follower > b_follower:
#         return user_guess == "a"
#     else:
#         return user_guess == "b"
#
#
# score = 0
# account_b = random.choice(data)
# game_should_continue = True
#
# while game_should_continue:
#     account_a = account_b
#     account_b = random.choice(data)
#
#     if account_a == account_b:
#         account_b = random.choice(data)
#     print(f"Compare A: {formate_data(account_a)}")
#     print(f"Against B: {formate_data(account_b)}")
#
#     a_follower_count = account_a["followers"]
#     b_follower_count = account_b["followers"]
#     guess = input("who has more followers, Type A or B: ").lower()
#     isCorrect = check_answer(guess, a_follower_count, b_follower_count)
#
#     if isCorrect:
#         score += 1
#         print(f"You are right your current score = {score}")
#     else:
#         game_should_continue = False
#         print(f"sorry you are wrong! your final score = {score}")
#
