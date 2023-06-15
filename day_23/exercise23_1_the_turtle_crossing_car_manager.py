from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.level = 0
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def create_cars(self):
        random_change = random.randint(1, 6)
        if random_change == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            random_y_pos = random.randint(-250, 250)
            new_car.goto(300, random_y_pos)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increment(self):
        self.car_speed += MOVE_INCREMENT
