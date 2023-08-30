from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create a new instance of the flask app.
app = Flask(__name__)

# List of all the books.
all_books = []

# Create a new database
db = SQLAlchemy()

# Configure the SQLite database, relative to the app instance folder.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_library_collection.db"

# Initialize the app with the extension.
db.init_app(app)


# Create a new object called Model from the class Books.
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


def access_all_books():
    # Access all the books in the database and return them in a list format.
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = [item[0] for item in result]
    return all_books


@app.route("/")
def home():
    # Add a new book
    all_books = access_all_books()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_book = Book(
                title=request.form.get("book_name"),
                author=request.form.get("book_author"),
                rating=request.form.get("book_rating"),
            )
            db.session.add(new_book)
            db.session.commit()
        return redirect("/")
    return render_template("add.html")


def get_book(book_id):
    # Look for a book in the database based on its id and return it to the new website route.
    with app.app_context():
        book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    book = Book(
        title=book.title,
        author=book.author,
        rating=book.rating,
    )
    return book


def update_book(book_rating, book_id):
    # Access to the database and the book with its id and update the book rating.
    with app.app_context():
        book_to_update = db.session.execute(
            db.select(Book).where(Book.id == book_id)
        ).scalar()
        book_to_update.rating = book_rating
        db.session.commit()


@app.route("/edit/<book_id>", methods=["GET", "POST"])
def edit(book_id):
    if request.method == "GET":
        book = get_book(book_id)
        return render_template("edit.html", book=book)
    else:
        new_rating = request.form["book_rating"]
        update_book(new_rating, book_id)
        all_books = access_all_books()
        return render_template("index.html", all_books=all_books)


def delete_book(book_id):
    with app.app_context():
        book_to_delete = db.session.execute(
            db.select(Book).where(Book.id == book_id)
        ).scalar()
        db.session.delete(book_to_delete)
        db.session.commit()


@app.route("/delete/<book_id>", methods=["GET", "POST"])
def delete(book_id):
    if request.method == "GET":
        book = get_book(book_id)
        return render_template("delete.html", book=book)
    else:
        delete_book(book_id)
        all_books = access_all_books()
        return render_template("index.html", all_books=all_books)


if __name__ == "__main__":
    app.run(debug=True)
