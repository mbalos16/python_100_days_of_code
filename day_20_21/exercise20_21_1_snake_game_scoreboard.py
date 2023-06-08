from turtle import Turtle
import time


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color("ivory")
        self.score = 0
        self.update_text()

    def update_text(self):
        self.clear()
        self.write(
            f"Score: {self.score}",
            move=False,
            align="center",
            font=("Futura", 16, "normal"),
        )

    def hit_food(self):
        self.score += 1
        self.update_text()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            f"GAME OVER!",
            move=False,
            align="center",
            font=("Futura", 18, "normal"),
        )
