from flask import Blueprint, render_template, redirect
from flask_login import login_user, logout_user

from src.ext.auth.form import SignUpForm, LoginForm
from src.ext.auth.controller import create_user, search_user, verify_password

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        create_user(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        return redirect("login")

    return render_template("signup.html", form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    
    form = LoginForm()

    print(form.errors)

    if form.validate_on_submit():
        user = search_user(form)

        if not user or not verify_password(user, form):
            # TODO(RichardOkubo): add a flash for error
            return redirect("login")        

        login_user(user)
        # TODO(RichardOkubo): add a flash for success
        return redirect("/")

    return render_template("login.html", form=form)


@bp.route("/logout")
def logout():
    logout_user()
    return redirect("/")
