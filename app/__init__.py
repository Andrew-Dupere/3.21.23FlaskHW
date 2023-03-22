from flask import Flask

app = Flask(__name__)

#import all of the routes from the routes file into current package

from . import routes

app.config['SECRET_KEY'] = 'you-will-never-guess'