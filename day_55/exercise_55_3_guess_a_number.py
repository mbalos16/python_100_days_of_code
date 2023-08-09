# Exercise 55.2.f Guess the number
from flask import Flask
import random

app = Flask(__name__)


@app.route("/home")
def home():
    return (
        '<h1>"Guess a number between 0 and 9!"</h1>'
        '<img src ="https://media.giphy.com/media/qJ2a8MnK9MutrKSFNw/giphy.gif">'
    )


@app.route("/home/<int:user_number>")
def compare_with_random(user_number):
    random_number = random.randint(0, 9)
    if user_number < random_number:
        return "<h1 style='color:red'> Too low, try again </h1><img src ='https://media.giphy.com/media/5QW76Ww9bquHdg1fTv/giphy.gif'>"

    elif user_number > random_number:
        return "<h1 style='color:violet'> Too high, try again </h1><img src ='https://media.giphy.com/media/VlqzeaRnhCvPLfrSh6/giphy.gif'>"
    else:
        return "<h1 style='color:green'> You found me! </h1><img src ='https://media.giphy.com/media/kUwcAFFtecL0M4Hy2d/giphy.gif'>"


def guess_number(user_number):
    return f"{user_number} is"


if __name__ == "__main__":
    app.run(debug=True)
