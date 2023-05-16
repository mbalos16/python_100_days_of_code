# Exercise 6.4 - Hurdle 4

# Hurdles race
# Reeborg has entered a hurdle race. Make him run the course, following the path shown.
# The position, the height and the number of hurdles changes each time this world is reloaded.
# What you need to know
# You should be able to write programs that are valid for worlds Around 4 and Hurdles 3, and ot combine them for this last hurdles race.
# Your program should also be valid for worlds Hurdles 1, Hurdles 2 et Hurdles 3
# Difficulty level


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_top():
    turn_right()
    move()
    turn_right()


def move_forward():
    while not wall_in_front() and not at_goal():
        move()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_top()
    move_forward()
    turn_left()


while not at_goal():
    move_forward()
    if wall_in_front():
        jump()
