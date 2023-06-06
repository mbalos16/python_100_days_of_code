# 19.2 Exercise turtle turtle race

from turtle import Turtle, Screen
import random

is_race_on = False

# Generate Screen, resize it and generate a prompt to get the bet
screen = Screen()
screen_width = 500
screen_height = 400
screen.setup(width=screen_width, height=screen_height)
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? \nChoose a color between: red, orange , yellow, green, blue or purple."
)

colors = ['red','orange', 'yellow', 'green', 'blue', 'purple' ]
all_turtles = []
turtle_size = 40

position_switch = 40
for color in colors:
    new_turtle = Turtle(shape="turtle")
    
    # No need for the turtle to draw
    new_turtle.penup()
    new_turtle.color(color)

    # Defining turtle's initial position.t)
   
    initial_point =  30
    x = (screen_width / 2) - (turtle_size/2)
    y = (screen_height / 2) - (turtle_size/2) - initial_point - position_switch
    new_turtle.goto(-x, -y)
    position_switch += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on =  True

stop_point = screen_width - turtle_size
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > stop_point:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                    
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()