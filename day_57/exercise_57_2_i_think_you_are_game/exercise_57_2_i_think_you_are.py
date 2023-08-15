# Exercise 57.1.Dinamic footer.
from flask import Flask, render_template
import requests


# --------------------------------------------------------------------
# Access Agify.io to get the age
def get_years(user_name):
    apify_url = f"https://api.agify.io?name={user_name}"
    result = requests.get(apify_url)
    data = result.json()
    years = data["age"]
    return years


# --------------------------------------------------------------------
# Access Genderise.io to get the gender


def get_gender(user_name):
    genderize_url = f"https://api.genderize.io?name={user_name}"
    result = requests.get(genderize_url)
    data = result.json()
    gender = data["gender"]
    return gender


# --------------------------------------------------------------------
# Use flask to connect Python with HTML
app = Flask(__name__)


@app.route("/guess/<user_name>")
def home(user_name):
    years = get_years(user_name)
    gender = get_gender(user_name)
    return render_template(
        "exercise_57_2_i_think_you_are.html",
        name=user_name,
        gender=gender,
        age=years,
    )


if __name__ == "__main__":
    app.run(debug=True)
