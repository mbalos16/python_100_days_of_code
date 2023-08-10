from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("exercise_56_1_my_personal_site_index.html")


if __name__ == "__main__":
    app.run(debug=True)
