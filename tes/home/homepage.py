from flask import Blueprint, request, render_template, redirect, session, flash, g
import requests
import models
from .forms import ContactForm

home = Blueprint('home', __name__, template_folder='templates', static_folder='static')


# ===================== '/home' ROUTES ==========================================>
@home.route('/')
def home_page():
    """Shows homepage for TES Archives application."""

    return render_template("home/home.html")


@home.route('/contact', methods=['GET', 'POST'])
def handle_contact_form():
    """Shows a form for leaving a message and validates it upon completion."""

    form = ContactForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        message = form.message.data
        c = Contact(first_name=first_name, last_name=last_name, email=email, message=message)
        db.session.add(c)
        db.session.commit()

        flash(f"Thanks {first_name}, your message has been sent! We will be in touch as soon as we can.")
        return redirect("/")
    
    else:
        flash("Sorry! Something went wrong with your entry. Please try again.")
        return render_template("home/contact.html", form=form)


@home.route('/login')
def show_login_cards():
    """Shows cards for Admin, Alumni, and Student login portals."""

    return render_template("home/login.html")

