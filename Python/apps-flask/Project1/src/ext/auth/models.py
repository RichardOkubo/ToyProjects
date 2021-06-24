from flask_login import UserMixin

from src.ext.database import db
from src.ext.auth import login_manager


@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()


class User(db.Model, UserMixin):
    __tablename__ = "users"
    
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.Unicode, nullable=False)
    email = db.Column("email", db.Unicode, unique=True, nullable=False)
    password = db.Column("passwd", db.Unicode, nullable=False)

    def __repr__(self):
        return self.username
