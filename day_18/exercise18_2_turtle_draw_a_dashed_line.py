# Exercise18_2 Turtle Draw a Dashed Line
from turtle import Turtle, Screen

tim = Turtle()
repetition = 20
line_length = 5

for i in range(repetition):
    tim.forward(line_length)
    tim.penup()
    tim.forward(line_length)
    tim.pendown()

screen = Screen()
screen.exitonclick()
