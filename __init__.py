from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config['SECRET_KEY'] = 'cant stop'
app.config['MONGODB_SETTINGS'] = {
    'db': 'ictools',
    'host': 'mongodb://localhost/ictools'
}
bootstrap = Bootstrap(app)
db = MongoEngine()



from app import routes, database

