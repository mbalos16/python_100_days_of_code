#  Exercise18.3 Turtle drawing different shapes
from turtle import Turtle, Screen
import random


def draw_poligon(tim, sides, size=20):
    angle = 360 / sides
    for i in range(sides):
        tim.forward(size)
        tim.right(angle)


def draw_poligons(tim, amount, size=20):
    for i in range(3, amount + 1):
        draw_poligon(tim=tim, sides=i, size=size)
        colour = random.choice(colours)
        tim.pencolor(colour)


tim = Turtle()

tim.shape("turtle")
tim.pensize(2)
colours = [
    "LightSalmon3",
    "LightPink4",
    "HotPink4",
    "IndianRed2",
    "orchid4",
    "firebrick",
    "OrangeRed4",
    "maroon",
]

draw_poligons(tim=tim, amount=60, size=40)

screen = Screen()
screen.exitonclick()