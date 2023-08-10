from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("exercise_56_3_name_card_index.html")


if __name__ == "__main__":
    app.run(debug=True)
