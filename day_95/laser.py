from turtle import Turtle, onkey


class Laser(Turtle):
    def __init__(self, step=20) -> None:
        super().__init__()
        self.penup()
        self.sety(-300)
        self.shape("square")
        self.width = 1
        self.height = 5
        self.step = step
        self.shapesize(stretch_wid=self.width, stretch_len=self.height, outline=0)
        onkey(self.look_right, "Right")
        onkey(self.look_left, "Left")

    def look_right(self):
        self.forward(self.step)

    def look_left(self):
        self.backward(self.step)