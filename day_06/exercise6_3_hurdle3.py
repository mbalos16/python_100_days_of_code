# Exercise 6.2 - Hurdle 3

# Hurdles race
# Reeborg has entered a hurdle race. Make him run the course, following the path shown.

# The position and number of hurdles changes each time this world is reloaded.
# What you need to know

#     The functions move() and turn_left().
#     The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
#     How to use a while loop and an if statement.

# Your program should also be valid for worlds Hurdles 1 and Hurdles 2.


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        jump()
