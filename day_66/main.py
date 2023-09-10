from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
import random

app = Flask(__name__)

##Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
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

    def to_dict(self):
        # Example shown by TheMuellenator in github, Link: https://gist.github.com/TheMuellenator/30a66ba90f003f68ad0218f2d54608c8
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    """Returns a jason with a random cafe in the database."""
    if request.method == "GET":
        with app.app_context():
            result = db.session.execute(db.select(Cafe))
            all_cafes = result.scalars().all()
            random_cofe_shop = random.choice(all_cafes)

        # # First way to return the data as a JSON
        # is by using jsonify and write down each element:

        # return jsonify(
        #     id=random_cofe_shop.id,
        #     name=random_cofe_shop.name,
        #     map_url=random_cofe_shop.map_url,
        #     img_url=random_cofe_shop.map_url,
        #     location=random_cofe_shop.location,
        #     seats=random_cofe_shop.seats,
        #     has_toilet=random_cofe_shop.has_toilet,
        #     has_wifi=random_cofe_shop.has_wifi,
        #     has_sockets=random_cofe_shop.has_sockets,
        #     can_take_calls=random_cofe_shop.can_take_calls,
        #     coffee_price=random_cofe_shop.coffee_price,
        # )

        # Another better way is to 1st convert the data
        # to dictionary in the main class
        # and next convert it to jsonify.
        return jsonify(cafe=random_cofe_shop.to_dict())


@app.route("/all")
def get_all_cafes():
    """Returns a jason with all the cafes in the database."""
    if request.method == "GET":
        with app.app_context():
            result = db.session.execute(db.select(Cafe))
            all_cafes = result.scalars().all()
            cafe_dict = [cafe.to_dict() for cafe in all_cafes]
        return jsonify(cafe_dict)


# The way of defining input arguments to work in Postman.
@app.route("/search/", methods=["GET"])
def get_location():
    """Returns a jason with all the cafes in the database."""
    location = request.args.get("location")
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(
            cafes=[cafe.to_dict() for cafe in all_cafes if cafe.location == location]
        )
    else:
        return (
            jsonify(
                error={"Not Found": "Sorry, we don't have a cafe at that location."}
            ),
            404,
        )


## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == "__main__":
    app.run(debug=True)
