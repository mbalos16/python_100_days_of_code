# Exercise 14.1 - High lower game

# Create a game where the user has to choose the celebrity who has more followers in instagram.

from random import randint
import art_exercise14_1_higher_lower
from data_exercise14_1_higher_lower import data

game_continues = True
user_score = 0

# Print the game logo
print(art_exercise14_1_higher_lower.logo)


# Generate two random numbers no longer than the data list.
def give_random_number():
    """Generates a list of two random numbers from the data list"""
    celebrity_index = []
    for _ in range(2):
        data_length = len(data) - 1
        celebrity_index.append(randint(0, data_length))
    return celebrity_index


# Access the data and get a gelebrity based on the index of the randomly generated list celebrity_index.
def get_one_celebrity(index, data):
    """Gets an index and a list of dictionaries that stores celebrities and their details. Returns the data of the celebrity based on the index."""
    celebrity = data[index]
    return celebrity


def convert_user_answer(user_answer, first_celebrity, second_celebrity):
    # We asign a value to user answer.
    if user_answer == "a":
        user_answer = first_celebrity
    else:
        user_answer = second_celebrity
    return user_answer


# Compare user's answer with celebrity's instagram followers.
def compare_celebrities(
    game_continues, user_answer, first_celebrity, second_celebrity, user_score
):
    # Get the highest followers between the two celebrities:
    high_celebrity = {}

    if first_celebrity["follower_count"] > second_celebrity["follower_count"]:
        high_celebrity = first_celebrity
    else:
        high_celebrity = second_celebrity

    # Compare the user answer with the highest celebrity
    if user_answer["follower_count"] == high_celebrity["follower_count"]:
        user_score += 1
    else:
        game_continues = False

    # Return user_answer and if the game continue
    return user_score, game_continues


while game_continues:
    # Create a variable to store the score of the user.
    # Stores a list of two random numbers
    celebrity_index = give_random_number()

    # Get first and second celebrity.
    first_celebrity = get_one_celebrity(celebrity_index[0], data)
    second_celebrity = get_one_celebrity(celebrity_index[1], data)

    # Print the first celebrity, the VS logo and the second celebrity
    print(
        f"Compare A: {first_celebrity['name']}, a {first_celebrity['description']}, from {first_celebrity['country']}."
    )
    print(art_exercise14_1_higher_lower.vs)

    print(
        f"Against B: {second_celebrity['name']}, a {second_celebrity['description']}, from {second_celebrity['country']}."
    )

    # Ask for the celebrity with more followers on instagram
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Convert user answer from letter to dictionary and we asign the value of the choosen celebrity:
    user_answer = convert_user_answer(user_answer, first_celebrity, second_celebrity)

    # Compare the user answer with the value of the elements of the celebritie in the dictionary.
    user_score, game_continues = compare_celebrities(
        game_continues, user_answer, first_celebrity, second_celebrity, user_score
    )
    if game_continues:
        print(f"You're right! Current score: {user_score}.")

# We print the final score when the user lose.
print(f"Sorry, that's wrong. Final score: {user_score}.")
