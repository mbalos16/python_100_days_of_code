from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("MintCream")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_text()

    def update_text(self):
        self.clear()
        self.goto(-240, 260)
        self.write(
            f"Level: {self.level}",
            move=False,
            align="left",
            font=("Futura", 20, "normal"),
        )

    def game_over(self):
        self.goto(0, 0)
        self.write(
            f"GAME OVER!",
            move=False,
            align="center",
            font=("Futura", 30, "normal"),
        )
