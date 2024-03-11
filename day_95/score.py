from turtle import Turtle
from constants import FONT_SIZE


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.screen_height = self.screen.window_height()
        self.screen_width = self.screen.window_width()
        self.margins = 30
        self.life = 3
        self.score = 0
        self.display_life()
        self.display_score()

    def display_life(self):
        """Write the life in the left corner of the screen"""
        self.penup()
        self.hideturtle()
        self.sety(self.screen_height / 2 - self.margins)
        self.setx(self.screen_width / 2 - self.screen_width + self.margins)
        self.write(f"♥️ {self.life}", move=True, align="center", font=(FONT_SIZE))
        self.pendown()

    def display_score(self):
        """Write the score in the right corner of the screen"""
        self.penup()
        self.hideturtle()
        self.sety(self.screen_height / 2 - self.margins)
        self.setx(self.screen_height / 2 - self.margins)
        self.write(f"SCORE: {self.score}", move=False, align="center", font=(FONT_SIZE))
        self.pendown()

    def hit_alien(self):
        """Will update the score after each alien death."""
        self.score += 1
        self.update_score()

    def update_score(self):
        """Updates the score every time the score has been increased."""
        self.clear()
        self.display_life()
        self.display_score()

    def hit_user(self):
        """Updates the life when the user is shoot by the alien."""
        self.life -= 1
        self.life = max(self.life, 0)
        self.update_life()

    def update_life(self):
        """Updates the user's lives if hitten by an allien."""
        self.clear()
        self.display_life()
        self.display_score()


if __name__ == "__main__":
    turtle = Score()
    turtle.mainloop()
