"""Super duper cool stuff."""

from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from .api.api import api
from .admin.admin import admin
from .alumni.alumni import alumni 
from .classes.classes import classes
from .donate.donate import donate
from .donor.donor import donor
from .home.home import home
from .resources.resources import resources
from .student.student import student 
from .models import *
from .secrets import secretz
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///tes_lib'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secretz
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

toolbar = DebugToolbarExtension(app)
connect_db(app)

db.drop_all()
db.create_all()


app.register_blueprint(api,url_prefix='/api')
app.register_blueprint(home,url_prefix='/home')
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(alumni,url_prefix='/alumni')
app.register_blueprint(student,url_prefix='/student')
app.register_blueprint(classes,url_prefix='/classes')
app.register_blueprint(resources,url_prefix='/resources')
app.register_blueprint(donor,url_prefix='/donor')
app.register_blueprint(donate,url_prefix='/donate')


# ROUTES ============================================>
@app.route('/')
def redirect_home():
    """Redirects visitors to the homepage."""

    

    return redirect('/home')