from turtle import Screen
from exercise20_21_1_snake_game_snake import Snake
from exercise20_21_1_snake_game_food import Food
from exercise20_21_1_snake_game_scoreboard import Scoreboard
import time

screen = Screen()


# Screen definition and game title
screen_width = 600
screen_height = 600
screen.setup(screen_width, screen_height)
screen.title("BMM • Snake Game")
screen.bgcolor("DarkSlateGrey")

# Tracer turns off the animation
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    snake.move()

    # Detect collision with food and refresh food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.hit_food()

    # Detect collision with wall.
    if (
        snake.head.xcor() > 285
        or snake.head.xcor() < -285
        or snake.head.ycor() > 285
        or snake.head.ycor() < -285
    ):
        score.reset()
        snake.reset()

    # Detect collision with wall.
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
screen.exitonclick()
