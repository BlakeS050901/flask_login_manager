from flask import Blueprint, render_template, redirect, url_for, session, flash
from forms import login, ForgotPassword1, ChangePassword
from models import User
from extensions import bcrypt, db
from random import randint
from email_handler import code_send
# Define a Blueprint
main = Blueprint('main', __name__, template_folder='../templates', static_folder='static')


'''
SORT OUT THE LOGIN SYSTEM
'''


@main.route('/', methods=['GET', 'POST'])
def log_in():
    users = User.query.all()
    for user in users:
        print(user.email)
    form = login()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(email=username).first()
        if user:
            if bcrypt.check_password_hash(user.password, password):
                flash('Logged in!', 'success')
                return redirect('/home')
            else:
                flash('Incorrect Password', 'danger')
                return redirect('/')
        else:
            new_user = User(email=username, password=bcrypt.generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            flash('User not found!', 'danger')
            return redirect('/')
    return render_template('login.html', form=form)


@main.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password1():
    form = ForgotPassword1()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if user:
            code = randint(10000, 999999)
            response = code_send(email, code)
            if response:
                session['code'] = code
                session['email'] = email
                flash(f'Email sent to {email}!', 'success')
                return redirect(url_for('main.change_password'))
        else:
            flash('User not found!', 'danger')
    return render_template('forgot_password.html', form=form)


@main.route('/change_password', methods=['GET', 'POST'])
def change_password():
    form = ChangePassword()
    if form.validate_on_submit():
        code = form.email_code.data
        password = form.password.data
        email = session['email']
        if str(code) == str(session['code']):
            print('Code correct')
            user = User.query.filter_by(email=email).first()
            user.password = bcrypt.generate_password_hash(password)
            db.session.commit()
            flash('Password changed!', 'success')
            return redirect('/')
    return render_template('password_reset.html', form=form)



'''
Pricing-related routes
'''


@main.route('/home')
def home():
    return render_template('index.html')


