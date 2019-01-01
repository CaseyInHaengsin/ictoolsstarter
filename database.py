from app import app
from app import db
from flask_mongoengine.wtf import model_form
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField

db.init_app(app)



class User(db.Document):
    username = db.StringField()
    password = db.StringField(max_length=256)
    email = db.EmailField()
    meta = {
        'collection': 'users'
    }
    

class Account(db.Document):
    username = db.StringField('Username', required=True, validators=[DataRequired()])
    password = db.StringField('Password', max_length=256)
    submit = SubmitField('Create Account')
    meta = {
        'collection': 'users'
    }

CreateAccount = model_form(Account)