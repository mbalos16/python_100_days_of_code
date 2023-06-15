UP = 90
from turtle import Screen
from exercise23_1_the_turtle_crossing_player import Player
from exercise23_1_the_turtle_crossing_car_manager import CarManager
from exercise23_1_the_turtle_crossing_scoreboard import Scoreboard
import time

player = Player()
screen = Screen()
car = CarManager()
score = Scoreboard()


# Screen definition and game title
screen_width = 600
screen_height = 600

# The screen is "listening" to the keyboard.
screen.listen()
# When user use the up keyboard the turtle moves.
screen.onkey(player.move_forward, "Up")

screen.setup(screen_width, screen_height)
screen.title("BMM • The Turtle Crossing Game")
screen.bgcolor("MistyRose4")
screen.tracer(0)

game_is_played = True
while game_is_played:
    time.sleep(0.1)
    screen.update()

    # Create cars and move them
    car.create_cars()
    car.move_cars()

    # Detect collision with the car
    for element in car.all_cars:
        if element.distance(player) < 20:
            game_is_played = False
            score.game_over()
            
    # Detect when user pased a level.
    if player.is_finish_line():
        player.start_point()
        car.increment()
        score.level += 1
        score.update_text()
    car.level += 1
screen.exitonclick()
