from app import app
from flask import render_template

@app.route('/')
@app.route('/shop')
def index():
    return render_template('index.html', title='Shop')


@app.route('/register')
def register():
    return render_template('register.html', title='Register')


@app.route('/login')
def login():
    return render_template('login.html', title='Login')