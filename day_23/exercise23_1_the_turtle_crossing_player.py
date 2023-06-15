from turtle import Turtle
from exercise23_1_the_turtle_crossing_scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("midnightblue")
        self.shape("turtle")
        self.penup()
        self.start_point()
        self.setheading(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def start_point(self):
        self.goto(STARTING_POSITION)

    def is_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def finish_line(self):
        self.goto(STARTING_POSITION)
