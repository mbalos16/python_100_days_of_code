# Exercise 57.1.Dinamic footer.
from flask import Flask, render_template
import random
import datetime as dt

app = Flask(__name__)

now = dt.datetime.now()
year = now.year

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    return render_template("exercise_57_1_update_footer_dinamically_index.html", num=random_number, year=year)


if __name__ == "__main__":
    app.run(debug=True)
