# Exercise 18.1 Turtle Draw a Square
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("circle")
tim.color("red")

# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)


for _ in range(4):
    tim.forward(100)
    tim.right(90)


screen = Screen()
screen.exitonclick()
