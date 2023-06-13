from turtle import Screen
from exercise22_1_pong_game_paddle import Paddle
from exercise22_1_pong_game_ball import Ball
from exercise22_1_pong_game_scoreboard import Scoreboard
import time

screen = Screen()

DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0


# Screen definition and game title
screen_width = 800
screen_height = 600
screen.setup(screen_width, screen_height)
screen.title("BMM • Pong Game")
screen.bgcolor("PeachPuff3")
screen.tracer(0)


# define the main elements. paddles at each side of the screen and the ball.
r_paddle = Paddle(x_pos=350, y_pos=0)
l_paddle = Paddle(x_pos=-350, y_pos=0)
ball = Ball(x_pos=0, y_pos=0)

scoreboard = Scoreboard()

# Use the keynboard to move the paddles.
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_played = True
while game_is_played:
    time.sleep(ball.velocity)
    screen.update()
    ball.movement()

    # Collision with ball.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.baunce_y()

    # collision with paddle right and left.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.baunce_x()
        scoreboard.l_point()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.baunce_x()
        scoreboard.r_point()

    if ball.xcor() > 380:
        ball.start_again()
        scoreboard.r_point()

    if ball.xcor() < -380:
        ball.start_again()
        scoreboard.l_point()

screen.exitonclick()
