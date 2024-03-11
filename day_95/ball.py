from turtle import Turtle, onkey, listen
from constants import UP, DOWN


class Ball(Turtle):
    def __init__(self, initial_pos, upwards) -> None:
        super().__init__()
        self.penup()
        self.shape("square")
        self.width = 0.4
        self.height = 0.8
        self.goto(initial_pos)
        self.setheading(UP)
        self.shapesize(stretch_wid=self.width, stretch_len=self.height, outline=0)
        self.upwards = upwards

    def ball_move_up(self):
        self.forward(10)

    def ball_move_down(self):
        self.backward(10)

    def automove(self):
        if self.upwards:
            self.ball_move_up()
        else:
            self.ball_move_down()

    def remove_ball(self):
        self.reset()
        self.hideturtle()
