# Exercise 55.1. Create and add decorators

from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def add_bold():
        print("it should be strong")
        return "<b>" + function() + "</b>"

    return add_bold


def make_enphasis(function):
    def add_bold():
        return "<em>" + function() + "</em>"

    return add_bold


def make_underlined(function):
    def add_bold():
        return "<u>" + function() + "</u>"

    return add_bold


@app.route("/bye")
@make_bold
@make_enphasis
@make_underlined
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)