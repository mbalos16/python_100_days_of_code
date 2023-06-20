import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("BMM • U.S. States Game")


# Create a turtle with the shape of an image.
states_image = "day_25/exercise25_3_us_states_game_50states_img.gif"
screen.addshape(states_image)
turtle.shape(states_image)


# The way to get a coordinate of a nod in an image.
# def get_mouse_click_coor(x, y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)

# Access the states column
states_df = pd.read_csv("day_25/exercise25_3_us_states_game_50states_data.csv")
states_database = (states_df["state"]).to_list()
guesses = []
score_count = 0
report = {"State": []}


def write_map(x, y, answer):
    """Needs x and y coordinates and a state name to write the state on the screen."""
    tim = turtle.Turtle()
    tim.hideturtle()
    tim.color("black")
    tim.penup()
    tim.goto(x=coord_x, y=coord_y)
    tim.write(answer_state)


game_is_on = True
while game_is_on:
    title_first_round = "Guess the U.S. State"
    title_round_two = f"{score_count}/50 States Correct"
    if score_count < 1:
        answer_state = screen.textinput(
            title=title_first_round, prompt="What's another state's name?"
        ).title()
    else:
        answer_state = screen.textinput(
            title=title_round_two, prompt="What's another state's name?"
        ).title()

    # Check if user state is part of the df. if so, write the name in the image.
    if answer_state in states_database:
        find_state = states_df[states_df["state"] == answer_state]

        if answer_state not in guesses:
            # generate coordinates for the turtule based on the datatbase state corrdinate
            coord_x = int(find_state["x"])
            coord_y = int(find_state["y"])

            # call the write map function passing the database state coordinate to write the state name in the map.
            write_map(coord_x, coord_y, answer_state)
            guesses.append(answer_state)
            score_count += 1

        # Check when the user arived guessed all the states.
        if score_count == 50:
            game_is_on = False

    # If the user uses the secret word "Exit" we generate a report with the missed words to help improvement
    if answer_state == "Exit":
        for state in states_database:
            if state not in guesses:
                report["State"].append(state)
        states_to_learn = pd.DataFrame(report)
        states_to_learn.to_csv("day_25/states_to_learn.csv", index=False)
        break

# Similar as as exitonclick()
turtle.mainloop()
