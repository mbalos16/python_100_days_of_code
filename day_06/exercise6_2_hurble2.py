# Exercise 6.2 - Hurdle 2

# Hurdles race
# Reeborg has entered a hurdle race, but he does not know in advance how long the race is. Make him run the course, following a path similar to the one shown, but stopping at the only flag that will be shown after the race has started.
# What you need to know

#     The functions move() and turn_left().
#     The condition at_goal() and its negation.
#     How to use a while loop.
# Your program should also be valid for world Hurdles 1.


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    jump()
