from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

# Initialize Ckeditor for flask app.
ckeditor = CKEditor()
ckeditor.init_app(app)

# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# Create a form with FlaskForms to add new blogs
class BlogForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    author = StringField(label="Your Name", validators=[DataRequired()])
    img_url = StringField(label="Blog Image URL", validators=[DataRequired()])
    body = CKEditorField(label="Blog Content")
    submit = SubmitField(label="SUBMIT POST")


# # Create a form with FlaskForms to edit a blog based on previows information

# class FilledBlogPost(FlaskForm):
#     title = StringField(label="Blog Post Title", validators=[DataRequired(message=title_message)])
#     subtitle = StringField(label="Subtitle", validators=[DataRequired(message=subtitle_message)])
#     author = StringField(label="Your Name", validators=[DataRequired(message=author_message)])
#     img_url = StringField(label="Blog Image URL", validators=[DataRequired(message=title_message)])
#     body = CKEditorField(label="Blog Content")
#     submit = SubmitField(label="SUBMIT POST")


with app.app_context():
    db.create_all()


def get_post(post_id):
    """Access the posts database and get the propper post based on the id."""
    with app.app_context():
        post = db.session.execute(
            db.select(BlogPost).where(BlogPost.id == post_id)
        ).scalar()
    post = BlogPost(
        title=post.title,
        subtitle=post.subtitle,
        date=post.date,
        body=post.body,
        author=post.author,
        img_url=post.img_url,
    )
    return post


def generate_blog_date():
    today = datetime.now()
    month = today.strftime("%B")
    day = today.strftime("%d")
    year = today.strftime("%Y")
    return f"{month} {day}, {year}"

def update_blog(post_id, updated_blog):
    """Access the posts database and update the propper post based on its previows id."""
    with app.app_context():
        post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
        post.title = updated_blog.title
        post.subtitle = updated_blog.subtitle
        post.body = updated_blog.body
        post.author = updated_blog.author
        post.img_url = updated_blog.img_url
        db.session.commit()

@app.route("/")
def get_all_posts():
    # Query the database for all the posts. Convert the data to a python list.
    all_posts = db.session.execute(
        db.select(BlogPost).order_by(BlogPost.title)
    ).scalars()
    posts = [post for post in all_posts]
    return render_template("index.html", all_posts=posts)


# Add a route so that you can click on individual posts.
@app.route("/<post_id>")
def show_post(post_id):
    # Retrieve a BlogPost from the database based on the post_id
    requested_post = get_post(post_id)
    return render_template("post.html", post=requested_post, post_id=post_id)


# Create the route add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    if request.method == "GET":
        form = BlogForm()
        return render_template("make-post.html", form=form)
    else:
        # Generate the date based on today.
        now = generate_blog_date()

        # Get the data from the form.
        new_blog = BlogPost(
            title=request.form.get("title"),
            subtitle=request.form.get("subtitle"),
            date=now,
            body=request.form.get("body"),
            author=request.form.get("author"),
            img_url=request.form.get("img_url"),
        )

        # Save the data in the database.
        db.session.add(new_blog)
        db.session.commit()

        # Redirect the user to the home page.
        return redirect("/")


# Create an edit_post() to change an existing blog post
@app.route("/edit_post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    if request.method == "GET":
        actual_post = get_post(post_id)
        form = BlogForm(
            title = actual_post.title,
            subtitle= actual_post.subtitle,
            body=actual_post.body,
            author=actual_post.author,
            img_url=actual_post.img_url
        )
        return render_template("make-post.html", form=form, post_id=post_id)
    else:
        # Get the data from the form using the actual id and date.
        updated_blog = BlogPost(
            title=request.form.get("title"),
            subtitle=request.form.get("subtitle"),
            body=request.form.get("body"),
            author=request.form.get("author"),
            img_url=request.form.get("img_url"),
        )
        update_blog(post_id=post_id, updated_blog=updated_blog)
        return redirect(url_for('show_post', post_id=post_id))

# A delete_post() route to remove a blog post from the database
@app.route("/delete/<post_id>", methods =["GET"])
def delete(post_id):
    post_to_delete = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
