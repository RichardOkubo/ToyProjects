from flask import Flask, render_template, redirect
from flask_bcrypt import Bcrypt
from flask_login import (UserMixin, LoginManager, login_manager, login_user,
                         login_required, logout_user)
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

app = Flask(__name__)

app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "0123456789"  # noqa
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)


class RegisterForm(FlaskForm):
    email = StringField(
        validators=[InputRequired(), Length(min=3, max=320)],
        render_kw={"placeholder": "example@email.com"})

    password = PasswordField(
        validators=[InputRequired(), Length(min=8, max=20)],
        render_kw={"placeholder": "********"})
    
    submit = SubmitField("Register")

    def validate_email(self, email):
        existing_email = User.query.filter_by(email=email.data).first()

        if existing_email:
            raise ValidationError(
                "That email already exists. Please choose a different one.")


class LoginForm(FlaskForm):
    email = StringField(
        validators=[InputRequired(), Length(min=3, max=320)],
        render_kw={"placeholder": "example@email.com"})

    password = PasswordField(
        validators=[InputRequired(), Length(min=8, max=20)],
        render_kw={"placeholder": "********"})
    
    submit = SubmitField("Login")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        # TODO(RichardOkubo): handle exception ValidationError

        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect("login")

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect("dashboard")

    return render_template("login.html", form=form)


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    return render_template("dashboard.html")
