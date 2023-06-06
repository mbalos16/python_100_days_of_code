#  Exercise18.5 Turtle drawing a spirography
from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)
tim = Turtle()

tim.shape("turtle")


# Generate random colours based on rgb numbers.
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


# Draw the circles
def draw_spirograph(orientation, radius, colour):
    while orientation != 360:
        tim.color(random_colour())
        tim.setheading(orientation)
        tim.circle(radius)
        orientation += 5


tim.pensize(2)
color_random = random_colour()
turtle_orientation = 0
circle_radius = 100
tim.speed(100)

# Call the draw function
draw_spirograph(
    orientation=turtle_orientation, radius=circle_radius, colour=color_random
)

screen = Screen()
screen.exitonclick()
