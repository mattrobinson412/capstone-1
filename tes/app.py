"""Super duper cool stuff."""

from flask import Flask, render_template, redirect, session, flash, g
from flask_debugtoolbar import DebugToolbarExtension
from api.apis import api
from admin.admins import admin
from alumni.alumnus import alumni
from classes.courses import classes
from donate.donates import donate
from donor.donors import donor
from home.homepage import home
from resources.resource import resources
from student.students import student
from models import *
from secret import *
# import seed
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///tes_lib'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "FunInTheSun98"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

toolbar = DebugToolbarExtension(app)

def connect_to_database(app):
    import models
    return models.connect_db(app)

def load_seed_file():
    import models
    import seed
    return seed.load_test_data(models.db)

connect_to_database(app)
load_seed_file()


app.register_blueprint(api,url_prefix='/api')
app.register_blueprint(home,url_prefix='/home')
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(alumni,url_prefix='/alumni')
app.register_blueprint(student,url_prefix='/student')
app.register_blueprint(classes,url_prefix='/classes')
app.register_blueprint(resources,url_prefix='/resources')
app.register_blueprint(donor,url_prefix='/donor')
app.register_blueprint(donate,url_prefix='/donate')


if __name__ == '__main__':
    app.run(host='0.0.0.0')


# ROUTES ============================================>
@app.route('/')
def redirect_home():
    """Redirects visitors to the homepage."""

    return redirect('/home')