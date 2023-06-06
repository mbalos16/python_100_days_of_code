#  Exercise18.4 Turtle drawing a random walk
from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)

tim = Turtle()


# Generate random colours based on rgb numbers.
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


# Exercise one was created with a list of colours instead of a random generation
# colours = [
#     "LightSalmon3",
#     "LightPink4",
#     "HotPink4",
#     "IndianRed2",
#     "orchid4",
#     "firebrick",
#     "OrangeRed4",
#     "maroon",
# ]


# # Generate random direction in random angle.
# def direction_random(thickness, colours, movement, tim):
#     while movement != 0:
#         random_number = random.randint(1, 4)
#         colour = random_colour()
#         tim.pencolor(colour)

#         if random_number == 1:
#             tim.forward(thickness)
#         elif random_number == 2:
#             tim.backward(thickness)
#         elif random_number == 3:
#             tim.right(thickness)
#         else:
#             tim.left(thickness)
#         movement = movement - 1


# Generate random direction in 90 degrees.
def direction_90_degrees(thickness, colours, movement, tim):
    angle = [0, 90, 180, 270]
    while movement != 0:
        colour = random_colour()
        tim.pencolor(colour)
        tim.setheading(random.choice(angle))
        tim.forward(thickness)


tim.pensize(20)
thickness = 50
velocity = 20
movement = 400
tim.shape("turtle")
tim.speed(velocity)

# direction_random(
#     thickness=thickness, colours=random_colour(), movement=movement, tim=tim
# )

direction_90_degrees(
    thickness=thickness, colours=random_colour(), movement=movement, tim=tim
)

screen = Screen()
screen.exitonclick()
