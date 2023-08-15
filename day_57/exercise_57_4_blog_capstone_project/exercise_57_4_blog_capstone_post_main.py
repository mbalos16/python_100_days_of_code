from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_post():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return all_posts


@app.route("/")
def home():
    all_posts = get_post()
    return render_template("exercise_57_4_blog_capstone_index.html", posts=all_posts)


@app.route("/post/<blog_id>")
def get_individual_blog(blog_id):
    all_posts = get_post()
    post = all_posts[int(blog_id) - 1]
    return render_template(
        "exercise_57_4_blog_capstone_post.html", post=post, blog_id=blog_id
    )


if __name__ == "__main__":
    app.run(debug=True)
