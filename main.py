import random
from art import logo


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    # Hint: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of
    # the actual score. 0 will represent a blackjack in our game.
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0

    # Hint : Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace
    # it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# Hint: Create a function called compare() and pass in the user_score and computer_score. If the computer and user
# both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has
# a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is
# over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(users_score, computers_score):
    if users_score == computers_score:
        return "Draw"
    elif computers_score == 0:
        return "You lost. Computer wins with a blackjack"
    elif users_score == 0:
        return "You win with a blackjack"
    elif users_score > 21:
        return "You lost. You went above 21."
    elif computers_score > 21:
        return "You win! Computer went above 21."
    elif users_score > computers_score:
        return "You win!"
    else:
        return "You lose. Computer scored higher."


# Hint : Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of
# blackjack and show the logo from art.py
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    game_over = False

    for x in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    # Hint: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be
    # repeated until the game ends.
    while not game_over:

        # Hint: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is
        # over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are: {user_cards} with a current score of {user_score}")
        print(f"Computer's first card is: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True

        # Hint: If the game has not ended, ask the user if they want to draw another card. If yes, then use the
        # deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        else:
            draw_card = input("Would you like to draw another card? Type 'y' or 'n': ")
            if draw_card == "y":
                user_cards.append(deal_cards())
            else:
                game_over = True

    # Hint: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long
    # as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(compare(users_score=user_score, computers_score=computer_score))
    print(f"The computer's final hand is {computer_cards} with a total of {computer_score}")


play_game()

while input("Would you like to play again? Type 'yes' to play again. Type 'no' to exit: ") == "y":
    import os
    os.system('clear')
    play_game()
else:
    game_over = True
