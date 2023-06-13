from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.width = 5
        self.height = 1
        self.shapesize(stretch_wid=self.width, stretch_len=self.height, outline=0)
        self.penup()
        self.goto(x_pos, y_pos)
        self.color("SlateBlue4")

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
