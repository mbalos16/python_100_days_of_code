from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


app = Flask(__name__)
# login_manager = LoginManager()
# login_manager.init_app(app)

app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)


# CREATE TABLE IN DB
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Add a new user into the database.
def add_user_to_db(new_user):
    with app.app_context():
        db.session.add(new_user)
        db.session.commit()

def check_user_in_db(email, password):
    with app.app_context():
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
    if user is None:
        raise ValueError(f"Username {email} not found in db.")
    return user


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods = ["GET", "POST"])
def register():    
        if request.method == 'POST':
            
            #Create the new user in one variable and add it to the database.
            password_user = request.form.get("password")
            new_user = User(
                name = request.form.get("name"),
                email = request.form.get("email"),
                password = generate_password_hash(password_user, method='pbkdf2:sha256', salt_length=8),
            )
            add_user_to_db(new_user)
            #Redirect the user to the secrets page passing its name to the page.
            return render_template("secrets.html", user_name = request.form.get("name"))
        return render_template("register.html")
        

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == 'POST':
        #Check if the user has alredy an acount and is in the database.
        email = request.form.get("email")
        password_user=request.form.get("password")
        password = generate_password_hash(password_user, method='pbkdf2:sha256', salt_length=8)
        user = check_user_in_db(email, password)
        # print("-----------------")
        # print(user.password)
        # print(password)
        # print("-----------------")
        if user.password == password:
            #Redirect the user to the secrets page passing its name to the page.
            return render_template("secrets.html", user_name = user.name)
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory(
        'static/files', "cheat_sheet.pdf", as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)
