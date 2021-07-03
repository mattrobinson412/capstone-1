from flask import Blueprint, request, render_template, redirect, flash, url_for, session, g
from flask_login import login_required, login_user, logout_user, current_user
import requests
import sys
sys.path.append("C:/Users/12392/Desktop/.vscode/Springboard/Projects/capstones/capstone-1/tes")
from models import *
from .forms import *

student = Blueprint('student', __name__, 
                            template_folder='templates',  
                            # static_url_path='static',  ----- fix in UI stage!!!
                            static_folder='static')


# Alumni 'login/logout' routes ###############################
@student.route("/login", methods=["GET", "POST"])
def handle_student_login():
    """Handle login function for a Student user."""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.email.data,
                                 form.password.data)

        if user:
            # IMPLEMENT authentication! ##############
            login_user(user)

        
            ##########################################
            return redirect("/student/home")

        else:
            flash("Invalid credentials. Please try again.", 'danger')
        
    return render_template('/student/login.html', form=form)


# @student.route("/logout", methods=["GET", "POST"])
# @login_required
# def handle_student_logout():
#     """Handle logout function for a Student user."""
#     user = User.query.get(current_user.id)
#     if user.status_id != 3:
#         return redirect("/home/404")
#     else:
#         logout_user()
#         return redirect(url_for('redirect_home'))


# Alumni 'general' routes ###############################
@student.route("/home")
@login_required
def show_student_homepage():
    """Shows homepage for a Student User."""

    user = User.query.get(current_user.id)
    if user.status_id != 3:
        return redirect("/home/404")
    else:
        return render_template("student/home.html", user=user)


@student.route("/contact", methods=["GET", "POST"])
@login_required
def handle_student_contact():
    """Shows a form for leaving a message and validates it upon completion."""

    user = User.query.get(current_user.id)
    if user.status_id != 3:
        return redirect("/home/404")
    else:
        form = ContactForm()

        if form.validate_on_submit():
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            message = form.message.data
            c = Contact(first_name=first_name, last_name=last_name, email=email, message=message)
            db.session.add(c)
            db.session.commit()

            user = User.query.get(current_user.id)

            return redirect("/student/home")
        
        else:
            return render_template("student/contact.html", form=form)


@student.route("/settings", methods=["GET", "POST"])
@login_required
def change_student_settings():
    """Allow Student user to see and handle contact forms from the homepage."""
    
    user = User.query.get(current_user.id)
    if user.status_id != 3:
        return redirect("/home/404")
    else:
        form = EditUserForm(obj=user)

        if form.validate_on_submit():
            first_name = form.first_name.data
            last_name = form.last_name.data
            phone_number = form.phone_number.data
            email = form.email.data
            password = form.password.data

            user.first_name = first_name
            user.last_name = last_name
            user.phone_number = phone_number
            user.email = email
            user.password = password
            db.session.commit()
            return redirect(f"/student/home")

        else:
            return render_template("/student/settings.html", form=form, user=user)
