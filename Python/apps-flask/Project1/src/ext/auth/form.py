import wtforms as wtf

from flask_wtf import FlaskForm


class SignUpForm(FlaskForm):
    username = wtf.StringField(
        "Username",
        [wtf.validators.DataRequired(), wtf.validators.length(max=20)]
    )
    email = wtf.StringField(
        "Email",
        [wtf.validators.DataRequired(), wtf.validators.Email()]
    )
    password = wtf.PasswordField(
        "Password",
        [wtf.validators.DataRequired()]
    )


class LoginForm(FlaskForm):
    email = wtf.StringField(
        "Email",
        [wtf.validators.DataRequired(), wtf.validators.Email()]
    )
    password = wtf.PasswordField(
        "Password",
        [wtf.validators.DataRequired()]
    )