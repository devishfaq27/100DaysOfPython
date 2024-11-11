import random
def deal_car():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Its a Draw! "
    elif c_score == 0:
        return "you win, opponent has blackjack"
    elif u_score == 0:
        return "You lose, haveing a blackjack"
    elif u_score == 21:
        return "you went over, You lose"
    elif c_score == 21:
        return "computer went over, you win"
    elif u_score > c_score:
        return "you win!"
    else:
        return "you lose"


def play_game():
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1

    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_car())
        computer_cards.append(deal_car())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards: {user_cards} your score: {user_score}")
        print(f"computer cards: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("type 'y' to get another card and type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_car())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_car())
        computer_score = calculate_score(computer_cards)

    print(f"your final hand: {user_cards} your final score: {user_score}")
    print(f"computer final hand: {computer_cards} computer final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("do you want to play blackjack game type 'y' for yes and 'n' for no: ") == "y":
    play_game()






















# def deal_cards():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card
#
# # in this function we are calculating the score of user and computer in this
# # there is some rules if the sum of 2 cards equal 21 that will return 0
# # and sum of 2 cards are 21 and also 11 is in the cards then remove the 11 replace
# # with it 1
#
#
# def calculate_score(cards):
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)
#
# def compare(u_score, c_score):
#     if u_score == c_score:
#         return "Its a Draw! "
#     elif c_score == 0:
#         return "you win, opponent has blackjack"
#     elif u_score == 0:
#         return "You lose, haveing a blackjack"
#     elif u_score == 21:
#         return "you went over, You lose"
#     elif c_score == 21:
#         return "computer went over, you win"
#     elif u_score > c_score:
#         return "you win!"
#     else:
#         return "you lose"
#
#
# def play_game():
#     #creating a 2 variables that user cards and computer cards that will will
#     #  appand the deal_card function in these veriable
#     user_cards = []
#     computer_cards = []
#     user_score = -1
#     computer_score = -1
#     is_game_over = False
#     for _ in range(2):  # its mean it will run 1 for user cards and 2 for computer cards and appnd the value in user and computer cards
#         user_cards.append(deal_cards())
#         computer_cards.append(deal_cards())
#
#     while not is_game_over:
#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)
#
#         print(f"your cards {user_cards} and your score {user_score}")
#         print(f"computer cards {computer_cards[0]}")
#
#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             user_should_deal = input("type 'y' for another card or type 'n' for to pass: ").lower()
#             if user_should_deal == "y":
#                 user_cards.append(deal_cards())
#             else:
#                 is_game_over = True
#
#     while computer_score != 0 and computer_score < 17:
#         computer_cards.append(deal_cards())
#         computer_score = calculate_score(computer_cards)
#
#     print(f"your final hand {user_cards} and your final score {user_score}")
#     print(f"computer final hand {computer_cards} and computer final score {computer_score}")
#     print(compare(user_score, computer_score))
#
#
# while input("do you want to play blackjack game type 'y' for yes and type 'n' for no: ") == "y":
#     play_game()
