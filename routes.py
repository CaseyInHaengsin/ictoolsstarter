from flask import render_template, redirect, request, url_for
from app import app
from app.forms import LoginForm
from flask_mongoengine.wtf import model_form
from app.database import User, Account, CreateAccount

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User()
        user.username = form.username.data
        user.password = form.password.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


        

@app.route('/create_account')
def create_account():
    form = CreateAccount(Account)
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('createaccount.html', form=form)