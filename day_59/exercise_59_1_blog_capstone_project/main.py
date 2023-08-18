from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_post():
    blog_url = "https://api.npoint.io/9df0f6e5893a3260580a"
    response = requests.get(blog_url)
    all_posts = response.json()
    return all_posts


@app.route("/")
def home():
    all_posts = get_post()
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/<blog_id>")
def get_individual_blog(blog_id):
    all_posts = get_post()
    post = all_posts[int(blog_id) - 1]
    return render_template("post.html", post=post, blog_id=blog_id)


if __name__ == "__main__":
    app.run(debug=True)
