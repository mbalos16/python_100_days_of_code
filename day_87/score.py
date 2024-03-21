from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("GhostWhite")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_text()

    def update_text(self):
        self.clear()
        self.goto(380, 270)
        self.write(
            self.score, move=False, align="center", font=("Futura", 18, "normal")
        )

    def point(self):
        self.score += 1
        self.update_text()
