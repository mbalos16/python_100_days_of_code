from turtle import Turtle
VELOCITY_INCREMENT = 1.01

class Ball(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("circle")
        self.width = 1
        self.height = 1
        self.shapesize(stretch_wid=self.width, stretch_len=self.height, outline=0)
        self.penup()
        self.goto(x_pos, y_pos)
        self.color("#E6E6FA")
        self.x_direction = 5
        self.y_direction = 5
        self.velocity = 1

    def movement(self):
        new_x = self.xcor() + self.x_direction * self.velocity
        new_y = self.ycor() + self.y_direction * self.velocity
        self.goto(new_x, new_y)

    def baunce_y(self):
        self.y_direction *= -1 
        self.velocity *= VELOCITY_INCREMENT
        
    def baunce_x(self):
        self.x_direction *= -1
        self.velocity *= VELOCITY_INCREMENT
