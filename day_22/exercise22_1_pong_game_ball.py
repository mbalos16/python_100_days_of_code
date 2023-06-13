from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("circle")
        self.width = 1
        self.height = 1
        self.shapesize(stretch_wid=self.width, stretch_len=self.height, outline=0)
        self.penup()
        self.goto(x_pos, y_pos)
        self.color("gray10")
        self.x = 10
        self.y = 10
        self.velocity = 0.1

    def movement(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def baunce_y(self):
        self.y *= -1

    def baunce_x(self):
        self.x *= -1
        self.velocity *= 0.9

    def start_again(self):
        self.goto(0, 0)
        self.velocity = 0.1
        self.baunce_x()
