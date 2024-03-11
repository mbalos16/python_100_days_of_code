from turtle import Turtle
from constants import ALIEN_COLOR

# fmt: off
# REAL_ALIEN = [(10.00,5.00), (15.00,5.00), (15.00,0.00), (20.00,0.00), (20.00,-5.00), (25.00,-5.00), (25.00,-10.00), (30.00,-10.00), (30.00,-15.00), (30.00,-20.00), (30.00,-25.00), (25.00,-25.00), (25.00,-20.00), (25.00,-15.00), (20.00,-15.00), (20.00,-20.00), (15.00,-20.00), (15.00,-25.00), (20.00,-25.00), (20.00,-30.00), (15.00,-30.00), (10.00,-30.00), (10.00,-25.00), (10.00,-20.00), (5.00,-20.00), (-0.00,-20.00), (-0.00,-25.00), (-0.00,-30.00), (-5.00,-30.00), (-10.00,-30.00), (-10.00,-25.00), (-5.00,-25.00), (-5.00,-20.00), (-10.00,-20.00), (-10.00,-15.00), (-15.00,-15.00), (-15.00,-20.00), (-15.00,-25.00), (-20.00,-25.00), (-20.00,-20.00), (-20.00,-15.00), (-20.00,-10.00), (-15.00,-10.00), (-15.00,-5.00), (-10.00,-5.00), (-10.00,0.00), (-5.00,0.00), (-5.00,5.00), (-0.00,5.00), (-0.00,0.00)]
ALIEN_PIXELS = [
    (-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2),
    (-1, -2), (-1, 2),
    (-0, -2), (-0, 2),
    ( 1, -2), ( 1, 2),
    ( 2, -2), ( 2, -1), ( 2, 0), ( 2, 1), ( 2, 2),
]
# fmt: on
# REAL_ALIEN_SIZE = 5
TURTLE_SIZE = 20

# Number of the height pixels of the alien
ALIEN_HEIGHT = 5

class Alien:
    def __init__(self, step=4, max_sideways_move=20, pixel_size=0.5, xcor=0, ycor=0):
        self.xcor = xcor
        self.ycor = ycor
        self.pixels = self.define_shape(pixel_size)
        self.step = step
        self.relative_pos = 0
        self.going_right = True
        self.max_sideways_move = max_sideways_move

    def automove(self):
        if not -self.max_sideways_move < self.relative_pos < self.max_sideways_move:
            if self.relative_pos >= self.max_sideways_move:
                # !!!!!!!!!!!!! If corY of the aliens in lower that the screen height minimum -> Aliens win
                self.move_down()
            self.going_right = not self.going_right

        if self.going_right:
            self.relative_pos += 1
            self.move_right(backwards=False)
        else:
            self.relative_pos -= 1
            self.move_right(backwards=True)

    def move_right(self, backwards=False):
        for pixel in self.pixels:
            if backwards:
                pixel.backward(self.step)
            else:
                pixel.forward(self.step)
        self.xcor = (
            self.xcor + self.step if backwards == False else self.xcor - self.step
        )

    def move_down(self):
        # !!!!!!!!!!!!! Move the compete line of pixels down and
        # !!!!!!!!!!!!! If the lines that appeared are less than 11, add a new line at the top
        for pixel in self.pixels:
            pixel.goto(pixel.xcor(), pixel.ycor() - self.step * ALIEN_HEIGHT)
        self.ycor = self.ycor - self.step * ALIEN_HEIGHT

    def define_shape(self, size):
        pixels = []
        for relative_pos in ALIEN_PIXELS:
            pix = Turtle("square")
            pix.color(ALIEN_COLOR)
            pix.penup()
            x = relative_pos[0] * TURTLE_SIZE * size + self.xcor
            y = relative_pos[1] * TURTLE_SIZE * size + self.ycor

            pix.setpos(x=x, y=y)
            pix.shapesize(stretch_wid=size, stretch_len=size, outline=0)
            pixels.append(pix)
        return pixels

    def pos(self):
        return (self.xcor, self.ycor)
    
    def remove_alien(self):
        for px in self.pixels:
            px.reset()
            px.hideturtle()