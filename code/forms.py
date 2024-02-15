from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class login(FlaskForm):
    username = StringField('Email:', validators=[DataRequired(), Email(), Length(min=6, max=80)])
    password = PasswordField('Password:', validators=[DataRequired(), Length(min=8, max=50)])
    submit = SubmitField('Submit')


class ForgotPassword1(FlaskForm):
    email = StringField('Email:', validators=[DataRequired(), Email(), Length(min=6, max=80)])
    submit = SubmitField('Submit')


class ChangePassword(FlaskForm):
    email_code = StringField('Email Code:', validators=[DataRequired(), Length(min=4, max=80)])
    password = PasswordField('Password:', validators=[DataRequired(), Length(min=8, max=50),
                                                      EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm Password:')
    submit = SubmitField('Submit')
