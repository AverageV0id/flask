from flask import render_template
from app import app


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