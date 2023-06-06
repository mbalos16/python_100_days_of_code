# Exercise 18.6 Turtle drawing the hirst doted painting

import turtle as t
import random

t.colormode(255)

colors_rgb = [
    (198, 12, 32),
    (250, 237, 17),
    (39, 76, 189),
    (38, 217, 68),
    (238, 227, 5),
    (229, 159, 46),
    (27, 40, 157),
    (215, 74, 12),
    (15, 154, 16),
    (199, 14, 10),
    (243, 33, 165),
    (229, 17, 121),
    (73, 9, 31),
    (60, 14, 8),
    (224, 141, 211),
    (10, 97, 61),
    (221, 160, 9),
    (17, 18, 43),
    (46, 214, 232),
    (11, 227, 239),
    (81, 73, 214),
    (238, 156, 220),
    (74, 213, 167),
    (77, 234, 202),
    (52, 234, 243),
    (3, 67, 40),
    (218, 87, 49),
    (174, 178, 231),
    (237, 169, 164),
    (6, 245, 223),
    (247, 9, 42),
    (10, 79, 112),
    (16, 54, 243),
    (240, 16, 16),
]

def generate_dots(
    total_lines, dot_size, quantity, space_between_dots, y, x, real_space
):
    vertical_space = space_between_dots
    while total_lines != 0:
        # Horizontal line
        
        for i in range(quantity):
            dot_colour = random.choice(colors_rgb)
            tim.dot(dot_size, dot_colour)
            tim.penup()
            tim.forward(real_space)

        tim.penup()
        tim.goto(x, (y + vertical_space))
        tim.pendown()
        vertical_space += space_between_dots
        total_lines -= 1
    

tim = t.Turtle()
tim.penup()

# Control drawing speed
speed = 150
tim.speed(speed)

# Control x and y starting positions
x = -350
y = -150
tim.goto(x, y)
tim.pendown()

# Control space between dots and dots size
dot_size = 20
space_between_dots = 50
# The real_space is the space between dost - 1 dot,
# 1/2 of the one on the left, and other 1/2 of the one in the right
real_space = dot_size + space_between_dots

# Quantity of dots in horizontal, vertical and lines
quantity = 10
total_lines = 10

tim.hideturtle()
generate_dots(total_lines, dot_size, quantity, space_between_dots, y, x, real_space)


# Screen and print
screen = t.Screen()
screen.exitonclick()
