from turtle import Turtle
import time


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("SlateBlue4")
        self.penup()
        self.hideturtle()

        self.l_score = 0
        self.r_score = 0
        self.update_text()

    def update_text(self):
        self.clear()
        self.goto(140, 260)
        self.write(
            self.l_score, move=False, align="center", font=("Futura", 30, "normal")
        )
        self.goto(-140, 260)
        self.write(
            self.r_score,
            move=False,
            align="center",
            font=("Futura", 30, "normal"),
        )

    def l_point(self):
        self.l_score += 1
        self.update_text()

    def r_point(self):
        self.r_score += 1
        self.update_text()
