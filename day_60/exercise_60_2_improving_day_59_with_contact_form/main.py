from flask import Flask, render_template, request
import requests
import requests
import smtplib

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


FROM_EMAIL = "[insert your email here]"
PERSONAL_API_PASSWORD = "[insert your email appi password here]"
TO_EMAIL = "[insert your email here]"


def send_email(msg):
    my_email = FROM_EMAIL
    my_password = PERSONAL_API_PASSWORD
    destination = TO_EMAIL

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=destination,
            msg=msg.encode("utf-8"),
        )


@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        msg = f"Subject: New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        send_email(msg)
        title = "Successfully sent your message."

        return render_template("contact.html", title=title)
    else:
        title = "Contact Me"
        return render_template("contact.html", title=title)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
