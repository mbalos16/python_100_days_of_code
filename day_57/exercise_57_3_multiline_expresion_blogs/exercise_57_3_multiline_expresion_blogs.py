# Exercise 57.1.Dinamic footer.
from flask import Flask, render_template
import requests

# --------------------------------------------------------------------
# Use flask to connect Python with HTML
app = Flask(__name__)


@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template(
        "exercise_57_3_multiline_expresion_blogs.html", posts=all_posts
    )


if __name__ == "__main__":
    app.run(debug=True)
