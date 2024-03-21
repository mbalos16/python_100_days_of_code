from turtle import Turtle
import random as rd

COLORS = [
    "ForestGreen",
    "CadetBlue",
    "SteelBlue",
    "Crimson",
    "Brown",
    "PaleVioletRed",
    "DodgerBlue",
]


class Block(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.width = 2
        self.height = 2
        self.x = 50
        self.y = 50
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._color = rd.choice(COLORS)
        self.velocity = 0.1

    def draw(self):
        self.shape("square")
        self.shapesize(stretch_wid=self.width, stretch_len=self.height, outline=0)
        self.penup()
        self.goto(self._x_pos, self._y_pos)
        self.color(self._color)
        return self