from turtle import Turtle

LEFT = 180
RIGHT = 0
PADDLE_STEP = 10

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.width = 5
        self.height = 1
        self.shapesize(stretch_wid=self.height, stretch_len=self.width, outline=0)
        self.penup()
        self.goto(x_pos, y_pos)
        self.color("#E6E6FA")

    def go_left(self):
        if self.heading() != RIGHT:
            self.setheading(LEFT)
        new_x = self.xcor() - PADDLE_STEP
        self.goto(new_x, self.ycor())

    def go_right(self):
        if self.heading() != LEFT:
            self.setheading(RIGHT)
        new_x = self.xcor() + PADDLE_STEP
        self.goto(new_x, self.ycor())
