from turtle import Turtle
import time


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("day_20_21/exercise_20_21_1_snake_game_data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color("ivory")
        self.update_text()

    def update_text(self):
        self.clear()
        self.write(
            f"Score: {self.score} | High score: {self.high_score}",
            move=False,
            align="center",
            font=("Futura", 16, "normal"),
        )

    def hit_food(self):
        self.score += 1
        self.update_text()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("day_20_21/exercise_20_21_1_snake_game_data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_text()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(
    #         f"GAME OVER!",
    #         move=False,
    #         align="center",
    #         font=("Futura", 18, "normal"),
    #     )
