"""'
Using Python Turtle, build the classic shoot 'em up game - space invaders game.
Space Invaders Wikipedia Page: https://en.wikipedia.org/wiki/Space_Invaders 

Your space ship can move left and right and it can hit some alien ships. 
Every second the ALIENS will move closer to your ship. Once the ALIENS touch 
your ship then it's game over. There are usually some barriers between you 
and the ALIENS which offers you defensive positions.

You can play the game here:
https://elgoog.im/space-invaders/

"""

from turtle import Turtle, listen, onkey
from screen import build_main_screen
from score import Score
from laser import Laser
from ball import Ball
from alien import Alien
import time
import random as rd
from constants import FONT_SIZE

BALLS = []
ALIEN_FIRE_PROB = 0.005 # 5% of True probability
ALIEN_HITBOX_RADIUS = 30
USER_HITBOX_RADIUS = 50

screen = build_main_screen()

# Turn off drawing animation
screen.tracer(0)

# Instance some of the imported objects
score = Score()
laser = Laser()

def create_ALIENS(cols=7, rows=5):
    xcor_pos = -160
    ycor_pos = 200
    ALIENS = []
    for item in range(rows):
        for item in range(cols):
            alien = Alien(xcor=xcor_pos, ycor=ycor_pos)
            ALIENS.append(alien)
            xcor_pos += 55
        xcor_pos = -160
        ycor_pos += 55
    return ALIENS


# User's ball
def fire_ball_user():
    """A ball will be instanced and appended to the list of balls when this ball is called"""
    ball = Ball(laser.pos(), upwards=True)
    BALLS.append(ball)


# Alien's ball
def fire_ball_alien(alien):
    """A ball will be instanced and apended to the list of balls when this function is called"""
    ball = Ball(alien.pos(), upwards=False)
    BALLS.append(ball)


ALIENS = create_ALIENS()

# Call the function fire_ball_user when the user press the 'UP' key in the keyboard
onkey(fire_ball_user, "Up")
listen()


game_is_on = True
while game_is_on:

    # Check if balls hit laser
    for ball in BALLS:
        # Move the ball
        ball.automove()
        
        if ball.distance(laser) < USER_HITBOX_RADIUS and ball.isvisible() and ball.upwards != True:
            score.hit_user()
            ball.remove_ball()
            BALLS.remove(ball)
        
        for alien in ALIENS:
            if (
                ball.distance(alien.pos()) < ALIEN_HITBOX_RADIUS
                and ball.isvisible()
                and ball.upwards == True
            ):
                score.hit_alien()
                alien.remove_alien()
                ALIENS.remove(alien)
                ball.remove_ball()
                BALLS.remove(ball)
                
    # Check if there's life remaining
    if score.life <= 0:
        game_is_on = False
        if not game_is_on:
            final_message = Turtle()
            final_message.penup()
            final_message.hideturtle()
            final_message.write(
                f"Well done✨!\nYour score is {score.score}!",
                align="center",
                font=(FONT_SIZE),
            )
            final_message.pendown()

    # Automatically move the alien
    for alien in ALIENS:
        # The alien will fire randomly based on the following condition
        alien_fires = rd.random() < ALIEN_FIRE_PROB
        if alien_fires:
            fire_ball_alien(alien)
        alien.automove()

    # Screen operations
    screen.update()
    time.sleep(0.1)
time.sleep(10)
