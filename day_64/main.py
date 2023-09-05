from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
# import json

# Create a new database
db = SQLAlchemy()

# Create a new instance of the flask app.
app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

TMDB_API_KEY = "a0f9728c952bf3ad0de86533ca929da0"
TMDB_API_READ_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMGY5NzI4Yzk1MmJmM2FkMGRlODY1MzNjYTkyOWRhMCIsInN1YiI6IjY0ZjFhOTY1OTdhNGU2MDBhYzNlYzhiMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.PUIGg_oQCA6oznXz_CQdF1GXJeUe3CT8K0291vCHlkA"


# Configure the SQLite database, relative to the app instance folder.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_film_collection.db"

# Initialize the app with the extension.
db.init_app(app)


# Create a new object called Model from the class Books.
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Float, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


# Create the table.
with app.app_context():
    # db.drop_all()
    db.create_all()
    db.session.commit()


# Add a new movie to the database.
def add_movie_to_db(movie):
    with app.app_context():
        db.session.add(movie)
        db.session.commit()


# # Add a new movie.
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg",
# )
# add_movie_to_db(new_movie)

# # Add a second movie.
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg",
# )
# add_movie_to_db(second_movie)


# Create an update form with FlaskForms.
class MyForm(FlaskForm):
    rating = StringField(
        label="Your rating out of 10 e.g. 7.5", validators=[DataRequired()]
    )
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class MyMovie(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")

def access_all_movies():
    # Access all the books in the database and return them in a list format.
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.rating))
        all_movies = [movie[0] for movie in result]
    return all_movies

def get_movie(movie_id):
    """Access the movies database and get the propper movie based on the id."""
    with app.app_context():
        movie = db.session.execute(
            db.select(Movie).where(Movie.id == movie_id)
        ).scalar()
    movie = Movie(
        title=movie.title,
        year=movie.year,
        description=movie.description,
        rating=movie.rating,
        ranking=movie.ranking,
        review=movie.review,
        img_url=movie.img_url,
    )
    return movie


def update_movie_data(movie_id, movie_rating, movie_review):
    """Access the book in the database and with it's id update the book rating and review."""
    with app.app_context():
        movie_to_update = db.session.execute(
            db.select(Movie).where(Movie.id == movie_id)
        ).scalar()
        movie_to_update.rating = movie_rating
        movie_to_update.review = movie_review
        db.session.commit()


def delete_movie(movie_id):
    with app.app_context():
        movie_to_delete = db.session.execute(
            db.select(Movie).where(Movie.id == movie_id)
        ).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()


# Route to the home.
@app.route("/")
def home():
    all_movies = access_all_movies()
    count = len(all_movies)+1
    for movie in all_movies:
        count -=1
        with app.app_context():
            movie_to_update = db.session.execute(
                db.select(Movie).where(Movie.title == movie.title)
            ).scalar()
            movie_to_update.ranking = count
            db.session.commit()
        all_movies = access_all_movies()
    return render_template("index.html", all_movies=all_movies)


# Edit the rating and review of the movies.
@app.route("/edit/<movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    form = MyForm(request.form)
    if request.method == "GET":
        movie = get_movie(movie_id)
        return render_template("edit.html", movie=movie, form=form)
    else:
        movie_rating = form.rating.data
        movie_review = form.review.data
        update_movie_data(movie_id, movie_rating, movie_review)
        return redirect(url_for("home"))


# Delete a movie by clicking in the Delete button. Issue: no popup for confirmation, directly.
@app.route("/delete/<movie_id>", methods=["GET", "POST"])
def delete(movie_id):
    delete_movie(movie_id)
    return redirect(url_for("home"))


# Access the TMDB api to get the movies details and add them to the page
def access_movie_details(movie_title):
    """Gets the title of a movie and returns a list of lists with the movies that include that title, movie id and release year"""
    url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=false&language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_API_READ_ACCESS_TOKEN}",
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    movies = [
        [movie["title"], movie["release_date"], movie["id"]]
        for movie in data["results"]
    ]
    return movies


def get_movie_details(movie_id):
    """Gets movie id and returns all the details after requesting them to the API database."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_API_READ_ACCESS_TOKEN}",
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data


# Add a new movie
@app.route("/add", methods=["GET", "POST"])
def add():
    form = MyMovie(request.form)
    if request.method == "GET":
        return render_template("add.html", form=form)
    if request.method == "POST":
        movie_title = form.title.data
        movies_list = access_movie_details(movie_title)
        print(movies_list)
        return render_template("select.html", form=form, movies_list=movies_list)


@app.route("/add/<movie_id>", methods=["GET", "POST"])
def include_movie_info_into_db(movie_id):
    movie_details = get_movie_details(movie_id)
    # This code helped us to beautifuly see the json code printed in the console.
    # print(json.dumps(movie_details, indent=4))
    img_rel_url = movie_details["poster_path"]
    new_movie = Movie(
        title=movie_details["original_title"],
        year=movie_details["release_date"][:4],
        description=movie_details["tagline"],
        rating=movie_details["vote_average"],
        ranking=None,
        review=None,
        img_url=f"https://image.tmdb.org/t/p/w500{img_rel_url}",
    )
    add_movie_to_db(new_movie)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
