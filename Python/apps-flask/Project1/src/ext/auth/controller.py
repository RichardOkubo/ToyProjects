from werkzeug.security import generate_password_hash, check_password_hash

from src.ext.auth.models import User
from src.ext.database import db


def create_user(username, email, password):
    """Register a user in the database."""

    user = User(
        username=username,
        email=email,
        password=generate_password_hash(password),
    )

    # TODO(RichardOkubo): Tratar 'exception' caso 'user' já exista
    db.session.add(user)
    db.session.commit()

    return user


def search_user(form):
    return User.query.filter_by(email=form.email.data).first()


def verify_password(user, form):
    return check_password_hash(user.password, form.password.data)
