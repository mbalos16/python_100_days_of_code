"""
On day 66, we create an API that serves data on cafes with wifi and good coffee. Today, you're going to use the data from that 
project to build a fully-fledged website to display the information.
Included in this assignment is an SQLite database called cafes.db that lists all the cafe data.

Using this database and what you learnt about REST APIs and web development, create a website that uses this data. 
It should display the cafes, but it could also allow people to add new cafes or delete cafes.
For example, this startup in London has a website that does exactly this:
https://laptopfriendly.co/london
"""

from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

# Create a new instance of the app
app = Flask(__name__)

# List of all cafes
all_cafes = []

# Create the connection with the database
db = SQLAlchemy()

# Path to the database
db_path = os.path.join(os.path.dirname(__file__), "cafes.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
db.init_app(app)

# Create a new object called Model from the class Cafes.
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/shops")
def coffee_shops():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars()
    print(all_cafes)
    return render_template("coffee_shops.html", all_cafes=all_cafes)

@app.route("/delete", methods=["GET", "POST"])
def delete_coffee():
    if request.method == "GET":
        return render_template("delete.html")
    if request.method == "POST":
        id = request.form.get("coffee_id")
        coffee_to_delete = db.get_or_404(Cafe, id)
        coffee_name = coffee_to_delete.name
        db.session.delete(coffee_to_delete)
        db.session.commit()
        return redirect(url_for("delete_confirmation", coffee_name=coffee_name))

@app.route("/suggest_coffee", methods=["GET", "POST"])
def suggest_coffee():
    if request.method == "POST":
        new_coffee_name = request.form.get("name")
        new_coffee = Cafe(
            name=new_coffee_name,
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            has_sockets=1 if request.form.get("sockets", "") else 0,
            has_toilet=1 if request.form.get("toilets", "") else 0,
            has_wifi=1 if request.form.get("wifi", "") else 0,
            can_take_calls=1 if request.form.get("can_take_calls", "") else 0,
            seats=request.form.get("seats"),
            coffee_price=f"£{request.form.get('coffee_price')}",
        )
        db.session.add(new_coffee)
        db.session.commit()
        return redirect(url_for("saved", new_coffee_name=new_coffee_name))
    return render_template("suggest.html")

@app.route("/confirmation/<coffee_name>")
def delete_confirmation(coffee_name):
    return render_template("delete_confirmation.html", coffee_name=coffee_name)

@app.route("/<new_coffee_name>")
def saved(new_coffee_name):
    return render_template("saved_confirmation.html", new_coffee_name=new_coffee_name)

if __name__ == "__main__":
    app.run(debug=True, port=5000)