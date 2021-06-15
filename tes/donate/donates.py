from flask import Blueprint, request, render_template
import requests
import sys
sys.path.append("C:/Users/12392/Desktop/.vscode/Springboard/Projects/capstones/capstone-1/tes")
import models

donate = Blueprint('donate', __name__, template_folder='templates', static_folder='static')


# =====================================================
@donate.route("/")
def donate_landing_page():
    """Render landing page for /donate section."""

    return render_template("donate/donate.html")