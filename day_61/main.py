from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField, validators
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"] = "[INSERT A PASSWORD HERE]"


class MyForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(), validators.Email()])
    password = PasswordField(
        label="Password", validators=[DataRequired(), validators.Length(min=8)]
    )
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        desired_email = "admin@email.com"
        desired_pass = "12345678"
        if form.email.data == desired_email and form.password.data == desired_pass:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
