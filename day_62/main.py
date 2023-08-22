from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, SelectField
from wtforms.validators import DataRequired
import csv


app = Flask(__name__)
# Random key
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField(
        label="Cafe name", validators=[DataRequired(), validators.InputRequired()]
    )
    location = StringField(
        label="Cafe Location on Google Maps (URL)",
        validators=[DataRequired(), validators.URL(), validators.InputRequired()],
    )
    open = StringField(
        label="Opening Times e.g.8AM",
        validators=[DataRequired(), validators.InputRequired()],
    )
    close = StringField(
        label="Closing Times e.g.5:30PM",
        validators=[DataRequired(), validators.InputRequired()],
    )
    coffee = SelectField(
        label="Coffee Rating",
        choices=["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"],
        validators=[DataRequired(), validators.InputRequired()],
    )

    wifi = SelectField(
        label="Wifi Strength Rating",
        choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
        validators=[DataRequired(), validators.InputRequired()],
    )
    power = SelectField(
        label="Power Socket Availability",
        choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
        validators=[DataRequired(), validators.InputRequired()],
    )
    submit = SubmitField(label="Submit")


# all Flask routes below
@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        csv_row = (
            f"{form.cafe.data},"
            f"{form.location.data},"
            f"{form.open.data},"
            f"{form.close.data},"
            f"{form.coffee.data},"
            f"{form.wifi.data},"
            f"{form.power.data}"
        )
        with open("day_62/cafe-data.csv", "a") as f:
            f.write(f"{csv_row}\n")
        return redirect("cafes")
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("day_62/cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
