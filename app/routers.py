

from flask import render_template, redirect, flash
from app import app
from app.forms import LoginForm, RegistrationForm


@app.route('/')
def index():
    user = {'username': 'Иван',
            'age': '17',
            'status': 'offline'}
    title= 'Старт!'
    return render_template('index.html', user=user, title=title)



@app.route('/users')
def users():
    all_users = [
    {'username': 'Иван','age': '17','status': 'offline'},
    {'username': 'Арсений', 'age': '19', 'status': 'online'},
    {'username': 'Александр', 'age': '14', 'status': 'offline'},
    {'username': 'Дмитрий', 'age': '16', 'status': 'online'},
    {'username': 'Андрей', 'age': '15', 'status': 'online'},
    ]
    return render_template('users.html', all_users=all_users)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Вы вошли как {}'.format(
            form.username.data))
    return render_template('login.html', form=form)


@app.route('/register', methods=["GET", "POT"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Вы зарегистрировались как {}'.format(form.username.data))
    return render_template('register.html', form=form)