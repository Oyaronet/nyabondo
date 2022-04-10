from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(),
              Length(min=16, max=120, message="Your username must be between 16-120!")])
    password = PasswordField("Password", validators=[DataRequired(message=
              "This field cannot be empty!")])
    button = SubmitField('LOG IN')