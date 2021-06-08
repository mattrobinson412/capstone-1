"""Super duper cool stuff."""

from flask import Flask, render_template, redirect, session, flash, g
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager, login_required, logout_user, current_user
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

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///tes_lib'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = keys
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


# Flask-Login features ==============================>
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/logout", methods=["GET", "POST"])
@login_required
def handle_user_logout():
    """Handles the logging out of a user."""
    
    user = User.query.get(current_user.id)

    if user.status_id == 1:
        logout_user()
        return redirect("/home")
    if user.status_id == 2:
        logout_user()
        return redirect("/home")
    if user.status_id == 3:
        logout_user()
        return redirect("/home")
    else:
        return redirect("/home/404")


# ROUTES ============================================>
@app.route('/logo')
@login_required
def redirect_home():
    """Redirects users to their respective dashboards."""

    user = User.query.get(current_user.id)

    if user.status_id == 1:
        return redirect('/admin/home')

    if user.status_id == 2:
        return redirect('/alumni/home')

    if user.status_id == 3:
        return redirect('/student/home')

    else:
        return redirect('/home/404')


@app.route('/settings')
@login_required
def redirect_proper_settings():
    """Redirects users to their respective settings."""

    user = User.query.get(current_user.id)

    if user.status_id == 1:
        return redirect('/admin/settings')

    if user.status_id == 2:
        return redirect('alumni/settings')

    if user.status_id == 3:
        return redirect('student/settings')

    else:
        return redirect("/home/404")


@app.route('/')
def show_homepage():
    """Shows homepage for the TES Archives App."""

    return redirect("/home")