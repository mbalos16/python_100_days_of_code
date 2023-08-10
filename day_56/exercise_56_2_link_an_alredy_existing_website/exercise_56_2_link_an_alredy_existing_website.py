from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("exercise_56_2_link_an_alredy_existing_index.html")


if __name__ == "__main__":
    app.run(debug=True)
