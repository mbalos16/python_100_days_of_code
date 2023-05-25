# Exercise 11.1 Blackjack Capstone Project


############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


# Import the art file and random
import art_exercise11_1_blackjack
import random

# random.seed(125)

# A list of cards where all have the same probability to be chosen.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


############### Functions #####################
# Get a random card from a list.
def get_card():
    """Returns a random card from the deck"""
    return cards[random.randint(0, (len(cards) - 1))]


def current_score(player_hand):
    """Returns the sum of all the cards of the player."""
    final_score = 0
    for card in player_hand:
        final_score += card
    if final_score > 21:
        for card in player_hand:
            if card == 11:
                final_score -= 10
                if final_score <= 21:
                    break
    return final_score


# Print all of this when the user win or lose
def print_details(
    user_hand,
    computer_hand,
    print_computer_hand=False,
):
    """Prints user hand, computer hand and scores."""
    print(f"    Your cards: {user_hand}, current score: {current_score(user_hand)}")
    print(f"    Computer's first card: {computer_hand[0]}.")
    print("----------------------------------------------")
    print(f"    Your final hand: {user_hand}.")

    if print_computer_hand == True:
        print(
            f"    Computer's final hand: {computer_hand}, current score:{current_score(computer_hand)}."
        )


def check_if_win(user_hand, computer_hand):
    """Checks if the user wins and prints the result."""
    # When the user is above 21
    if current_score(user_hand) > 21:
        print_details(
            user_hand,
            computer_hand,
        )
        print("You went over.You lose 😭")

    else:
        # Computer above 17, get new card
        while current_score(computer_hand) < 17:
            computer_hand.append(get_card())

        print_details(user_hand, computer_hand, print_computer_hand=True)

        # Draw
        if current_score(user_hand) == current_score(computer_hand):
            print("This was a draw 🤪 ")

        # Computer wins
        elif (
            current_score(user_hand) < current_score(computer_hand)
            and current_score(computer_hand) <= 21
        ):
            print("You lose 😭.")

        # User wins
        elif (
            current_score(user_hand) > current_score(computer_hand)
            or current_score(computer_hand) > 21
        ):
            print("You win 😁!")


# Ask the user if wants a new card?
def ask_new_card(user_hand):
    """Returns an updated hand for the user adding a nwe card"""
    answer = input(" Type 'y' to get another card, type 'n' to pass: ").lower()
    if answer == "y":
        user_wants_new_card = True
        user_hand.append(get_card())
    elif answer == "n":
        user_wants_new_card = False
    # Return the True/False boolean to alow the while loop to continue or not
    return user_wants_new_card, user_hand


# Play the game
def play(user_hand, computer_hand):
    """Checks if the user wants to play. If so, will add as many new cards to the user hand as the user wants, and next checks if the user wins."""
    print(art_exercise11_1_blackjack.logo)
    user_wants_new_card = True
    while current_score(user_hand) < 21 and user_wants_new_card:
        print(f"    Your cards: {user_hand}, current score: {current_score(user_hand)}")
        print(f"    Computer's first card: {computer_hand[0]}.")
        user_wants_new_card, user_hand = ask_new_card(user_hand)
    check_if_win(user_hand, computer_hand)


# Do you want to play?
def start():
    """Checks if the user wants to play and if so, prints the logo, generate the first hand and starts the game"""
    do_you_play = input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if do_you_play == "y":
        # Get random cards for user and computer's hands from the list.
        user_hand = [
            get_card(),
            get_card(),
        ]
        computer_hand = [get_card(), get_card()]
        play(user_hand, computer_hand)


start()
